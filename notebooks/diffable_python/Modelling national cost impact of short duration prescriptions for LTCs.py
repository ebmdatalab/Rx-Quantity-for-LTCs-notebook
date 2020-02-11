# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Aim: To model the cost impact of dispensing one month rather than 2 or 3 months
#
# We examined the cost of a policy switch to recommend two or three monthly prescriptions across the NHS where there is no clinical rationale for issuing shorter durations. We estimated the cost to the NHS in ££, 
# - savings to  NHS in staff time, 
# - savings in time for patients and 
# - the estimated economic burden that would be relieved. 

# ### What are the costs to include?

# > Longer prescription lengths were associated with more medication waste per prescription. However, when including dispensing fees and prescriber time, longer prescription lengths resulted in lower TUC. This finding was consistent across all five cohorts. Savings ranged from £8.38 to £12.06 per prescription per 120 days if a single long prescription was issued instead of multiple short prescriptions. Prescriber time costs accounted for the largest component of TUC.
#
# [Doble et al 2017]
#
# **1. Dispensing fees**
#
# - Currently 126p per item. 
# - Plus 2% of the cost per prescription (cost per day multiplied by prescription length) for prescriptions over £100 \*see below
#
# (https://psnc.org.uk/dispensing-supply/endorsement/fees-allowances/) 
#
# **2. Prescriber time**
#
# Depending on the item, the prescriber time per prescription varies [Doble et al 2017]
# - antihypertensives: £3.77 (in 3-month scenario), £3.76 (28 days)	
# - diabetes: £3.55 (in 3-month scenario), £3.54 (28 days)	
# - SSRIs: £3.18 (in 3-month scenario), £3.23 (28 days)
#
# Note they use Figures from Curtis et al 2015, which are:
# - GP time £3.80/min, all practice expenses and including qualification costs (excluding quals it would be £3.20/min) - however, these are costs per minute **of patient contact** i.e. denominator used to calculate this rate was total patient contact time rather than total working hours?  
# - GP Nurse time £0.93/min (£56/hr per hour of F2F contact time), including qualification costs. (Basic rate is £36/hr / 0.6/min)
#
# Latest GP/nurse Figures from Curtis et al 2019:
# - GP  £132/hr (£2.20/min)
# - Nurse £37/hr (£0.62/min)
#
# With electronic repeat _dispensing_, it is possible that 12 months' of 28+ days' supply are authorised in one go, which means that changing the duration of each prescription would have no effect on prescriber time. With repeat _prescribing_, the patient must still request each prescription from the practice. 
#
# **3. Wastage**
#
# Depending on the item, the longer the duration, the more medicines will be wasted [Doble et al 2017]
# - antihypertensives: £0.51 (in 3-month scenario), £0.07 (28 days)	
# - diabetes: £1.37 (in 3-month scenario), £0.33 (28 days)	
# - SSRIs: £0.43 (in 3-month scenario), £0.21 (28 days)
#
# - For statins (secondary prevention) they found that 3.325% days of shorter duration 
#   (under 60 days) prescription supplies were wasted,
#   compared to 3.663% of longer duration (>=60 days) prescriptions. 
#
# **4. Patient time and expenses**
#
# **5. Income generation**
#
# **6. Errors**
#
# **Refs**
# - *Doble B, Payne R, Harshfield A, Wilson EC. BMJ Open. 2017;7(12):e019382.*
# - *Curtis L , Burns A . Unit Costs of Health and Social Care. Canterbury, UK: Personal Social Services Research Unit, The University of Kent, 2015*

# **Fees for expensive prescriptions (over £100)**
#
# Not a consideration for the drugs we are looking at, all of which are available generically:
# - Ramipril £2-5 /pack https://openprescribing.net/tariff/?codes=0205051R0AAADAD&codes=0205051R0AAANAN&codes=0205051R0AAAAAA&codes=0205051R0AAAKAK&codes=0205051R0AAABAB&codes=0205051R0AAALAL&codes=0205051R0AAACAC&codes=0205051R0AAAMAM
# - Atorvastatin <£2/pack https://openprescribing.net/tariff/?codes=0212000B0AAAAAA&codes=0212000B0AAABAB&codes=0212000B0AAACAC&codes=0212000B0AAADAD
# - Simvastatin <£2/pack https://openprescribing.net/tariff/?codes=0212000Y0AAAAAA&codes=0212000Y0AAABAB&codes=0212000Y0AAADAD&codes=0212000Y0AAAHAH
# - Levothyroxine max £15/pack during 18-19 https://openprescribing.net/tariff/?codes=0602010V0AABZBZ&codes=0602010V0AAGHGH&codes=0602010V0AABWBW&codes=0602010V0AABXBX&codes=0602010V0AABYBY
# - Amlodipine <£2/pack https://openprescribing.net/tariff/?codes=0206020A0AAABAB&codes=0206020A0AAAAAA

