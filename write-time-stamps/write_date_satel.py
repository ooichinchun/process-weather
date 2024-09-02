from datetime import datetime, timedelta
import calendar
import numpy as np
from os import path
import sys

## Define date ranges
YY = int(sys.argv[1])
MM = int(sys.argv[2])
DDmax = calendar.monthrange(YY, MM)[1]

## Create name strings
save_folder = '/mnt/data/co-develop/data/satel/'

## Define storage variables
#Nx = 6000
#Ny = 6000
Ax = 2299
Bx = 3501
Nx = Bx - Ax
Ay = 274
By = 2025
Ny = By - Ay


# 5 Variables: YY / MM / DD / HH / MIN
X = np.empty(shape=[DDmax*24*6,5])


## Begin day/time/time/var loop
for DD in range(1,DDmax+1):				## start day
	for TT in range(0,24):				## start hour
		for UU in range(0,60,10):		## start minute

			VV = (int)(UU/10)

			## Define time
			datefolder = datetime(YY, MM, DD, TT, UU)
			print(datefolder)

			store = (DD-1)*24*6+TT*6+VV
			print(store)

			X[store,0] = YY
			X[store,1] = MM
			X[store,2] = DD
			X[store,3] = TT
			X[store,4] = UU


savename=save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'_timestamps.npy'
np.save(savename,X)
