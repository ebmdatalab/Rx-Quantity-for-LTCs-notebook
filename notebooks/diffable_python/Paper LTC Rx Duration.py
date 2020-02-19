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


# +
##here we want to create a larger basket building on medicines in the seven days measure basket
sql='''
SELECT
bnf.chemical,
SUM(items) AS total_items,
SUM(total_quantity) AS total_tabs_caps
FROM
  ebmdatalab.hscic.raw_prescribing_normalised AS presc
INNER JOIN
  hscic.bnf as bnf
ON
  presc.bnf_code=bnf.presentation_code
WHERE
(presentation LIKE '%_Tab%' or presentation LIKE '%_Cap%')
    AND SUBSTR(bnf_code,0,2) IN ('01','02','04','06') ## here we use common BNF chapters. Chapter 3 resp is excluded due to amount of inhalers and ch5 for short course ABx
    AND (month >= "2018-12-01") ##restrict to last 12 month
    AND (month <= "2019-11-01")
GROUP BY
bnf.chemical
ORDER BY
total_items
'''


df_total_meds = bq.cached_read(sql, csv_path='total_meds.csv')
# -

## import final list
df_total_meds .head()

##here we export to manually filter
df_for_filter = df_total_meds.sort_values("total_tabs_caps", ascending=False)
df_for_filter.to_csv('medicines_for_filter.csv')

# +
### manual_filter_list.csv - we reviewed top 50 by qty and 18 chemicals were identified for includion
## here we extract data for modelling
sql = '''
SELECT
  pct,
  items,
  quantity_per_item
FROM
 ebmdatalab.hscic.raw_prescribing_normalised AS presc
JOIN
  hscic.ccgs AS ccgs
ON
presc.pct=ccgs.code
WHERE
(bnf_code LIKE "0205051R0%" OR  ##ramipril
bnf_code LIKE "0212000B0%" OR ##atrovastatin
bnf_code LIKE "0212000Y0%" OR ##simvastatin
bnf_code LIKE "0602010V0%" OR ##levothyroxine
bnf_code LIKE "0206020A0%" OR ##amlodipine
bnf_code LIKE "0204000H0%" OR ## Bisoprolol Fumarate
bnf_code LIKE "0209000A0%" OR ## Aspirin
bnf_code LIKE "0403030Q0%" OR ## Sertraline Hydrochloride
bnf_code LIKE "0403030D0%" OR ## Citalopram Hydrobromide
bnf_code LIKE "0205052N0%" OR ## Losartan Potassium
bnf_code LIKE "0202010B0%" OR ## Bendroflumethiazide
bnf_code LIKE "0205051L0%" OR ## Lisinopril
bnf_code LIKE "0205040D0%" OR ## Doxazosin Mesilate
bnf_code LIKE "0403030E0%" OR ## Fluoxetine Hydrochloride
bnf_code LIKE "0209000C0%" OR ## Clopidogrel
bnf_code LIKE "0205052C0%" OR ## Candesartan Cilexetil
bnf_code LIKE "0202010P0%" OR ## Indapamide
bnf_code LIKE "0205051M0%") ## Perindopril Erbumine
AND
(bnf_name LIKE '%_Tab%' or bnf_name LIKE '%_Cap%') ##this restricts to tablets or capsules
AND (month >= '2018-12-01'
    AND month <= '2019-11-01')
AND
ccgs.org_type='CCG'
GROUP BY
  pct,
  items,
  quantity_per_item
    '''

df_ltc = bq.cached_read(sql, csv_path='ltc_qty.csv')
df_ltc.head(10)
# -

df_rx_repeat = df_ltc.groupby(['quantity_per_item'])['items'].sum().reset_index()
df_rx_repeat["total_quantity"] = df_rx_repeat["quantity_per_item"]*df_rx_repeat["items"] 
df_rx_repeat.tail(5)

df_rx_repeat.describe()

# There is a maximum of 9060 on a single...... That well over 20 years worth of tablets, lets investigate further below.

####  ZOOM IN BELOW
fig = px.bar(df_rx_repeat, x='quantity_per_item', y='items')
fig.show()

# # ^^^^ ZOOM IN 

###here we make a list of durations we want to affect for later filtering
lst = [7,28,56,84] ##a week, a month, two months, three months

# +
df_common = df_rx_repeat.loc[(df_rx_repeat["quantity_per_item"].isin(lst))]

print(df_common)                                                             
# -

total = df_common["total_quantity"].sum()
df_common["proportion_of_qty"] = df_common["total_quantity"]/total*100
df_common

fig = px.bar(df_common, x='quantity_per_item', y='total_quantity')
fig.update_layout(
    title="Number of Tabets/Capsules for Commonly Prescribed Quantities for Commonly Prescribed Medicines")
fig.show()

# Most tablets/capsules for common LTC medicines are being dispensed on 28 day prescriptions (59%) with approximately 33% being dispensed on two monthly scripts. Only 4.5% of these common medicines are being supplied on three onthly prescriptions. 
#
# The Bristol paper assertion that most prescribing is 28 days is correct based on our basket of common LTC medicines. They recommend three month presctiptions as being more cost effective. Now lets look at script volume to see what the workload implications might be for our basket of common medicines.

fig = px.bar(df_common, x='quantity_per_item', y='items')
fig.update_layout(
    title="Number of Items for Commonly Prescribed Quantities for Commonly Prescribed Medicines")
fig.show()

# There are 16.2million one month scripts for our basket of common medicines. There will be substantial number of prescriptions that need amending.

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
        title= ("Proportion of Tabets/Capsules supplied on" ,quantity_per_item, "days  prescription for Commonly Prescribed Medicines"),
        column='proportion_of_basket', 
        separate_london=False,
        plot_options={'vmax': 100}
    )
    plt.show()

# My impression is that the 28 day supply map looks similar to SystmOne v EMIS Web [map of deployment](https://github.com/ebmdatalab/jupyter-notebooks/blob/master/General%20Practice%20EHR%20Deployment/EHR%20Deployment.ipynb)

#  code review improvements - what I would like to tweak
# - Cartogram Map titles, they do not look right but it fails when I try tweaking. How do you combine the changing column title and a nonchangeable string?
#

# + collapsed=true jupyter={"outputs_hidden": true}

