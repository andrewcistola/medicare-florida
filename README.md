# Project Luna
Community driven, value based primary care for Medicare beneficiaries in Gainesville, FL<br>
<br>
![https://i9.ytimg.com/vi/lje5HQw7pR4/mq1.jpg?sqp=CIj8uf4F&rs=AOn4CLB0eidJVvvtLcQMSRWCbq7IhzmaCQ](https://youtu.be/lje5HQw7pR4)<br>
<br>
## About this Repository
This repository contains data, visuals, and documents to evaluate Opportunities for a Community driven, value based primary care clinic for Medicare patients using Direct Contracting payment models. This could sound weird, but also on point (think of Luna Lovegood).  

![](_fig/ffs_map_al_visits.png)<br>
<br>
![](_fig/ffs_map_al_pop.png)<br>
<br>
![](_fig/adv_map_al_adv.png)<br>
<br>
![](_fig/ffs_map_fl_visits.png)

### Data Table
`ffs_al.csv` is a ready to use table with information related to the request. 

#### Variable Definitions
ZIP = 5 digit Zip code in Alachua County, FL<br>
POP_OVER_65 = Total population over 65 in Zip Code<br>
POP_TOTAL = Total population in Zip Code<br>
TOTAL_DAYS_OF_CARE = Total bed days from Medicare Part A/B beneficaries from all hopsitals for residents within that Zip Code<br>
TOTAL_CHARGES = Total raw charges from Medicare Part A/B beneficaries from all hopsitals for residents within that Zip Code<br>
TOTAL_CASES = Total hospital visits from Medicare Part A/B beneficaries from all hopsitals for residents within that Zip Code<br>
DAYS_per 65 = TOTAL_DAYS_OF_CARE / POP_OVER_65<br>
CHARGES_per 65 = TOTAL_CHARGES / POP_OVER_65<br>
VISTIS_per 65 = TOTAL_CASES/ POP_OVER_65<br>

#### Notes
- Population data was accessed from the 2018 American Community Survey. https://data.census.gov/cedsci/?g=0100000US&tid=ACSDP1Y2018.DP05<br>
- Hospitalization data was accessed from the 2020 CMS Hospital Compare, Health Services Area File. https://data.cms.gov/Medicare-Inpatient/Hospital-Service-Area-File-2018/sgw2-6vb4<br>
- The open source Healthy Neighborhoods Repository was used for this project. For Raw data files, documentation, and code visit https://github.com/andrewcistola/healthy-neighborhoods<br>

## Repository Contents:
`ffs_al.csv` Ready to use file<br>
`Income Statement.xlsx` Draft of income statement for possible clinic<br>
`_data` Data used for the request<br>
`_code` Code used for the request<br>
`_fig` Figures made in the request<br>
`LICENSE` Generic MIT licenses for open source projects from DrewC!<br>
`.gitattributes` File extensions marked for GH large file storage<br>
`environment.yml` Conda environment with dependencies for use in development projects<br>

## Repository Structure
The repository uses the following file organization.

### Subdirectories
`_v#.#` dependency files deployed for that specific release or version<br>
`_data` staged data files related to the project<br>
`_fig` graphs, images, and maps related to the project<br>
`_archive` old files no longer used<br>
`_raw` raw data files, documentation, and code used for staging data<br>
`project` Files related to specifc project<br>
`README` Description, directory, notes

### File Naming:
`topic_prefix_suffix.ext`

### Topics:
Topics are assigned based on content and listed in the directory README

### Prefixes:
`alpha_` First draft of script, continuting with greek alphabet
`omega_` Final draft of script
`
### Suffixes:
`_code` Development code script for working in an IDE<br>
`_book` Jupyter notebook <br>
`_stage` Data files that have been modified from raw source<br>
`_2020-01-01` Text scripts with results output with date it was run<br>
`_map` 2D geographic display<br>
`_graph` 2D chart or graph representing numeric data

## Style:
Code scripts use the following style:

### PEP-8
Whenever possible code scripts follow PEP-8 standards. 

### Elective options:
Python and R code scripts use the following elective options:<br>
`=` for variable defintions (no `<-`)<br>
`''` for all character strings or arguments (no `""`) <br>
A single space is provided between each element ex. `columns = 'COlA'`<br>

### Naming Conventions:
Python and R code scripts use the following variable naming conventions:<br>
<br>
data frames: `df_xx`<br>
list: `l_xx`<br>
arrays: `a_xx`<br>
feature tables: `df_X`<br>
target tables: `df_Y`<br>

## Disclaimer
While the author (Andrew Cistola) is a Florida DOH employee and a University of Florida PhD student, these are NOT official publications by the Florida DOH, the University of Florida, or any other agency. 
No information is included in this repository that is not available to any member of the public. 
All information in this repository is available for public review and dissemination but is not to be used for making medical decisions. 
All code and data inside this repository is available for open source use per the terms of the included license. 

### allocativ
This repository is part of the larger allocativ project dedicated to prodiving analytical tools that are 'open source for public health.' Learn more at https://allocativ.com. 
