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

# ##### <center>This notebook is a work in progress to demonstrate how a traditional academic paper could look with execuatbale code presented alongside. Numbers and discussions presented are still at an early draft phase<center> #####

# <h1><center>Variation in repeat prescription duration for long term conditions: a xxxx study in English NHS primary care.</center></h1>
# <h2><center>Authors, Authors*</center></h2>
#
#
# <centre>The DataLab, Nuffield Department of Primary Care Health Sciences, University of Oxford, UK, OX2 6GG<centre>
#
# *Corresponding: ben.goldacre@phc.ox.ac.uk
#

# # Introduction

# In England, 14.2 million people are estimated to have at least two long-term conditions (LTCs),[1] many of whom will routinely receive a prescription medicine to treat or relieve their condition. GP practices in England issue 1.1 billion prescriptions every year,[2] two thirds of which are estimated to be repeat prescriptions, commonly for LTCs.[3] The economic burden involved in the issuing of prescriptions, including the time of doctors and other practice staff, dispensing by pharmacies, and collection by patients, may be affected by the duration for which each prescription is given.
# <br>
# <br>
# The NHS does not issue national guidance on the duration of prescriptions and doctors are recommended to select a “clinically appropriate” duration.[4] Local guidance may recommend one-month prescriptions, to minimise wastage from unused medications. However, researchers in the University of Bristol have recommended that NHS England, the national body responsible for all NHS care and organisations, should recommend three-monthly prescriptions for LTCs rather than shorter durations.[5] Longer duration prescriptions are likely to increase adherence with medication, reduce inconvenience for patients, and save costs in terms of staff time, which is likely to offset any increased waste from unused medications.[6–9] 
# <br><br>
# Our [OpenPrescribing.net](https://openprescribing.net/) service is a publicly funded and openly accessible explorer for NHS primary care prescribing data, launched in 2015, with 135,000 unique users in the past year including doctors, pharmacists and patients. It supports complex bespoke data queries on all English GP prescriptions dispensed in primary care, and displays numerous predefined standard measures for safety, cost, and effectiveness for every practice in England. We propose a measure to display prescription duration for a subset of products across the complete population of GP prescriptions.[10] 
# <br><br>
# We therefore set out to: describe the current repeat prescription durations for long term conditions, describe variation between CCGs, investigate factors associated with repeat prescribing duration and provide a conservative estimate of the economic impact of any policy changes with regards to repeat prescription duration in England.
#

# # Methods
#
# #### _Study Design_
# We analysed prescribing practice by conducting a retrospective cohort study in prescribing
# data from all English NHS general practices and CCG, complemented with data on EHR deployment from NHS Digital; user-testing of two commonly used EHRs by a senior pharmacist and estimation of economic impacts resulting from a change in practice.
#
# #### _Software and Reproducibility_
# This paper is a novel interactive paper presented alongside executable code. Methods are described in text alongside execuatable code. Data, as well as all code for data management and analysis is also archived in GitHub.[17] Data management is performed using Python and Google BigQuery, with analysis carried out using Stata 13.2 / Python. The following cell details the Python libraries used in addition to the [core environment template](https://github.com/ebmdatalab/datalab-notebook-template) deveopled by The DataLab and further information on requirments and dependencies can be obtained in `requirements.in`. 
#
#

import pandas as pd
import numpy as np
import plotly.express as px
from ebmdatalab import bq, maps, charts
import matplotlib.pyplot as plt
import os
import warnings; warnings.simplefilter('ignore') ##this is for readability due to a few deprecation warnings - we will fix this and use recommended updated methods

# #### _Data Sources_
# We extracted data from the OpenPrescribing.net database. This imports openly accessible prescribing data from the large monthly files published by the NHS Business Services Authority which contain data on cost and items prescribed for each month, for every typical general practice and CCG in England since mid-2010.[11]The monthly prescribing datasets contain one row for each different medication and dose, in each prescribing organisation in NHS primary care in England, describing the number of items (i.e. prescriptions issued) and the total cost. These data are sourced from community pharmacy claims data and therefore contain all items that were dispensed. We extracted all available data for standard general practices, excluding other organisations such as prisons and hospitals, according to the NHS Digital dataset of practice characteristics and excluded practices that had not prescribed at least one item per measure. We excluded all other organisations such as prisons and hospitals. We restricted our analysis to a basket of medicines which are commonly prescribed for long term conditions and nearly exclusively used once a day using a prior method for measures of seven days prescribing on OpenPrescribing. It does not include dosage instructions e.g. take two tablets twice a day.[10] Briefly the most commonly prescribed tablets/capsules by chemical substance and sorted by highest volume. Two senior pharmacists reviewed the list and identified the medicines which are nearly exclusively prescribed once daily in their experience to create the basket and it includes the chemicals  atorvastatin, simvastatin, levothyroxine, amlodipine and ramipril. Data on EHRs and in which general practice they are deployed was extracted from a monthly file that is circulated by NHS Digital to interested parties and available on request.[12] 
#