# **Example**
#
# > **Three-Month Versus 28-Day Prescribing of Antihypertensives**
#
# > We conducted two analyses representing alternative scenarios. 
# In both cases we first added in the transaction and drug wastage costs (Table 3). 
#
# > For the 3-month arm this equated to an extra 
# £21.01 per annum [= dispensing fees (£0.90) + prescriber time (£3.77) + wastage costs (£0.51) × (365/90)], 
#
# > and in the 28-day arm, 
# £61.68 [= dispensing fees (£0.90) + prescriber time (£3.76) + wastage costs (£0.07) × (365/28)].
#
# From Martin A, Payne R, Wilson EC. Appl Health Econ Health Policy 2018;16:317–30. doi:10.1007/s40258-018-0383-9

# # Calculations

# ## 1. Dispensing fees

# - 126p - cost per item dispensed (not divided across items on same prescription form)
# - Currently 60% of our selected items are dispensed in 28-day packs.
#

print ("total dispensing cost for 1, 4, 8 or 12 week supplies: £%4.1f M"%(1.26*(2674229+16212361+4604721+423880)/1E6))
print ("total dispensing cost for 4-week / one month prescriptions: £%4.1f M"%(1.26*16212361/1E6))

# +
# We assume that approx 10% of one-month prescriptions are appropriate (e.g. newly initiated patients). 

# Calculate cost of dispensing 90% of prescriptions in 3-month batches
n=0.9*1.26*16212361/3

print ("potential reduction in cost if 90 percent one-month prescriptions were 3-months: £%4.1f M"%(n/1E6))
# -

# ## 2. Prescriber time

# +
#Latest GP/nurse overall cost figures from Curtis et al 2019:

#GP £132/hr (£2.20/min)
#Nurse £37/hr (£0.62/min)

cdoc = 2.2 # cost per minute for GP time
cnur = 0.62 # cost per minute for nurse time

# note the values for the following variables are selected arbitrarily

prop_doc = 0.5 # proportion approved by a GP
prop_nur = 1-prop_doc # proportion approved by a nurse

t = 0.5 # time taken to approve a repeat prescription (minutes)
prop_erd = 0.5 # proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)

cpp_doc = cdoc*t*(1-prop_erd) # cost per average prescription (doc)
cpp_nur = cnur*t*(1-prop_erd) # cost per average prescription (nur)


print ("£{:,.0f}".format(16212361*((prop_doc*cpp_doc) + (prop_nur*cpp_nur))), " cost to approve all 28-day prescriptions")
print ("£{:,.0f}".format(16212361*(0.1+0.9/3)*((prop_doc*cpp_doc) + (prop_nur*cpp_nur))), " cost to approve if 90% 28-day prescriptions were 84-days")
# -

# ## 3. Wastage

# +
# For statins (secondary prevention Doble et al found that 3.325% days of shorter duration (\<60 days) prescription supplies
# were wasted, compared to 3.663% of longer duration  (\>=60 days) prescriptions. 
# [Doble et al 2017]

# Atorvastatin 20mg averaged around 80p per 28-tablet pack in 2018-19 (eyeballed)
p = 0.8
print ("£%8.5f"%(p*0.03325), " (3.325%) wasted per 28-day supply")
print ("£%8.5f"%(3*p*0.03663), " (3.663%) wasted per 84-day supply")
# -

