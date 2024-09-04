import os
import numpy as np
import matplotlib.pyplot as plt
import PIL
import calendar
import sys


"""The following bounds can be used to georeference the SatTS data to WGS84 coordinate system.

"ulx": 80, "uly": 30, "lrx": 160, "lry": -25

x: 80 to 160 (80)
y: -25 to 30 (55)

The interpretation of the data:

Pixel:Colour
Thunderstorm: Yellow (R: 255; G: 255; B: 0)
Not thunderstorm: Dark Green (R: 0; G: 50; B: 0)
Corrupted data: Blue (R: 0; G: 0; B: 255)
No data available: Black/No colour


# 4 Classes
# RGB = 255,255,0 --> Class 1 (Thunderstorm)
# RGB = 0,50,0 --> Class 0 (No Thunderstorm)
# RGB = 0,0,255 --> Class -1 (Corrupted Data)
# RGB = Black, No color --> Class -1 (Missing Data)

"""

## Create name strings
##header = '/mnt/data/co-develop/ooicc/SatTS/' + str(YY) + '/' + str(MM).zfill(2) + '/'
header = '/mnt/data/co-develop/SatTS2/'
save_folder = '/mnt/data/co-develop/data/sat_TS/'

# Define regular grid
#x_grid = np.linspace(80.025, 159.975, 1600)     # Regular grid for x-coordinate
#y_grid = np.linspace(-24.975, 29.975, 1100)     # Regular grid for y-coordinate
#X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates

#X_SatTS = X[299:781,209:911]
#Y_SatTS = Y[299:781,209:911]

#np.save('/content/drive/My Drive/Colab Notebooks/met-atm-data/X_grid_SatTS.npy',X_SatTS)
#np.save('/content/drive/My Drive/Colab Notebooks/met-atm-data/Y_grid_SatTS.npy',Y_SatTS)


## Define date ranges
#YYvec = [2023,2023,2024,2024]
#MMvec = [4,12,1,2]
#month = 0

## Lookup date
#YY = YYvec[month]	## start year
#MM = MMvec[month]	## start month
YY = int(sys.argv[1])
MM = int(sys.argv[2])
print(YY)
print(MM)
DDmax = calendar.monthrange(YY,MM)[1]
#print(DDmax)



## Define storage variables
## Initial size is 1100 x 1600
## Reduced size is 482 x 702
## X goes from 90.475  to 125.525
## Y goes from -10.025 to 14.025
## Corresponding Indices
# X_SatTS = X[299:781,209:911]
# Y_SatTS = Y[299:781,209:911]

#Nx = 1100
#Ny = 1600
Nx = 482
Ny = 702
X = np.full((DDmax*24*6,Nx,Ny,1), -1.)
#xe = -999.*np.ones([Nx,Ny])




## Begin day/time/time/var loop
for DD in range(1,DDmax+1):				## start day
  for TT in range(0,24):				## start hour
    for UU in range(0,60,10):			## start minute

      VV = (int)(UU/10)

      ## Load file
      filehead = header + str(YY).zfill(4) + str(MM).zfill(2) + str(DD).zfill(2) + str(TT).zfill(2) + str(UU).zfill(2)
      filename = filehead + '_H8_SatTS.png'
      #print(filename)

      try:

        ## Load data
        xx = PIL.Image.open(filename)
        xx_array = np.array(xx)
        xx.close()
        #print('File Loaded' + filename)
        yy = np.full((1100, 1600, 1), -1)

        # Apply the conditions to update the yy array
        yy[xx_array[:,:,0] == 255, 0] = 1
        yy[xx_array[:,:,1] == 50, 0] = 0

        # Apply the conditions to update the yy array
        X[(DD-1)*24*6+TT*6+VV, :, :, 0] = yy[299:781,209:911,0]

      except Exception as e:
        print('Missing: ' + filename)

savename = save_folder + str(YY).zfill(4)+str(MM).zfill(2)+'Nx'+str(Nx).zfill(4)+'Ny'+str(Ny).zfill(4)+'.npy'
np.save(savename,X)

#plt.contourf(X_SatTS, Y_SatTS, X[0,:,:,0])
#print(X.shape)

