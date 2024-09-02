import os
import numpy as np
from datetime import datetime
import calendar
import sys

## Define date ranges
YY = int(sys.argv[1])
MM = int(sys.argv[2])
DDmax = calendar.monthrange(YY, MM)[1]

## Create name strings
save_folder = '/mnt/data/co-develop/data/radar/'


## Define storage variables
X = np.empty(shape=[DDmax*24*12,5])


## Begin day/time/time/var loop
for DD in range(1,DDmax+1):				## start day

  for TT in range(0,24):				## start hour
    for UU in range(0,60,5):			## start minute

      VV = (int)(UU/5)

      store = (DD-1)*24*12+TT*12+VV
      X[store,0] = YY
      X[store,1] = MM
      X[store,2] = DD
      X[store,3] = TT
      X[store,4] = UU

savename = save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'_timestamps.npy'
np.save(savename,X)