# Assuming this scales up to all of our 5 prescriptions...
print ("£{:,.0f}".format(p*0.03325*16212361), " (3.325%) wasted of all 28-day supplies")
print ("£{:,.0f}".format(p*0.03663*16212361*3), " (3.663%) wasted if all 28-day supplies were 84-day")
print ("£{:,.0f}".format((p*0.03663*16212361*3*0.9) + (p*0.03325*16212361*0.1)), " wasted if 90% of all 28-day supplies were 84-day")

# ## 4. Patient time and expenses

# - Time required to travel to pharmacy / GP?
# - DIfferences for dispensing practices (>1.6m)?
# - Time taken to collect prescription? Under electronic prescribing prescriptions may already be ready to collect when the patient arrives. 
#
#
# - Sliding scale might be the best way! 
# - The majority of population live within 20 mins walk of a pharmacy (few years old maybe)

# +
# Conservatively assume 10 mins per prescription (a low estimate to account for most people going to the pharmacy while nearby)
t = 10

print ("{:,.0f}".format(t*16212361/60), " total patient hours to collect all 28-day supplies")
print ("{:,.0f}".format(t*16212361/60/3), " total patient hours if all 28-day supplies were 84 days")
print ("{:,.0f}".format(((0.1)+(0.9/3))*(t*16212361/60)), " total patient hours if 90% 28-day supplies were 84 days")
print ("{:,.1f}".format((t*12/60)), " hours per patient per year on 28-day supplies")
print ("{:,.1f}".format((t*12/60/3)), " hours per patient per year on 84-day supplies")


# + collapsed=true jupyter={"outputs_hidden": true}
# IFS should have an estimate somewhere for the cost of public time... 
# -

# ## 5. Income generation

# Patients eligible to pay for prescriptions pay a fixed amount per prescription which contributes towards the total prescribing bill. For each prescription dispensed for 84 rather than 28 days, income would be reduced by 2/3.
#
# However, the majority of prescriptions (90%?) are exempt from charges, for example over 60s, under 19s, people on low incomes etc. Those eligible to pay who collect a lot of medications can have their total capped. 
#
# Therefore, for the medications we are considering we may expect that >95% of the prescriptions (2x statins, largely over-60s) are not paid for by patients. 
#
# Crucially, where patients pay for routine prescriptions, it is likely that they are already given 84 days supply to reduce the cost burden on them.
#
# Therefore, we would expect a very small decrease in income from changing patients from 28 day prescriptions to longer durations.

# # Model

# +
#Common Variables
prescriptions = 16212361 # total 28-day prescriptions
percent_amenable = 0.9 # proportion of prescriptions amenable to change to longer durations 0.5-0.95
months_supply = 3 # 2-4


# Dispensing fees
# Calculate cost of dispensing 90% of prescriptions in 3-month batches
def calculate_dispensing_fees(prescriptions, months_supply, percent_amenable):
    return percent_amenable*1.26*prescriptions/(months_supply)


# Staff Cost
prop_doc = 0.5 # proportion approved by a GP
t = 0.5 # time taken to approve a repeat prescription (minutes)
prop_erd = 0.5 # proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)

def calculate_staff_cost(prescriptions, months_supply, percent_amenable, prop_doc, prop_erd, t):
    cdoc = 2.2 # cost per minute for GP time
    cnur = 0.62 # cost per minute for nurse time
    prop_nur = 1-prop_doc # proportion approved by a nurse
    cpp_doc = cdoc*t*(1-prop_erd) # cost per average prescription (doc)
    cpp_nur = cnur*t*(1-prop_erd) # cost per average prescription (nur)
    
    return prescriptions*((1-percent_amenable)+percent_amenable/months_supply)*((prop_doc*cpp_doc) + (prop_nur*cpp_nur))


# Wastage
priceperitem = 0.8 # average cost per box (28-day supply)

def calculate_waste(prescriptions, months_supply, percent_amenable, priceperitem):
    return (priceperitem*0.03663*prescriptions*percent_amenable*months_supply) + (priceperitem*0.03325*prescriptions*(1-percent_amenable))


#Patient Cost
cost_public = 1 # cost of public time per minute
time_collect = 10 # time to collect prescription (minutes) (0-60)

def calculate_patient_cost(prescriptions, months_supply, percent_amenable, cost_public, time_collect):
    return (cost_public*((1-percent_amenable)+(percent_amenable/months_supply))*(time_collect*prescriptions/60))

    
