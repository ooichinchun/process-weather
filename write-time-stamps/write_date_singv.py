from datetime import datetime
import calendar
import numpy as np
import sys

## Save location
save_folder = '/mnt/data/co-develop/data/singv/'

## Define key times
Nspn = 3 ## spin-up time (6-12 hours)
Nend = 24 ## stop time

## Define date ranges
TTvec = list(range(0,24,3))

## Lookup date
YY = int(sys.argv[1]) # start year
MM = int(sys.argv[2]) # start month
DDmax = calendar.monthrange(YY,MM)[1]


## Define storage variables
Nx = 964
Ny = 1016


# 5 Variables: YY / MM / DD / HH / SINGV(t)
X = np.empty(shape=[DDmax*np.shape(TTvec)[0],5])


## Begin day/time/time/var loop
for DD in range(1,DDmax+1):				## start day
	for TT in TTvec:					## start hour (multiple of 3)

		## Define time
		datefolder = datetime(YY, MM, DD, TT, 0) # 0 seconds
		print(datefolder)
		ind = (int)((DD-1)*np.shape(TTvec)[0]+TT/3)
		print(ind)

		## Loop over different training times for single reference time
		for t in range(Nspn,Nend):
			print(t)

			X[ind,0] = YY
			X[ind,1] = MM
			X[ind,2] = DD
			X[ind,3] = TT
			X[ind,4] = t


savename=save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'Nt'+str(np.shape(TTvec)[0]).zfill(2)+'_timestamps.npy'
np.save(savename,X)