#the sql query to generate this data can be read in <filename>
df_ltc = pd.read_csv(os.path.join('..','data','ltc_qty.csv'))


df_ltc.sum()

# _Repeat prescribing durations_
#
# We measured the quantity of tablets or capsules issued for medicines within our definition and plotted them on a histogram ([jump to](#histogram1)). We identified prescriptions likely to have been issued for one month (28 tablets/capsules), two months  (56 tablets/capsules) or three months  (84 tablets/capsules)  ([jump to](#commonqty)).
#

df_rx_repeat = df_ltc.copy()
df_rx_repeat["total_quantity"] = df_rx_repeat["quantity_per_item"]*df_rx_repeat["items"] 


###here we make a list of common durations e.g. week, month, two months, three months 
lst = [7,28,56,84]

##create a dataframe with common quantities
df_common = df_rx_repeat.loc[(df_rx_repeat["quantity_per_item"].isin(lst))]
df_common_national = df_common.groupby(["quantity_per_item"])['items','total_quantity'].sum().reset_index()

national_qty_total = df_rx_repeat["total_quantity"].sum()
df_common_national = df_common.groupby(["quantity_per_item"])['items','total_quantity'].sum().reset_index()
df_common_national["proportion_of_total_qty"] = df_common_national["total_quantity"]/national_qty_total*100

# _Geographical variation at CCG level across England_
#
# We created choropleth maps of the proportion of prescriptions that are likely to have been issued for one month (28 tablets/capsules), two months  (56 tablets/capsules) or three months  (84 tablets/capsules) for each CCG in England between August 2018 and July 2019. ([jump to](#ccgmap)) 
#

df_ccg = df_ltc.groupby(['pct','quantity_per_item'])['items'].sum().reset_index()
df_ccg["total_quantity"] = df_ccg["quantity_per_item"]*df_ccg["items"] #create a ccg dataframe
df_common_ccg = df_ccg.loc[(df_ccg["quantity_per_item"].isin(lst))] # create a CCG dataframe with common qty

ccg_total = df_common_ccg.groupby(["pct"]).sum().reset_index()
ccg_total=ccg_total.rename(columns = {'total_quantity':'basket_qty'}).drop(columns =['quantity_per_item', 'items']) ##we don't need two columns


ccg_map =  pd.merge(df_common_ccg,ccg_total, on="pct")  
ccg_map["proportion_of_basket"] = ccg_map["total_quantity"]/ccg_map["basket_qty"]*100
ccg_map

df_common_ccg.head()



df_common_ccg = df_ccg.loc[(df_ccg["quantity_per_item"].isin(lst))]

# _Factors associated with repeat prescribing durations_
#
# We examined factors associated prescribing one month durations versus longer durations of two or three months combined. We selected variables from data available on individual CCGs and practices from publicly available data that have previously been shown to be associated with variation in prescribing. These variables were: proportion of GP registered list who are over 65, the proportion of patients with a long term health condition[ref], if the practice was a dispensing practice and the primary electronic health record (EHR) used in the practice. We explored the influence of CCG membership on individual practices  by xyz.
#

# _EHR System User-Interface Evaluation_
#
# One senior pharmacist issued prescriptions in the EMIS and SystmOne computer systems to a test patient and observed the prompts. We also contacted the vendors of all four EHRs to enquire about their default options for course duration.
#

# _Patient and Public Involvement_ 
#
# Our website OpenPrescribing.net, is an openly accessible data explorer for all NHS England primary care prescribing data, which receives a large volume of user feedback from professionals, patients and the public. This feedback is used to refine and prioritise our informatics tools and research activities. Patients were not formally involved in developing this specific study design
#

