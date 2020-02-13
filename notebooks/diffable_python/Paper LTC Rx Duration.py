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
#   widgets:
#     application/vnd.jupyter.widget-state+json:
#       state: {}
#       version_major: 2
#       version_minor: 0
# ---

# We recently launched a new measure of [seven day prescribing for long term conditions](https://openprescribing.net/measure/seven_day_prescribing/all-england/) where we found variation across the country. In the background we state that there is no consensus on duration of long term prescriptions and guidance varies throughout the country around stable long term prescriptions. Most CCGs will have some form of guidance generally for one, two or three months. 
#
# The University of Bristol have produced a [policy briefing](https://www.bristol.ac.uk/policybristol/policy-briefings/repeat-prescription-costs/) arguing that three month repeat prescriptions are more cost-effective. They base this on a systematic review and studies in CPRD. 
#
# I have had a quick skim of the systematic review (based exclusively on American data) and the CPRD study. The policy briefing states that _current guidance to issue 28-day repeat prescriptions_. This deviates from the DataLab assertion in the seven days measure that there is no consensus. Martin, Payne and Wilson study is is based on old guidance from a handful of areas. This notebook seeks to ascertain what the variation is in 28 v 56 v 84 across the country for our basket of medicines commonly prescribed once daily for long term conditions on the complete prescribing dataset for England.

# +
##importing libraries that are need to support analysis
import pandas as pd
import numpy as np
import plotly.express as px
from ebmdatalab import bq, maps, charts
import matplotlib.pyplot as plt
import os


# +
### here we extract data for modelling
sql = '''
SELECT
  pct,
  quantity_per_item,
  sum(items) as items
FROM
 ebmdatalab.hscic.raw_prescribing_normalised AS presc
INNER JOIN hscic.ccgs AS ccgs ON presc.pct=ccgs.code AND ccgs.org_type='CCG'

WHERE
(bnf_code LIKE "0205051R0%" OR  ##ramipril
bnf_code LIKE "0212000B0%" OR ##atrovastatin
bnf_code LIKE "0212000Y0%" OR ##simvastatin
bnf_code LIKE "0602010V0%" OR ##levothyroxine
bnf_code LIKE "0206020A0%") ##amlodipine
AND
(bnf_name LIKE '%_Tab%' or bnf_name LIKE '%_Cap%') ##this restricts to tablets or capsules
AND (month BETWEEN '2018-08-01'
    AND '2019-07-01')

GROUP BY
  pct,
  quantity_per_item
    '''

df_ltc = bq.cached_read(sql, csv_path=os.path.join('..','data','ltc_qty.csv'))
df_ltc.head(10)
# -

df_ltc.info()

df_rx_repeat = df_ltc.copy()
df_rx_repeat["total_quantity"] = df_rx_repeat["quantity_per_item"]*df_rx_repeat["items"] 
df_rx_repeat.tail(5)

df_rx_repeat.describe()

# There is a maximum of 8400 on a single...... That is 23 years worth of tablets, lets investigate further below.

# +

dfp = df_rx_repeat.copy()
dfp = dfp.groupby(["quantity_per_item"]).sum().reset_index()

fig = px.bar(dfp, x='quantity_per_item', y='items')
fig.update_xaxes(range=[0, 120])


fig.show()
# -

###here we make a list of durations we want to affect for later filtering
lst = [7,28,56,84]

# +
df_common = df_rx_repeat.loc[(df_rx_repeat["quantity_per_item"].isin(lst))]

print(df_common)                                                             
# -

total = df_common["total_quantity"].sum()
df_common["proportion_of_qty"] = df_common["total_quantity"]/total*100
df_common

# +
dfp = df_common.copy()
dfp = dfp.groupby(["quantity_per_item"]).sum().reset_index()

fig = px.bar(dfp, x='quantity_per_item', y='total_quantity')
fig.update_layout(
    title="Number of Tabets/Capsules for Commonly Prescribed Quantities for Commonly Prescribed Medicines")
fig.show()

# get value for percentage dispensed in each of 1/2/3 months prescriptions: 
percentage = {}
for d in lst:
    percentage[d] = dfp.loc[dfp["quantity_per_item"]==d,'proportion_of_qty'].item()

print(f"Tablets/capsules for common LTC medicines are most commonly being dispensed on 28 day prescriptions ({percentage[28]:.1f}%)",
      f"with approximately {percentage[56]:.1f}% being dispensed on two-monthly scripts.",
      f"Only {percentage[84]:.1f}% of these common medicines are being supplied on three-monthly prescriptions." )

