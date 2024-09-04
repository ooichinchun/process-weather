import os
import netCDF4 as nc
import numpy as np
from scipy.interpolate import griddata
#import matplotlib.pyplot as plt

from datetime import datetime, timedelta
import calendar

from glob import glob
import pyproj
import sys


## Create name strings
#header = '/mnt/data/mss_datasets/radar_unzipped/'+str(mmvec[month])+'/'
#header = os.getcwd()
header = '/mnt/data/co-develop/radar2'
save_folder = '/mnt/data/co-develop/data/radar/'
print(header)


# Radii of coverage circles
lat_min, lat_max = 1.2, 1.5
lon_min, lon_max = 103.6, 104.05
radar_location = (1.34911, 103.972583)



def lat_lon_transform(x,y):
    # Define the Azimuthal Equidistant projection parameters
    projection_params = {
        'proj': 'aeqd',  # Azimuthal Equidistant projection
        'lat_0': 1.34911,  # Latitude of projection origin
        'lon_0': 103.972583,  # Longitude of projection origin
        'ellps': 'sphere',  # Use a spherical Earth model
        'units': 'm'  # Units of measurement (meters)
    }

    # Create a PyProj Transformer object for the Azimuthal Equidistant projection
    aeqd_transformer = pyproj.Transformer.from_proj(
        pyproj.Proj(**projection_params),  # From Azimuthal Equidistant projection
        pyproj.Proj(proj='latlong'),  # To latitude and longitude
        always_xy=True  # Always treat inputs as X, Y (longitude, latitude)
    )

    # Project the coordinates to latitude and longitude
    lon, lat = aeqd_transformer.transform(x, y)
    return lon, lat

def interpolate_xy(f, X_interp, Y_interp):

  try:

    filename = glob(f + '*dBZ.cappi_Radar Data.n*')[0]
    print(filename)

    file = nc.Dataset(filename,'r')
    band1_data = file.variables['Band1'][:]

    unmasked_indices = np.where(band1_data.mask == False)
    #print(len(unmasked_indices[0]))

    # Checks for presence of radar signals (missing should mean clear sky --> set to -10 everywhere)
    if len(unmasked_indices[0]) > 0:

      azimuthal_equidistant = file.variables['azimuthal_equidistant']

      x = file.variables['x'][:]
      y = file.variables['y'][:]

      X,Y = np.meshgrid(x,y)

      #plt.contourf(X,Y,band1_data)

      X = np.matrix.flatten(X)
      Y = np.matrix.flatten(Y)
      LON,LAT = lat_lon_transform(X,Y)

      lon_lat = np.transpose(np.stack([LON,LAT]))

      # Interpolation with nearest negates fill_value option --> Interpolation affects the shape slightly
      interpolated_values = griddata(lon_lat, np.matrix.flatten(band1_data), (X_interp, Y_interp), method='nearest', fill_value=np.nan)

    else:
      interpolated_values = -10.*np.ones(X_interp.shape)
      print(X_interp.shape)

    file.close()

  except Exception as e:

    print('Corrupted')
    interpolated_values = -999.*np.ones(X_interp.shape)

  return interpolated_values

## Define date ranges
#YYvec = [2023,2023,2024,2024]
#MMvec = [4,12,1,2]
#DDmax = [30,31,31]
#mmvec = ['2023Apr','2023Dec','2024']
#month = 2 # select month to output

## Lookup date
#YY = YYvec[month]	## start year
#MM = MMvec[month]	## start month
YY = int(sys.argv[1])
MM = int(sys.argv[2])
DDmax = calendar.monthrange(YY, MM)[1]
print(DDmax)



# Define regular grid for Lat Lon Interpolation
Nx = 401
Ny = 401
x_grid_interp = np.linspace(102.0, 106.0, Nx)     # Regular grid for x-coordinate
y_grid_interp = np.linspace(-0.6, 3.4, Ny)     # Regular grid for y-coordinate
X_interp, Y_interp = np.meshgrid(x_grid_interp, y_grid_interp)  # Meshgrid of regular (x, y) coordinates


## Define storage variables
## -999 is for corrupted / missing files ; -10 everywhere is clear sky
X = np.empty(shape=[DDmax*24*12,Nx,Ny])
xe = -999.*np.ones([Nx,Ny])


## Begin day/time/time/var loop
for DD in range(1,DDmax+1):				## start day

  sample_name = glob(header + '/' + str(YY).zfill(4) + '-' + str(MM).zfill(2) + '-' + str(DD).zfill(2) + '/*.nc*')

  for TT in range(0,24):				## start hour
    for UU in range(0,60,5):				## start minute

      VV = (int)(UU/5)

      ## Define time
      datefolder = datetime(YY, MM, DD, TT, UU)
      #print(datefolder)

      filehead = header + '/' +str(datefolder.year).zfill(4)+'-'+str(datefolder.month).zfill(2)+'-'+str(datefolder.day).zfill(2)+'/'+str(datefolder.year).zfill(4)+str(datefolder.month).zfill(2)+str(datefolder.day).zfill(2)+str(datefolder.hour).zfill(2)+str(datefolder.minute).zfill(2)
      print(filehead)
	  
      valid = False
      for samples in sample_name:
        if filehead in samples:
          #filename = glob(filehead + '*dBZ.cappi_Radar Data.nc4')[0]
          print(filehead)
          valid = True

      if valid:
        interp_values = interpolate_xy(filehead, X_interp, Y_interp)
      else:
        interp_values = xe

      X[(DD-1)*24*12+TT*12+VV,:,:] = interp_values

print(X.max())
print(X.min())

#savename = header + '/'+str(YY).zfill(4)+str(MM).zfill(2)+'Nx'+str(Nx).zfill(4)+'Ny'+str(Ny).zfill(4)+'.npy'
savename = save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'Nx'+str(Nx).zfill(4)+'Ny'+str(Ny).zfill(4)+'.npy'
np.save(savename,X)
