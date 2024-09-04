import numpy as np
import os
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import sys


year_month = sys.argv[1]
print(year_month)

# Folders where data are located and for output
data_folder = '/mnt/data/co-develop/data/sat_TS/'
save_folder = '/mnt/data/co-develop/downsample_data/sat_ts/'

X_grid_sat_ts = np.load(data_folder + 'X_grid_SatTS.npy')
Y_grid_sat_ts = np.load(data_folder + 'Y_grid_SatTS.npy')

print(X_grid_sat_ts.shape)

data_sat_ts = np.load(data_folder + year_month + 'Nx0482Ny0702.npy')
print(data_sat_ts.shape)


#### Define regular grid centered on Radar (x,y)
#### Center of Radar grid at 1.35, 103.97
#### First set are for 0.01 degree resolution to match radar
#x_grid = np.linspace(103.34, 104.61, 128)     # Regular grid for x-coordinate
#y_grid = np.linspace(0.72, 1.99, 128)     # Regular grid for y-coordinate
#X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates

# Define regular grid for Satellite and SatTS
x_grid = np.linspace(102.71, 105.25, 128)     # Regular grid for x-coordinate
y_grid = np.linspace(0.09, 2.63, 128)     # Regular grid for y-coordinate
X_grid_subset_satel, Y_grid_subset_satel = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates


X_sat_ts_subset = X_grid_sat_ts[200:275,225:300]
Y_sat_ts_subset = Y_grid_sat_ts[200:275,225:300]

lon_lat = np.transpose(np.stack([np.matrix.flatten(X_sat_ts_subset),np.matrix.flatten(Y_sat_ts_subset)]))



##### Code segment is to plot individual sub-sets for visualization

#data_sat_ts_subset = data_sat_ts[0,200:275,225:300]

#interpolated_values = griddata(lon_lat, np.matrix.flatten(data_sat_ts_subset), (X_grid_subset_satel, Y_grid_subset_satel), method='nearest')
#plt.contourf(X_grid_subset_satel,Y_grid_subset_satel,interpolated_values, 101)
#plt.colorbar()

#####


n_satTS = data_sat_ts.shape[0]
print('SatTS Dataset: ' + str(n_satTS))


output_vec = []

for i in range(n_satTS):


  data_sat_ts_subset = data_sat_ts[i,200:275,225:300]
  interpolated_values = griddata(lon_lat, np.matrix.flatten(data_sat_ts_subset), (X_grid_subset_satel, Y_grid_subset_satel), method='nearest')
  output_vec.append(interpolated_values)


output_vec = np.array(output_vec)

output_filename = save_folder + 'satTS_array_' + year_month + '.npy'
np.save(output_filename, output_vec)

