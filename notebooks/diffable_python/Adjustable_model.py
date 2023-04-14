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

# # Creating an interactive modelling tool with widgets to adjust variables

# +
import os
import pandas as pd
import ipywidgets as widgets
from IPython.display import display, Markdown
from ipywidgets import Layout

from model import cost_model
dispensing = 1.26

# +
df_ltc = pd.read_csv(os.path.join("..", "data", "ltc_qty_cost.csv"))

# calculate cost per item
data = df_ltc.set_index("pct").sort_index()
# add a total row
data = data.append(data.sum().rename("All")).reset_index()

# calculate additional fields
data["percent_28d"] = 100*data['items_28d']/data['total_items']
data["cost_per_item"] = data['net_cost_28d']/data['items_28d']


prescriptions = data.loc[data["pct"]=="All", "items_28d"].item() 
priceperitem = data.loc[data["pct"]=="All", "cost_per_item"].item()

data.tail()
# -

# ## Create a simple interactive tool

# +
# ensure tests pass despite conflict with widget output:
# NBVAL_IGNORE_OUTPUT 

# Selection widget:
#ccg_selector = widgets.Dropdown(options=data[["pct","items"]].to_numpy().tolist(), value=prescriptions, description='CCG:', disabled=False)
ccg_selector = widgets.Dropdown(options=data["pct"], value="All", description='CCG:', disabled=False)

# make widget titles fit by setting the style
style = {'description_width': 'initial'}


### Sliders for other variables:

months_supply_slider = widgets.IntSlider(min=1, max=4, step=1, description='Months supply:', style=style, value=3)

# proportion of prescriptions amenable to change
percent_amenable_slider = widgets.FloatSlider(min=0.2, max=0.95, step=0.05, description='Proportion amenable:', style=style, value=0.9)

# proportion of prescriptions approved by a GP
prop_doc_slider = widgets.FloatSlider(min=0.1, max=0.9, step=0.1, description='Proportion GP:', style=style, value=0.5)

# time taken to approve a repeat prescription (minutes)
time_slider = widgets.FloatSlider(min=0.1, max=2, step=0.1, description='Time per presc (min):', style=style, value=0.5)

# proportion of prescriptions on electronic repeat dispensing (assume zero cost - or one cost per 12 months?)
prop_erd_slider = widgets.FloatSlider(min=0, max=1, step=0.1, description='e-RD proportion:', style=style, value=0.5)

# price per item
#priceperitem_slider = widgets.FloatSlider(min=0.5, max=2, step=0.1, description='Price per item (£):', style=style, value=0.8)

# cost of public time per minute
cost_public_slider = widgets.IntSlider(min=5, max=15, step=1, description='Cost of public time per hour (£):', style=style, value=11)

# time to collect prescription (minutes)
time_collect_slider = widgets.IntSlider(min=0, max=30, step=1, description='Time to collect (min):', style=style, value=10)

    
def f(ccg_selector, months_supply_slider, percent_amenable_slider, prop_doc_slider, time_slider, prop_erd_slider, 
      cost_public_slider, time_collect_slider):
    
    ccg = ccg_selector
    months_supply = months_supply_slider
    percent_amenable = percent_amenable_slider
    prop_doc = prop_doc_slider
    t = time_slider
    prop_erd = prop_erd_slider
    #priceperitem = priceperitem_slider
    cost_public = cost_public_slider
    time_collect = time_collect_slider
    
    # items and cost per item, using ccg from dropdown
    prescriptions = data.loc[data["pct"]==ccg, "items_28d"].item() 
    percent_28d = data.loc[data["pct"]==ccg, "percent_28d"].item() 
    priceperitem = data.loc[data["pct"]==ccg, "cost_per_item"].item()

    
    results = cost_model(prescriptions, months_supply, percent_amenable, dispensing, prop_doc, prop_erd, t, priceperitem, cost_public, time_collect)
    
    dispensing_fees = results['dispensing']    
    staff_cost = results['staff']
    waste = results['waste']
    patient_cost = results['patient']

    print(f'Total 28-day prescriptions = {prescriptions:,.0f} \n'
          f'Percent 1 month (of all 1+2+3 month prescriptions) = {percent_28d:,.0f}% \n'
          f'Mean price per item = £{priceperitem:,.2f} \n'
          f'\n'
          f'Dispensing fees =  £{dispensing_fees/1E6:,.1f} M \n'
          f'Staff cost =  £{staff_cost/1E6:,.1f} M \n'
          f'Wasted meds =  £{waste/1E6:,.1f} M \n'
          f'Patient cost =  £{patient_cost/1E6:,.1f} M \n \n'
          f'Overall impact: =  £{(staff_cost+ waste+ patient_cost)/1E6:,.1f} M'
         )

out = widgets.interactive_output(f, 
                                 {'ccg_selector': ccg_selector,
                                  'months_supply_slider': months_supply_slider, 
                                  'percent_amenable_slider': percent_amenable_slider,
                                  'prop_doc_slider': prop_doc_slider, 
                                  'time_slider': time_slider, 
                                  'prop_erd_slider': prop_erd_slider,
                                  #'priceperitem_slider': priceperitem_slider, 
                                  'cost_public_slider': cost_public_slider, 
                                  'time_collect_slider': time_collect_slider})


widgets.HBox([widgets.VBox([months_supply_slider, percent_amenable_slider, prop_doc_slider, time_slider, prop_erd_slider, 
      cost_public_slider, time_collect_slider, ccg_selector, out])])
# -

# Display static output
f(ccg_selector="All", 
  months_supply_slider = 3, 
  percent_amenable_slider = 0.9, 
  prop_doc_slider = 0.5, 
  time_slider=0.5, 
  prop_erd_slider=0.5, 
  cost_public_slider=11, 
  time_collect_slider=10)
