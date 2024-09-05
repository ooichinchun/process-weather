import numpy as np
import os
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import sys


year_month = sys.argv[1]
print(year_month)

var_grp = sys.argv[2]


# Folders where data are located and for output
radar_grid_folder = '/mnt/data/co-develop/data/radar/'
singv_grid_folder = '/mnt/data/co-develop/data/singv/'
singv_data_folder = '/mnt/data/co-develop/data/singv/correct_spin3_full/'

save_folder = '/mnt/data/co-develop/downsample_data/singv/'


X_grid_singv = np.load(singv_grid_folder + 'X_grid_singv.npy')
Y_grid_singv = np.load(singv_grid_folder + 'Y_grid_singv.npy')

X_grid_radar = np.load(radar_grid_folder + 'X_interp_grid.npy')
Y_grid_radar = np.load(radar_grid_folder + 'Y_interp_grid.npy')

print(X_grid_singv.shape)
print(X_grid_radar.shape)


data_singv = np.load(singv_data_folder + year_month + 'Nt08var0' + var_grp + 'Nspn03Nend24Nx0964Ny1016.npy')
print(data_singv.shape)


#### Define regular grid centered on Radar (x,y)
#### Center of Radar grid at 1.35, 103.97
#### First set are for 0.01 degree resolution to match radar
#x_grid = np.linspace(103.34, 104.61, 128)     # Regular grid for x-coordinate
#y_grid = np.linspace(0.72, 1.99, 128)     # Regular grid for y-coordinate
#X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates


# Hand-tuned indices subset the above grid centered on radar (x,y) for 128 x 128 grid
X_grid_subset = X_grid_radar[132:(132+128),134:(134+128)]
Y_grid_subset = Y_grid_radar[132:(132+128),134:(134+128)]


# Hand-tuned indices subset the SINGV grid to above radar grid
X_singv_subset = X_grid_singv[450:(450+150),600:(600+150)]
Y_singv_subset = Y_grid_singv[450:(450+150),600:(600+150)]

lon_lat = np.transpose(np.stack([np.matrix.flatten(X_singv_subset),np.matrix.flatten(Y_singv_subset)]))

##### Code segment is to plot individual sub-sets for visualization

#data_singv_subset = data_singv[0,5,1,450:(450+150),600:(600+150)]
#print(data_singv_subset.shape)

#interpolated_values = griddata(lon_lat, np.matrix.flatten(data_singv_subset), (X_grid_subset, Y_grid_subset), method='linear')
#plt.contourf(X_grid_subset,Y_grid_subset,interpolated_values)
#plt.contourf(X_grid_singv[450:(450+150),600:(600+150)],Y_grid_singv[450:(450+150),600:(600+150)],data_singv[0,5,1,450:(450+150),600:(600+150)])

#####



n_singv = data_singv.shape[0]
print('SINGV Dataset: ' + str(n_singv))

#output = -555. * np.ones([data_singv.shape[0], data_singv.shape[2], 128, 128])
output = -555. * np.ones([data_singv.shape[0], data_singv.shape[1], data_singv.shape[2], 128, 128])

# n_singv = 8 per day * n_days
# n_radar = 12 per hour * 3 * 8 hours per day * n_days
#if (n_radar != n_singv*36):
#  print('Error in dataset size')

time_steps_singv = data_singv.shape[1]

for j in range(data_singv.shape[2]):

  print(j)
  #output_vec = []

  for i in range(n_singv):
  #print(i)

    for t_index in range(time_steps_singv):

      # 5 in index 2 is for hour 8 (which corresponds to t+2 prediction)
      #t_index = 5
      data_singv_subset = data_singv[i,t_index,j,450:(450+150),600:(600+150)]

      interpolated_values = griddata(lon_lat, np.matrix.flatten(data_singv_subset), (X_grid_subset, Y_grid_subset), method='linear')
      #output_vec.append(interpolated_values)

      #output_vec = np.array(output_vec)
      output_vec = np.array(interpolated_values)
      output[i,t_index,j,:,:] = output_vec


#output_filename = save_folder + 'singv_array_' + year_month + 'Nt08var0' + var_grp + 'Nspn03_T_index' + str(t_index)+ '.npy'
output_filename = save_folder + 'singv_array_' + year_month + 'Nt08var0' + var_grp + 'Nspn03.npy'
np.save(output_filename, output)