# -

# The Bristol paper assertion that most prescribing is 28 days is correct based on our basket of common LTC medicines. They recommend three-month presctiptions as being more cost effective. Now let's look at script volume to see what the workload implications might be for our basket of common medicines.

# +
fig = px.bar(dfp, x='quantity_per_item', y='items')
fig.update_layout(
    title="Number of Items for Commonly Prescribed Quantities for Commonly Prescribed Medicines")
fig.show()

items_28d = dfp.loc[dfp["quantity_per_item"]==28,'items'].item()/10E6
print(f'There are {items_28d:,.1f}M one-month scripts for our basket of common medicines. There will be a substantial number of prescriptions that need amending.')
# -

# ## CCG Variation

df_ccg = df_ltc.groupby(['pct','quantity_per_item'])['items'].sum().reset_index()
df_ccg["total_quantity"] = df_ccg["quantity_per_item"]*df_ccg["items"] 
df_ccg.tail(5)

# +
df_common_ccg = df_ccg.loc[(df_ccg["quantity_per_item"].isin(lst))]


# +
ccg_total = df_common_ccg.groupby(["pct"]).sum().reset_index()
ccg_total=ccg_total.rename(columns = {'total_quantity':'basket_qty'}).drop(columns =['quantity_per_item', 'items']) ##we don't need two columns
ccg_total.head()


# +
ccg_map =  pd.merge(df_common_ccg,ccg_total, on="pct")  
ccg_map["proportion_of_basket"] = ccg_map["total_quantity"]/ccg_map["basket_qty"]*100
ccg_map.head()


# -

for quantity_per_item in ccg_map.quantity_per_item.unique():
    plt.figure(figsize=(20, 7))
    maps.ccg_map(
        ccg_map[ccg_map['quantity_per_item'] == quantity_per_item], 
        title= (f"Proportion of Tabets/Capsules supplied on {quantity_per_item}-day \n prescriptions for Commonly Prescribed Medicines"),
        column='proportion_of_basket', 
        separate_london=False,
        plot_options={'vmax': 100}
    )
    plt.show()

# My impression is that the 28 day supply map looks similar to SystmOne v EMIS Web [map of deployment](https://github.com/ebmdatalab/jupyter-notebooks/blob/master/General%20Practice%20EHR%20Deployment/EHR%20Deployment.ipynb)

# ## Excessive quantities in CCGs

# Above we saw that there are some excessive quantities being prescribed, one script for 8400 would equate to 23 years supply and it was prescribed in a single month. It is unlikely that it was dispensed but we will now interrogate the data to see what the true cost of excessive prescribing is. We cannot investigate further so we will create files for interested CCGs - perhaps we could do mass audit?

# +
### here we extract data for modelling
sql = '''
SELECT
  month,
  pct,
  practice,
  bnf_name,
  items,
  actual_cost,
  quantity_per_item
FROM
 ebmdatalab.hscic.raw_prescribing_normalised AS presc
INNER JOIN hscic.ccgs AS ccgs ON presc.pct=ccgs.code AND ccgs.org_type='CCG'

WHERE
(bnf_code LIKE "0205051R0%" OR  ##ramipril
bnf_code LIKE "0212000B0%" OR ##atrovastatin
bnf_code LIKE "0212000Y0%" OR ##simvastatin
bnf_code LIKE "0602010V0%" OR ##levothyroxine
bnf_code LIKE "0206020A0%") ##amlodipine
AND
(bnf_name LIKE '%_Tab%' or bnf_name LIKE '%_Cap%') ##this restricts to tablets or capsules
AND (month >= '2018-08-01'
    AND month <= '2019-07-01')
AND
quantity_per_item >= 336 ##this is one years supply
    '''

df_excess = bq.cached_read(sql, csv_path=os.path.join('..','data','ltc_qty_excess.csv'))
df_excess.head(10)
# -

df_excess.describe()

df_excess[["items","actual_cost"]].sum()

# +
# here we create csv files for each CCG to investigate further if they wish - these are now available on GitHub
for i, g in df_excess.groupby('pct'):
    if "GITHUB_WORKSPACE" not in os.environ:
        g.to_csv(os.path.join('..','data','{}.csv').format(i.split('/')[0]), index=False)
# -


#  code review improvements - what I would like to tweak
# - currently has 12 months to July 19, we should update with latest

# + collapsed=true jupyter={"outputs_hidden": true}

