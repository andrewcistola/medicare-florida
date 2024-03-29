# Information
name = 'ffs_map' # Inptu file name with topic, subtopic, and type
path = 'other/chacko_18-11-2020/' # Input relative path to file 
directory = '/home/drewc/GitHub/' # Input working directory
title = 'Medicare FFS by Zip Code in Alachua County Florida' # Input descriptive title
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
stamp = str(datetime.now())

### Preprocess First Dataset
df_d1 = pd.read_csv('other/chacko_18-11-2020/_data/ffs_2018_ZCTA_stage.csv') # Import first dataset saved as csv in _data folder
df_d1 = df_d1.filter(['POP_OVER_65', 'VISITS_per65', 'ZCTA']) # Drop or filter columns to keep only feature values and idenitifer
df_d1 = df_d1.rename(columns = {'ZCTA': 'ID', 'VISITS_per65': 'quant', 'POP_OVER_65': 'pop'}) # Apply standard name to identifier and quantitative outcome
df_d1.info() # Get class, memory, and column info: names, data types, obs

### Geojoin outcome table with polygons
gdf_d1 = gp.read_file('other/chacko_18-11-2020/_data/shape/ZCTA/cb_2018_us_zcta510_500k/cb_2018_us_zcta510_500k.shp') # Import shape files from folder with all other files downloaded
gdf_d1 = gdf_d1.to_crs(epsg = 3857) # Reproject to mercateur
gdf_d1['ID'] = gdf_d1['ZCTA5CE10'].astype('str') # Change data type of column in data frame
gdf_d1['ID'] = gdf_d1['ID'].str.rjust(5, '0') # add leading zeros of character column using rjust() function
gdf_d1['ID'] = 'ZCTA' + gdf_d1['ID'] # Combine string with column
gdf_d1 = gdf_d1.filter(['ID', 'geometry']) # Keep only selected columns
gdf_d1 = pd.merge(gdf_d1, df_d1, on = 'ID', how = 'inner') # Geojoins can use pandas merge as long as geo data is first passed in function
gdf_d1 = gdf_d1.filter(['quant', 'geometry', 'pop', 'ID']) # Keep only selected columns
gdf_d1.info() # Get class, memory, and column info: names, data types, obs

### Filter by Florida and join
df_sub = pd.read_csv('other/chacko_18-11-2020/_data/labels/crosswalk.csv') # Import shape files from folder with all other files downloaded
df_fl = df_sub[df_sub["ST"] == "FL"] # Subset by Florida 
df_fl = df_fl.filter(['ZCTA']) # Keep only selected columns
df_fl = df_fl.rename(columns = {'ZCTA': 'ID'}) # Apply standard name to identifier and quantitative outcome
gdf_fl = pd.merge(gdf_d1, df_fl, on = 'ID', how = 'inner') # Geojoins can use pandas merge as long as geo data is first passed in function
gdf_fl = gdf_fl.filter(['quant', 'geometry', 'pop', 'ID']) # Keep only selected columns
gdf_fl.info() # Get class, memory, and column info: names, data types, obs

### Filter by Alachua County Florida and join
df_sub = pd.read_csv('other/chacko_18-11-2020/_data/labels/crosswalk.csv') # Import shape files from folder with all other files downloaded
df_sub = df_sub[df_sub["ST"] == "FL"] # Subset by Florida 
df_al = df_sub[df_sub["NAME"] == "ALACHUA"] # Subset by Alachua County 
df_al = df_al.filter(['ZCTA', 'ZIP']) # Keep only selected columns
df_al = df_al.rename(columns = {'ZCTA': 'ID'}) # Apply standard name to identifier and quantitative outcome
gdf_al = pd.merge(gdf_d1, df_al, on = 'ID', how = 'inner') # Geojoins can use pandas merge as long as geo data is first passed in function
gdf_al = gdf_al.filter(['quant', 'geometry', 'pop', 'ID', 'ZIP']) # Keep only selected columns
gdf_al.info() # Get class, memory, and column info: names, data types, obs

### Create choropleth for FL
map = gdf_fl.plot(column = 'quant', cmap = 'YlGnBu', figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Visits per Pop over 65', 'loc': 'center left'})
map.set_title('Medicare FFS Hospital Visits 2015-2018 by Zip Code in Florida', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.0, 0.1), xytext = (0.00, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.01, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.05, 0.06), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.05, 0.01), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 20, '50 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_fl_visits.png', dpi = 1000, bbox_inches = 'tight')

