import pandas as pd

#### Common Variables 
prescriptions = 1E8 # total 28-day prescriptions (replace with input value)
percent_amenable = 0.9 # proportion of prescriptions amenable to change to longer durations 0.5-0.95
months_supply = 3 # 2-4


##### Dispensing fees
dispensing = 1.26
# Calculate cost of dispensing 90% of prescriptions in 3-month batches

def calculate_dispensing_fees(prescriptions, months_supply, percent_amenable, dispensing):
    return prescriptions* (# no of items
           dispensing) * ( # cost multiplier
           (1-percent_amenable)+(percent_amenable/months_supply)) # adjusted number of items


##### Staff Cost
prop_doc = 0.5 # proportion approved by a GP
t_approve = 0.5 # time taken to approve a repeat prescription (minutes)
prop_erd = 0.5 # proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)

def calculate_staff_cost(prescriptions, months_supply, percent_amenable, prop_doc, prop_erd, t):
    cdoc = 2.2 # cost per minute for GP time
    cnur = 0.62 # cost per minute for nurse time
    prop_nur = 1-prop_doc # proportion approved by a nurse
    cpp_doc = cdoc*t_approve*(1-prop_erd) # cost per average prescription (doc)
    cpp_nur = cnur*t_approve*(1-prop_erd) # cost per average prescription (nur)
    
    return prescriptions*( # no of items
           prop_doc*cpp_doc + prop_nur*cpp_nur)*( # cost multiplier
           (1-percent_amenable)+(percent_amenable/months_supply)) # adjusted number of items


##### Wastage
priceperitem = 1.04 # latest average cost per box (28-day supply) across basket of items - replace with calculated value

def calculate_waste(prescriptions, months_supply, percent_amenable, priceperitem):
    waste_s = 0.03325
    waste_l = 0.03663
    return prescriptions*(   # no of items
            priceperitem)*(  # cost multiplier
                (waste_l*percent_amenable*months_supply) + (# waste for longer prescriptions 
                # note here we multiply by months_supply rather than divide as the amount of product subject to potential waste will increase with longer duration
                waste_s*(1-percent_amenable))) # waste for remaining 28 day prescriptions


#Patient Cost
cost_public = 11 # cost of public time per hour
time_collect = 10 # time to collect prescription (min) 

def calculate_patient_cost(prescriptions, months_supply, percent_amenable, cost_public, time_collect):
    return prescriptions*( # no of items
           cost_public*time_collect/60)*(  # cost multiplier
           (1-percent_amenable)+(percent_amenable/months_supply)) # adjusted number of items
           

def cost_model(prescriptions, months_supply, percent_amenable, dispensing, prop_doc, prop_erd, t_approve, priceperitem, cost_public, time_collect):
    dispensing_fees = calculate_dispensing_fees(prescriptions, months_supply, percent_amenable, dispensing)    
    staff_cost = calculate_staff_cost(prescriptions, months_supply, percent_amenable, prop_doc, prop_erd, t_approve)
    waste = calculate_waste(prescriptions, months_supply, percent_amenable, priceperitem)
    patient_cost = calculate_patient_cost(prescriptions, months_supply, percent_amenable, cost_public, time_collect)
    
    model_output = pd.Series(index=["dispensing","staff","waste","patient"], dtype=float)
    model_output["dispensing"] = dispensing_fees
    model_output["staff"] = staff_cost 
    model_output["waste"] = waste 
    model_output["patient"] = patient_cost
    
    return model_output