# # Results
#
# In our study period 159,715,336 prescription items [code output 22] were issued for medicines commonly taken once daily for long-term conditions of which 156,349,790 (approx 98%) prescriptions [code output 24] were issued for durations suggestive of one month (45%) , two months (41%) or three months (7.5%) [Table 1](#table1). Quantities of tablets or capsules prescribed on a single prescription ranged from 1 tablets/capsules to 8400 ([figure 1](#histogram1)) whilst [figure 2](#histogram2) shows the overwhelming majority of prescriptions are issued for one or two months.  There is substanial geographic variation with an obvious geographic clustering (dn-need better word) from east to west with one and two month prescriptions ([figure 3](#ccgmap)).
#
#

df_ltc.sum()

# ### Table 1: _Total Volume of items and quantity for one week, one month, two months and three months_ <a id='table1'></a>

df_common_national

df_common.sum()

# #### Figure 1: _Histogram of all prescribed medicines quantity_ <a id='histogram1'></a>

# +
dfp = df_rx_repeat.copy()
dfp = dfp.groupby(["quantity_per_item"]).sum().reset_index()


fig = px.bar(dfp, x='quantity_per_item', y='items')
fig.update_layout(
    title=" Figure 1: Number of Tabets/Capsules for Commonly Prescribed Medicines")
fig.update_xaxes(range=[0, 120])
fig.show()
# -

# #### Figure 2: _Histogram of all prescribed medicines quantity_ <a id='histogram2'></a>

# +
dfp = df_common.copy()
dfp = dfp.groupby(["quantity_per_item"]).sum().reset_index()

fig = px.bar(dfp, x='quantity_per_item', y='total_quantity')
fig.update_layout(
    title="Number of Tabets/Capsules for Commonly Prescribed Quantities for Commonly Prescribed Medicines")
fig.show()

# get value for percentage dispensed in each of 1/2/3 months prescriptions: 
#percentage = {}
#for d in lst:
#    percentage[d] = dfp.loc[dfp["quantity_per_item"]==d,'proportion_of_total_qty'].item()

#print(f"Tablets/capsules for common LTC medicines are most commonly being dispensed on 28 day prescriptions ({percentage[28]:.1f}%)",
 #     f"with approximately {percentage[56]:.1f}% being dispensed on two-monthly scripts.",
  #    f"Only {percentage[84]:.1f}% of these common medicines are being supplied on three-monthly prescriptions." )
# -

# #### Geographical variation at CCG level across England <a id='ccgmap'></a>

for quantity_per_item in ccg_map.quantity_per_item.unique():
    plt.figure(figsize=(20, 7))
    maps.ccg_map(
        ccg_map[ccg_map['quantity_per_item'] == quantity_per_item], 
        title= (f"Proportion of Tabets/Capsules supplied on {quantity_per_item}-day \n prescriptions for small basket of Commonly Prescribed Medicines"),
        column='proportion_of_basket', 
        separate_london=False,
        plot_options={'vmax': 100}
    )
    plt.show()

# ##### Factors associated with repeat prescribing durations
# We found EHR sytem in use to be significantly associated with repeat prescribing duration. Listsize, number of patients >65 and deprivation were not show to be associated with durations. CCG membership showed a xx relationship (table 2). This section is made up so far as a placeholder - we need to add in stata code and actually check relationships!

# |             |                           | Log regression | 
# |-------------|---------------------------|----------------|
# | EHR         | emis |                |   |   |
# | Age         |                           |                |
# | Deprivation |                           |                |
# | CCG memebership |                           |                |
# QoF Score

# ##### EHR System User-Interface Evaluation
#
# We will insert written descriptions of observations plus responses of the EHR vendors once we have completed.

