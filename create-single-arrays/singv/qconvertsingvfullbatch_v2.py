from netCDF4 import Dataset
from datetime import datetime, timedelta
import numpy as np
import sys
import calendar


## Lookup date
YY = int(sys.argv[1])
MM = int(sys.argv[2])
DDmax = calendar.monthrange(YY, MM)[1]


## Create name strings
header = '/mnt/data/mss_datasets/singvda_level1_wmc_2nd_batch/'
save_folder = '/mnt/data/co-develop/data/singv/correct_spin3_full/'

## Define key times
Nspn = 3 ## spin-up time (6-12 hours)
Nend = 24 ## stop time
Npre = 4 ## number of pressure levels
Nvec = [2,3,4,4,5,5,3,2] # reflectivity, rainfall, u-wind, v-wind, humidity, temperature, otherwind, radiation


## Define date ranges
#YYvec = [2023,2024,2024]
#MMvec = [12,1,2]
#DDmax = [31,31,29]
TTvec = list(range(0,24,3))
#month = 0 # select month to output
#month = int(sys.argv[1])


## Create name strings
varlist = [
'PP1SXS',
'PP1SXS',
'PP1SXS',
'PP1SXS',
'PP1SXU',
'PP1SXS',
'PP1SXU',
'PP1SXS',
'PP1SXS',
'PP1SXU',
'PP1SXU',
'PP1SXS',
'PP1SXS',
'PP1SXS',
'PP1SXS',
'PP1SXS',
]
varnamelist = [
'precipitation_rate',
'radar_reflectivity_at_1km_agl',
'thickness_of_rainfall_amount',
'relative_humidity',
'relative_humidity', # 4 pressures
'air_temperature',
'air_temperature', # 4 pressures
'total_cloud_amount',
'total_radar_reflectivity_max_in_column',
'u_wind', # 4 pressures
'v_wind', # 4 pressures
'wind_from_direction',
'max_wind_speed_of_gust',
'wind_speed',
'toa_outgoing_longwave_flux',
'total_downward_surface_shortwave_flux',
]
vvec = [
[1,8],
[0,2,7],
[9],
[10],
[3,4],
[5,6],
[11,12,13],
[14,15]
]
varlvl = [4,6,9,10] ## pressure level variables

## Define storage variables
Nx = 964
Ny = 1016




for isel in range(0,8):

	#isel = 6 # select entry in Nvec
	Nvar = Nvec[isel]
	X = np.empty(shape=[DDmax*np.shape(TTvec)[0],Nend-Nspn,Nvar,Nx,Ny])


	## Begin day/time/time/var loop
	for DD in range(1,DDmax+1):				        ## start day
		for TT in TTvec:							## start hour (multiple of 3)

			## Define time
			datefolder = datetime(YY, MM, DD, TT, 0) # 0 seconds
			print(datefolder)
			ind = (int)((DD-1)*np.shape(TTvec)[0]+TT/3)
			print(ind)

			## Loop over different training times for single reference time
			for t in range(Nspn,Nend):
				print(t)

				## Define time
				datefile = datefolder + timedelta(hours = t)
				count = 0

				for v in vvec[isel]: 	## variable number

					var = varlist[v]
					varname = varnamelist[v]
					mul = v in varlvl
						
					## Load file
					filename = header+str(datefolder.year).zfill(4)+str(datefolder.month).zfill(2)+str(datefolder.day).zfill(2)+'T'+str(datefolder.hour).zfill(2)+'00Z/'+var+str(datefolder.month).zfill(2)+str(datefolder.day).zfill(2)+str(datefolder.hour).zfill(2)+'00'+str(datefile.month).zfill(2)+str(datefile.day).zfill(2)+str(datefile.hour).zfill(2)+'0001.nc'
					
					try:

						dat = Dataset(filename, "r", format="NETCDF4")

						## Load data
						out = dat[varname][:].data
						dat.close()
	
						## Multiple pressure levels
						if mul:
							for j in range(0,Npre):
								X[ind,t-Nspn,count,:,:] = out[j] 
								count = count + 1
							count = count - 1

						## Single pressure level
						else:
							X[ind,t-Nspn,count,:,:] = out 
					except Exception as e:
						## Multiple pressure levels
						if mul:
							for j in range(0,Npre):
								X[ind,t-Nspn,count,:,:] = -999. 
								count = count + 1
							count = count - 1

						## Single pressure level
						else:
							X[ind,t-Nspn,count,:,:] = -999.				

					count = count + 1

	savename=save_folder+str(YY).zfill(4)+str(MM).zfill(2)+'Nt'+str(np.shape(TTvec)[0]).zfill(2)+'var'+str(isel).zfill(2)+'Nspn'+str(Nspn).zfill(2)+'Nend'+str(Nend).zfill(2)+'Nx'+str(Nx).zfill(4)+'Ny'+str(Ny).zfill(4)+'.npy'
	np.save(savename,X)
