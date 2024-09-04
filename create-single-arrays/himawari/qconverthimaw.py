from netCDF4 import Dataset
from datetime import datetime, timedelta
import numpy as np
from os import path
import sys
import calendar
#import glob


## Create name strings
data_folder = '/mnt/data/co-develop/himawari/'
save_folder = '/mnt/data/co-develop/data/satel/'

## Define date ranges
#YYvec = [2024]
#MMvec = [2]
#DDmax = [29]
#MMvec = [12]
#DDmax = [31]
#index = 0

## Lookup date
#YY = YYvec[index]	## start year
#MM = MMvec[index]	## start month
YY = int(sys.argv[1])
MM = int(sys.argv[2])
DDmax = calendar.monthrange(YY, MM)[1]

## Create appropriate bands

bandvec = [[1,4,6,8],[2,3,9]]
#bandopt = 1
bandopt = int(sys.argv[3])

## Create name strings
#header = '/mnt/data/co-develop/himawari/'+str(YYvec[index]).zfill(4)+'/'+str(MMvec[index]).zfill(2)+'/'
header = data_folder+str(YY).zfill(4)+'/'+str(MM).zfill(2)+'/'

## Define storage variables
#Nx = 6000
#Ny = 6000
Ax = 2299
Bx = 3501
Nx = Bx - Ax
Ay = 274
By = 2025
Ny = By - Ay

#X = np.empty(shape=[DDmax[index]*24*6,np.shape(bandvec[bandopt])[0],Nx,Ny])
X = np.empty(shape=[DDmax*24*6,np.shape(bandvec[bandopt])[0],Nx,Ny])
xe = -999.*np.ones([Nx,Ny])



## Begin day/time/time/var loop
#for DD in range(1,DDmax[index]+1):		## start day
for DD in range(1,DDmax+1):				## start day
	for TT in range(0,24):				## start hour
		for UU in range(0,60,10):		## start minute

			VV = (int)(UU/10)

			## Define time
			datefolder = datetime(YY, MM, DD, TT, UU)
			print(datefolder)

			for bandnum in range(0,np.shape(bandvec[bandopt])[0]):

				bandind = bandvec[bandopt][bandnum]

				filename = header+str(datefolder.year).zfill(4)+str(datefolder.month).zfill(2)+str(datefolder.day).zfill(2)+str(datefolder.hour).zfill(2)+str(datefolder.minute).zfill(2)+'_tir_'+str(bandind).zfill(2)+'TIR['+str(bandind)+'].nc'
				print(filename)
				if not path.isfile(filename):
					print(str(0)+' file not found')
					out = xe
				else:
					print(1)
					## Load file
					dat = Dataset(filename, "r", format="NETCDF4")
					## Load data
					out = dat['tbb'][:].data
					out = out[0,Ax:Bx,Ay:By]
					dat.close()

				store = (DD-1)*24*6+TT*6+VV
				print(store)
				X[store,bandnum,:,:] = out 

savename=save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'bandopt'+str(bandopt).zfill(2)+'Nx'+str(Nx).zfill(4)+'Ny'+str(Ny).zfill(4)+'.npy'
np.save(savename,X)