# # Discussion
#
# _Summary_
#
# Prescribers in primary care supply; 60.4% of prescriptions items (n = 16 212 361) in quantities suggestive of one month's supply; 34.5% of prescription items ( n = 4604721) as two months supply and 4.8% of prescription items (n = 423880) in quantities suggestive of three months supply. We found that dispensing doctor status and the EHR in use in a practice were the most likely predictors of prescription duration. We estimate the current overall economic impact of this to be £193.9million  and that the NHS could reduce the economic impact on patients, staff utilisation and wastage to the tune of £108.4 million by switching 90% of these one month supply to three monthly supplies.
#   
# _Strengths and weaknesses_
#
# Our prescribing data includes all prescribing in all typical practices in England, thus
# minimising the potential for obtaining a biased sample. We used prescribing data derived from pharmacy claims data used to calculate the transfer of funds from CCGs to dispensing pharmacies: all parties are motivated to ensure the accuracy of this data. We excluded a small number of settings such as walk-in centres, which typically do not issue repeat prescriptions for medicines. Pharmacy claims data does not currently include dosage instructions our durations is an estimate whilst only including the top fifty medicines means that our economic forecasting is likely to be an underrepresentation of the true cost. Estimates of staff mix, time to prescribe and patient impact are likely to vary between practices and region and in order to compensate for this our cost impact modelling allows readers to adjust variables to modify the estimate or calculate local values. 
#
# _Findings in Context_
#
# - Duration background from Bristol
# - Our previous work  the user interface of EHR
# - Disp doctor and CCG (all DataLab papers on trends and variation are relevant here)
#
# _Policy Implications and Interpretation_
#  - Savings (££ + patient & staff time + reduced environmental impact)
#  - Discuss COVID stock issues. Any changes to be managed in Stepwise approach in tandem with evaluation to ensure supply chain robustness
#  - EHR impact and possibility of using it for cluster RCT by changing defaults
#
# _Future Research_ 
# - any changes if decided upon need to be evaluated
# - possibility of using it for cluster RCT by changing defaults?
# - EHR design : oppurtunity for research
#
#
#

# +
# Summary & Conclusion
# -

# #### Acknowledgements
# XX.
#
# #### Conflicts of Interest
# All authors have completed the ICMJE uniform disclosure form at www.icmje.org/coi_disclosure.pdf and declare the following: BG has received research funding from the Laura and John Arnold Foundation, the Wellcome Trust, the Oxford Biomedical Research Centre, the NHS National Institute for Health Research School of Primary Care Research, the Mohn-Westlake Foundation, the Good Thinking Foundation, the Health Foundation, and the World Health Organisation; he also receives personal income from speaking and writing for lay audiences on the misuse of science. XX are employed on BG’s grants for XX. 
#
# #### Funding
# This work is supported by…
# ..The NIHR Biomedical Research Centre, Oxford
# ..A Health Foundation grant (Award Reference Number 7599); 
# ..A National Institute for Health Research (NIHR) School of Primary Care Research (SPCR) grant (Award Reference Number 327). 
# ..LJAF (Award Reference Number xxx).
# ..This research was supported by the National Institute for Health Research Applied Research Collaboration Oxford and Thames Valley. The views expressed in this publication are those of the author(s) and not necessarily those of the NIHR or the Department of Health and Social Care.
# ...Funders had no role in the study design, collection, analysis, and interpretation of data; in the writing of the report; and in the decision to submit the article for publication.
#
#
# #### Ethical approval
# ..This study uses exclusively open, publicly available data, therefore no ethical approval was required.
# ..Study ethics
#
# #### Guarantor
# BG is guarantor.
#
# #### Contributorship
# XX XX conceived the study. XX XX designed the methods. XX XX collected and analysed the data with methodological and interpretation input from XX XX. XX drafted the manuscript. All authors contributed to and approved the final manuscript. XX was lead engineer on the associated website resource with input from XX XX. BG supervised the project and is guarantor.
#