### Create choropleth for FL with street overlay
map = gdf_fl.plot(column = 'quant', cmap = 'BuGn', edgecolor = 'black', linewidth = 1, alpha = 0.7, figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Visits per Pop over 65', 'loc': 'center left'})
ctx.add_basemap(ax = map, source = ctx.providers.Stamen.TonerLite)
map.set_title('Medicare FFS Hospital Visits 2015-2018 by Zip Code in Florida', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.15, 0.1), xytext = (0.15, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.16, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.2, 0.03), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.2, 0.0), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 20, '50 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_fl_street_visits.png', dpi = 1000, bbox_inches = 'tight')

### Create choropleth for AL FL with street overlay
map = gdf_al.plot(column = 'quant', cmap = 'Blues', edgecolor = 'black', alpha = 0.7, figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Visits per Pop over 65', 'loc': 'upper right', 'fontsize': '6'})
gdf_al.apply(lambda x: map.annotate(s = x.ZIP, xy = x.geometry.centroid.coords[0], ha = 'center'), axis=1);
ctx.add_basemap(ax = map, source = ctx.providers.Stamen.TonerLite)
map.set_title('Medicare FFS Hospital Visits 2015-2018 by Zip Code in Alachua County, FL', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.15, 0.1), xytext = (0.15, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.16, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.2, 0.03), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.2, 0.0), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 0.1, '10 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_al_visits.png', dpi = 1000, bbox_inches = 'tight')

### Create choropleth for AL with street overlay
map = gdf_al.plot(column = 'pop', cmap = 'Blues', edgecolor = 'black', linewidth = 1, figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Visits per Pop over 65', 'loc': 'upper right', 'fontsize': '6'})
gdf_al.apply(lambda x: map.annotate(s = x.ZIP, xy = x.geometry.centroid.coords[0], ha = 'center'), axis=1);
map.set_title('Population over 65 2015-2018 by Zip Code in Alachua County, FL', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.15, 0.1), xytext = (0.15, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.16, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.2, 0.03), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.2, 0.0), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 0.1, '10 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_al_pop.png', dpi = 1000, bbox_inches = 'tight')

### Export to CSV
df_ex = pd.read_csv('other/chacko_18-11-2020/_data/ffs_2018_ZCTA_stage.csv') # Import first dataset saved as csv in _data folder
df_sub_2 = pd.read_csv('other/chacko_18-11-2020/_data/labels/crosswalk.csv') # Import shape files from folder with all other files downloaded
df_sub_2 = df_sub_2[df_sub_2["ST"] == "FL"] # Subset by Florida 
df_al_2 = df_sub_2[df_sub_2["NAME"] == "ALACHUA"] # Subset by Alachua County 
df_al_2 = df_al_2.filter(['ZCTA', 'ZIP']) # Keep only selected columns
df_al_ex = pd.merge(df_ex, df_al_2, on = 'ZCTA', how = 'inner') # Geojoins can use pandas merge as long as geo data is first passed in function
df_al_ex = df_al_ex.drop(columns = ["ZCTA"]) # Drop Unwanted Columns
df_al_ex = df_al_ex.set_index("ZIP") # Set column as index
df_al_ex.to_csv(r'other/chacko_18-11-2020/_fig/ffs_al.csv') # Clean in excel and select variable
df_al_ex.info() # Get class, memory, and column info: names, data types, obs

### Create choropleth for FL with street overlay
map = gdf_fl.plot(column = 'quant', cmap = 'BuGn', edgecolor = 'black', linewidth = 1, alpha = 0.7, figsize = (10, 10), scheme = 'equal_interval', k = 9, legend = True, legend_kwds={'title': 'Visits per Pop over 65', 'loc': 'center left'})
ctx.add_basemap(ax = map, source = ctx.providers.Stamen.TonerLite)
map.set_title('Medicare FFS Hospital Visits 2015-2018 by Zip Code in Florida', fontdict = {'fontsize': 16}, loc = 'center')
map.set_axis_off()
map.annotate('', xy = (0.15, 0.1), xytext = (0.15, 0.0), arrowprops = dict(arrowstyle = 'simple'), fontsize = 10, xycoords= 'axes fraction')
map.annotate('N', xy = (0.16, 0.01), xycoords = 'axes fraction', fontsize = 16)
map.annotate('Andrew S. Cistola, MPH', xy = (0.2, 0.03), xycoords = 'axes fraction', fontsize = 10)
map.annotate(stamp, xy = (0.2, 0.0), xycoords = 'axes fraction', fontsize = 10)
map.add_artist(AnchoredSizeBar(map.transData, 20, '50 km', loc = 'lower right'))
plt.savefig(path + '_fig/' + name + '_fl_street_visits.png', dpi = 1000, bbox_inches = 'tight')






