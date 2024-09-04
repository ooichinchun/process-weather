import numpy as np
import os
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import sys


year_month = sys.argv[1]
print(year_month)

# Folders where data are located and for output
data_folder = '/mnt/data/co-develop/data/radar_TS/'
radar_grid_folder = '/mnt/data/co-develop/data/radar/'

save_folder = '/mnt/data/co-develop/downsample_data/radar_ts/'

X_grid_radar = np.load(radar_grid_folder + 'X_interp_grid.npy')
Y_grid_radar = np.load(radar_grid_folder + 'Y_interp_grid.npy')

print(X_grid_radar.shape)

data_radar = np.load(data_folder + year_month + 'Nx0401Ny0401.npy')
print(data_radar.shape)


#### Define regular grid centered on Radar (x,y)
#### Center of Radar grid at 1.35, 103.97
#x_grid = np.linspace(103.34, 104.61, 128)     # Regular grid for x-coordinate
#y_grid = np.linspace(0.72, 1.99, 128)     # Regular grid for y-coordinate
#X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates

# Hand-tuned indices subset the above grid centered on radar (x,y) for 128 x 128 grid
X_grid_subset = X_grid_radar[132:(132+128),134:(134+128)]
Y_grid_subset = Y_grid_radar[132:(132+128),134:(134+128)]

print(X_grid_subset.shape)
#print(Y_grid_subset[:,0])


##### Code segment is to plot individual sub-sets for visualization

#data_singv_subset = data_singv[0,5,1,450:(450+150),600:(600+150)]
#print(data_singv_subset.shape)

#interpolated_values = griddata(lon_lat, np.matrix.flatten(data_singv_subset), (X_grid_subset, Y_grid_subset), method='linear')
#plt.contourf(X_grid_subset,Y_grid_subset,interpolated_values)
#plt.contourf(X_grid_singv[450:(450+150),600:(600+150)],Y_grid_singv[450:(450+150),600:(600+150)],data_singv[0,5,1,450:(450+150),600:(600+150)])

#####


n_radar = data_radar.shape[0]
print('Radar Dataset: ' + str(n_radar))


# n_radar = 12 per hour * 3 * 8 hours per day * n_days
#if (n_radar != n_singv*36):
#  print('Error in dataset size')

output_vec = data_radar[:,132:(132+128),134:(134+128)]

output_filename = save_folder + 'radarTS_array_' + year_month + '.npy'
np.save(output_filename, output_vec)