# # References
#
# 1 	Stafford M, Steventon A, Thorlby R, et al. Understanding the health care needs of people with multiple health conditions. 2018.
#
# 2 	Prescription Cost Analysis - England, 2018 [PAS] - NHS Digital. NHS Digital. https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis/2018 (accessed 8 Apr 2019).
# 3 	GUIDANCE FOR THE IMPLEMENTATION OF REPEAT DISPENSING. NHS Employers. 2013.https://www.nhsemployers.org/~/media/Employers/Publications/repeat-dispensing-guide.pdf (accessed 8 Jan 2019).
#
# 4 	Prescribing in general practice | The BMA. 2018.https://www.bma.org.uk/advice/employment/gp-practices/service-provision/prescribing/prescribing-in-general-practice (accessed 8 Jan 2020).
#
# 5 	University of Bristol. Increasing the duration of repeat prescriptions may save NHS money and improve care | PolicyBristol | University of Bristol. https://www.bristol.ac.uk/policybristol/policy-briefings/repeat-prescription-costs/ (accessed 8 Jan 2020).
#
# 6 	King S, Miani C, Exley J, et al. Impact of issuing longer- versus shorter-duration prescriptions: a systematic review. Br J Gen Pract 2018;68:e286–92. doi:10.3399/bjgp18X695501
#
# 7 	Martin A, Payne R, Wilson EC. Long-Term Costs and Health Consequences of Issuing Shorter Duration Prescriptions for Patients with Chronic Health Conditions in the English NHS. Appl Health Econ Health Policy 2018;16:317–30. doi:10.1007/s40258-018-0383-9
#
# 8 	Miani C, Martin A, Exley J, et al. Clinical effectiveness and cost-effectiveness of issuing longer versus shorter duration (3-month vs. 28-day) prescriptions in patients with chronic conditions: systematic review and economic modelling. Health Technol Assess  2017;21.https://ora.ox.ac.uk/objects/uuid:58356d06-a69c-4502-ba3e-c17fcfa57c8b
#
# 9 	Doble B, Payne R, Harshfield A, et al. Retrospective, multicohort analysis of the Clinical Practice Research Datalink (CPRD) to determine differences in the cost of medication wastage, dispensing fees and prescriber time of issuing either short (< 60 days) or long (≥ 60 days) prescription lengths in primary care for common, chronic conditions in the UK. BMJ Open 2017;7:e019382.https://bmjopen.bmj.com/content/7/12/e019382?utm_source=TrendMD&utm_medium=cpc&utm_campaign=BMJOp_TrendMD-0
#
# 10 	MacKenna B. New Measure: Seven Day Prescribing for Long-term Conditions. EBM DataLab. 2019.https://ebmdatalab.net/new-measure-seven-day-prescribing-for-long-term-conditions/ (accessed 8 Jan 2020).
# 11 	NHS Business Services Authority. Information Services Portal (ISP). https://www.nhsbsa.nhs.uk/information-services-portal-isp (accessed 11 Oct 2018).
#
# 12 	Freedom of information request NIC-142425-M5S5D - NHS Digital. NHS Digital. https://digital.nhs.uk/about-nhs-digital/contact-us/freedom-of-information/freedom-of-information-disclosure-log/freedom-of-information-disclosure-log-october-2017/freedom-of-information-request-nic-142425-m5s5d (accessed 8 Apr 2019).
#
# 13 	PSNC. Fees and allowances. PSNC Main site. https://psnc.org.uk/dispensing-supply/endorsement/fees-allowances/ (accessed 2 Mar 2020).
#
# 14 	Curtis L, Burns A. Unit Costs of Health and Social Care 2019. PSSRU 2020. https://web.archive.org/web/20200210164225/https://www.pssru.ac.uk/project-pages/unit-costs/unit-costs-2019/ (accessed 10 Feb 2020).
#
# 15 	Provision of market research for value of travel time savings and reliability:Non-Technical Summary Report. Department for Transport. 2015.https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/470229/vtts-phase-2-report-non-technical-summary-issue-august-2015.pdf
#
# 16 	Parkin E, Bate A, Loft P. NHS charges. Published Online First: 2020.https://researchbriefings.parliament.uk/ResearchBriefing/Summary/CBP-7227 (accessed 18 Feb 2020).
#
# 17 	The DataLab. GitHub Repo: Rx Quantity for Long Term Conditions. Github https://github.com/ebmdatalab/Rx-Quantity-for-Long-Term-Conditions (accessed 8 Jan 2020).
#
# 18 	MacKenna B, Curtis HJ, Walker AJ, et al. Trends and variation in unsafe prescribing of methotrexate: a cohort study in English NHS primary care. Health Systems and Quality Improvement. 2019. doi:10.1101/19000919
#
# 19 	MacKenna B. Ghost branded generics: Why does the cost of generic atorvastatin vary? EBM DataLab. 2018.https://ebmdatalab.net/ghost-branded-generics-why-does-the-cost-of-generic-atorvastatin-vary%ef%bb%bf/ (accessed 8 Apr 2019).
#
# 20 	Impact Of Electronic Health Record Interface Design On Unsafe Prescribing Of Ciclosporin, Tacrolimus and Diltiazem: A Cohort Study In English NHS Primary Care. JMIR Preprints. https://preprints.jmir.org/preprint/17003 (accessed 28 Nov 2019).
#
# 21 	Montoy JCC, Coralic Z, Herring AA, et al. Association of Default Electronic Medical Record Settings With Health Care Professional Patterns of Opioid Prescribing in Emergency Departments: A Randomized Quality Improvement Study. JAMA Intern Med Published Online First: 2020.https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/2759133
#
#


