import numpy as np
import os
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import sys


year_month = sys.argv[1]
print(year_month)

bandopt = sys.argv[2]

# Folders where data are located and for output
data_folder = '/mnt/data/co-develop/data/satel/'
save_folder = '/mnt/data/co-develop/downsample_data/satel/'

X_grid_satel = np.load(data_folder + 'X_grid_satel.npy')
Y_grid_satel = np.load(data_folder + 'Y_grid_satel.npy')

print(X_grid_satel.shape)


data_satel = np.load(data_folder + year_month + 'bandopt0' + bandopt + 'Nx1202Ny1751.npy')

print(data_satel.shape)


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


X_satel_subset = X_grid_satel[550:725,575:775]
Y_satel_subset = Y_grid_satel[550:725,575:775]

lon_lat = np.transpose(np.stack([np.matrix.flatten(X_satel_subset),np.matrix.flatten(Y_satel_subset)]))

##### Code segment is to plot individual sub-sets for visualization

#data_satel_subset = data_satel[0,0,550:725,575:775]

#interpolated_values = griddata(lon_lat, np.matrix.flatten(data_satel_subset), (X_grid_subset_satel, Y_grid_subset_satel), method='linear')
#plt.contourf(X_grid_subset_satel,Y_grid_subset_satel,interpolated_values, 101)
#plt.colorbar()

#####




n_satel = data_satel.shape[0]
print('Satel Dataset: ' + str(n_satel))

output = -555. * np.ones([data_satel.shape[0], data_satel.shape[1], 128, 128])

# n_singv = 8 per day * n_days
# n_radar = 12 per hour * 3 * 8 hours per day * n_days
#if (n_radar != n_singv*36):
#  print('Error in dataset size')

for j in range(data_satel.shape[1]):

  output_vec = []

  for i in range(n_satel):
  #print(i)


    data_satel_subset = data_satel[i,j,550:725,575:775]

    interpolated_values = griddata(lon_lat, np.matrix.flatten(data_satel_subset), (X_grid_subset_satel, Y_grid_subset_satel), method='linear')
    output_vec.append(interpolated_values)

  output_vec = np.array(output_vec)
  output[:,j,:,:] = output_vec


output_filename = save_folder + 'satel_array_' + year_month + 'bandopt0' + bandopt + '.npy'
np.save(output_filename, output)

