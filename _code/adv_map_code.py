# Information
name = 'adv_map' # Inptu file name with topic, subtopic, and type
path = '_request/chacko_18-11-2020/' # Input relative path to file 
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
import folium # Mapping library with dynamic 
import json # library for importing and manipuation json files


### Set Directory
os.chdir(directory) # Set wd to project repository

### Set Timestamps
day = str(date.today())
stamp = str(datetime.now())### Create Folium Map

### Preprocess First Dataset
df_d1 = pd.read_csv('_request/chacko_18-11-2020/_data/raw/ACSDT5Y2018.B27010_2020-11-30T113447/ACSDT5Y2018.B27010_data_with_overlays_2020-11-30T113430.csv') # Import first dataset saved as csv in _data folder
df_d1 = df_d1.drop(df_d1.index[0]) # Drop first row of dataframe
df_d1 = df_d1.drop(columns = ["NAME"]) # Drop Unwanted Columns
df_d1["B27010_065E"] = df_d1["B27010_065E"].astype("int64") # Change data type of column in data frame
df_d1["B27010_051E"] = df_d1["B27010_051E"].astype("int64") # Change data type of column in data frame
df_d1["ADV_per65"] = df_d1["B27010_065E"] / df_d1["B27010_051E"]
df_d1 = df_d1.filter(['GEO_ID', 'ADV_per65']) # Drop or filter columns to keep only feature values and idenitifer
df_d1.info() # Get class, memory, and column info: names, data types, obs

### Join to Polygon
gdf_d1 = gp.read_file('_request/chacko_18-11-2020/_data/shape/ZCTA/cb_2018_us_zcta510_500k/cb_2018_us_zcta510_500k.shp') # Import shape files from folder with all other files downloaded
gdf_d1 = gdf_d1.rename(columns = {'AFFGEOID10': 'GEO_ID'}) # Apply standard name to identifier and quantitative outcome
gdf_d1 = gdf_d1.filter(['GEO_ID', 'geometry']) # Drop or filter columns to keep only feature values and idenitifer
gdf_d1 = pd.merge(gdf_d1, df_d1, on = 'GEO_ID', how = 'inner') # Geojoins can use pandas merge as long as geo data is first passed in function
gdf_d1.info() # Get class, memory, and column info: names, data types, obs

### Create choropleth for AL FL
map = gdf_d1.plot(column = 'ADV_per65', cmap = 'Blues', edgecolor = 'black', alpha = 0.7, figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Beneficiaries per Pop over 65', 'loc': 'upper right', 'fontsize': '6'})
map.set_title('Medicare Advantage Estimates 2015-2018 by Zip Code in Florida', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.15, 0.1), xytext = (0.15, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.16, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.2, 0.03), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.2, 0.0), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 0.1, '10 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_al_adv.png', dpi = 1000, bbox_inches = 'tight')




js_d1 = gdf_d1.to_crs(epsg=4326).to_json()
map_fl = folium.Map(location = [29.6516, -82.3248], tiles = 'OpenStreetMap', zoom_start = 11) # Florida Open Street map
map_fl.choropleth(geo_data = js_d1, data = df_d1, columns = ["B27010_051E", "B27010_064E", "B27010_065E"], key_on = "feature.geoid", fill_color = "Blues", fill_opacity = 0.7, legend_name = "2018 Estimate") # Folium choropleth map
folium.features.GeoJson(js_d1).add_to(map_fl) # Isolate features from geographic json file and save as data frame
map_fl.save('_request/chacko_18-11-2020/_fig/adv_map.html') # Save map as html file