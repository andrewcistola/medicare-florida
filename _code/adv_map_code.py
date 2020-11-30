# Information
name = 'adv_map' # Inptu file name with topic, subtopic, and type
path = 'other/chacko_18-11-2020/' # Input relative path to file 
directory = '/home/drewc/GitHub/' # Input working directory
title = 'Medicare Advantage by Zip Code in Alachua County Florida' # Input descriptive title
author = 'Andrew S. Cistola, MPH' # Input Author

## Create Map from Zip Code Data

### Import python libraries
import os # Operating system navigation
from datetime import datetime
from datetime import date

### Import data science libraries
import pandas as pd # Widely used data manipulation library with R/Excel like tables named 'data frames'
import numpy as np # Widely used matrix library for numerical processes

### Import Visualization Libraries
import matplotlib.pyplot as plt # Comprehensive graphing package in python
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import geopandas as gp # Simple mapping library for csv shape files with pandas like syntax for creating plots using matplotlib 
import descartes # Mapping library for use with geopandas
import mapclassify # Mapping library for use with geopandas
import contextily as ctx # Open street maps for overlay with geopandas

### Set Directory
os.chdir(directory) # Set wd to project repository

### Set Timestamps
day = str(date.today())
stamp = str(datetime.now())### Create Folium Map

### Add census tract layer

### Preprocess First Dataset
df_d3 = pd.read_csv('other/chacko_18-11-2020/_data/ffs_2018_ZCTA_stage.csv') # Import first dataset saved as csv in _data folder
df_d1 = df_d1.filter(['POP_OVER_65', 'VISITS_per65', 'ZCTA']) # Drop or filter columns to keep only feature values and idenitifer
df_d1 = df_d1.rename(columns = {'ZCTA': 'ID', 'VISITS_per65': 'quant', 'POP_OVER_65': 'pop'}) # Apply standard name to identifier and quantitative outcome
df_d1.info() # Get class, memory, and column info: names, data types, obs


### Add Zip Code layer