dispensing_fees = calculate_dispensing_fees(prescriptions, months_supply, percent_amenable)    
staff_cost = calculate_staff_cost(prescriptions, months_supply, percent_amenable, prop_doc, prop_erd, t)
waste = calculate_waste(prescriptions, months_supply, percent_amenable, priceperitem)
patient_cost = calculate_patient_cost(prescriptions, months_supply, percent_amenable, cost_public, time_collect)
    

# +
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Layout

prescriptions = 16212361 # total 28-day prescriptions

# make widget titles fit by setting the style
style = {'description_width': 'initial'}


months_supply_slider = widgets.IntSlider(min=2, max=4, step=1, description='Months supply:', style=style, value=3)

# proportion of prescriptions amenable to change
percent_amenable_slider = widgets.FloatSlider(min=0.2, max=0.95, step=0.05, description='Proportion amenable:', style=style, value=0.9)

# proportion of prescriptions approved by a GP
prop_doc_slider = widgets.FloatSlider(min=0.1, max=0.9, step=0.1, description='Proportion GP:', style=style, value=0.5)

# time taken to approve a repeat prescription (minutes)
time_slider = widgets.FloatSlider(min=0.1, max=2, step=0.1, description='Time per presc (min):', style=style, value=0.5)

# proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)
prop_erd_slider = widgets.FloatSlider(min=0, max=1, step=0.1, description='e-RD proportion:', style=style, value=0.5)

# price per item
priceperitem_slider = widgets.FloatSlider(min=0.5, max=2, step=0.1, description='Price per item (£):', style=style, value=0.8)

# cost of public time per minute
cost_public_slider = widgets.IntSlider(min=5, max=15, step=1, description='Cost of public time (£):', style=style, value=11)

# time to collect prescription (minutes)
time_collect_slider = widgets.IntSlider(min=0, max=30, step=1, description='Time to collect (min):', style=style, value=10)

    
def f(months_supply_slider, percent_amenable_slider, prop_doc_slider, time_slider, prop_erd_slider, 
      priceperitem_slider, cost_public_slider, time_collect_slider):
    
    months_supply = months_supply_slider
    percent_amenable = percent_amenable_slider
    prop_doc = prop_doc_slider
    t = time_slider
    prop_erd = prop_erd_slider
    priceperitem = priceperitem_slider
    cost_public = cost_public_slider
    time_collect = time_collect_slider
    
    dispensing_fees = calculate_dispensing_fees(prescriptions, months_supply, percent_amenable)    
    staff_cost = calculate_staff_cost(prescriptions, months_supply, percent_amenable, prop_doc, prop_erd, t)
    waste = calculate_waste(prescriptions, months_supply, percent_amenable, priceperitem)
    patient_cost = calculate_patient_cost(prescriptions, months_supply, percent_amenable, cost_public, time_collect)

    print('Total prescriptions = {:,} \n'
          '\n'
          'Dispensing fees =  £{:,.0f} \n'
          'Staff cost =  £{:,.0f} \n'
          'Wasted meds =  £{:,.0f} \n'
          'Patient cost =  £{:,.0f} \n \n'
          'Overall impact: =  £{:,.0f}'
          .format(prescriptions, dispensing_fees, staff_cost, waste, patient_cost, staff_cost + waste + patient_cost),
         )

out = widgets.interactive_output(f, 
                                 {'months_supply_slider': months_supply_slider, 
                                  'percent_amenable_slider': percent_amenable_slider,
                                  'prop_doc_slider': prop_doc_slider, 
                                  'time_slider': time_slider, 
                                  'prop_erd_slider': prop_erd_slider,
                                  'priceperitem_slider': priceperitem_slider, 
                                  'cost_public_slider': cost_public_slider, 
                                  'time_collect_slider': time_collect_slider})


widgets.HBox([widgets.VBox([months_supply_slider, percent_amenable_slider, prop_doc_slider, time_slider, prop_erd_slider, 
      priceperitem_slider, cost_public_slider, time_collect_slider, out])])


# + collapsed=true jupyter={"outputs_hidden": true}
# calculate actual cost per prescription

# + collapsed=true jupyter={"outputs_hidden": true}
# link to practice-level data to allow people to choose their practice
