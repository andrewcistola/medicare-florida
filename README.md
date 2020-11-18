# Development Repository for Andrew S Cistola, MPH (DrewC!)
A repository containing projects under development.

## About this Repository
This a private repository containing subrepos for current projects under development as well as templates for easy transfer to new repositories.

## Repository Contents:
`_archive` Old files from previous projects
`toolbox` Collected code, installers, or templates
`allocativ` Development projects for Fractureproof, Healthy Neighborhoods Project, and Python for Healthcare
`neville` Research for PhD dissertation
`.vscode` Settings used for VS Code IDE
`LICENSE` Generic MIT licenses for open source projects from DrewC!
`.gitattributes` File extensions marked for GH large file storage
`environment.yml` Conda environment with dependencies for use in development projects

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
