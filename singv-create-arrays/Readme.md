## Script to pre-process SINGV-DA data 

The following script 'qconvertsingvfullbatch_v1.py' is meant to pre-process SINGV-DA output.

The script processes the data in SINGV-DA into different numpy arrays (split by categories as described below) and processes the data by individual months.

The data is stored with the following <b>hard-coded</b> indexing:<br>
&nbsp;&nbsp;&nbsp;&nbsp; [SINGV-Start-Date, NWP-hour, Variable Index, 0:964,0:1016]

The last two indices follow the SINGV-DA domain size (initial 1.5 km spacing) to:</br>
&nbsp;&nbsp;&nbsp;&nbsp; Lat: -5.5 to 7.5
&nbsp;&nbsp;&nbsp;&nbsp; Long: 94.80 to 108.5
  
This creates 964 x 1016 grid points with 1.5 km spacing between grid points.
  
<br>

### Current Processing status

Current data has been downloaded for Dec 2023 to Feb 2024 and processed (in /mnt/data/co-develop/data/singv/correct_spin3_full/) 

Additional months to be processed include Mar 2024 to Jul 2024.

<br>

### Instructions for use:

1. Update header and save_folder in qconvertsingvfullbatch_v1.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; header is where the SINGV-DA nc data files are stored (file directory should be /mnt/data/mss_datasets/singvda_level1_wmc/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the numpy arrays will be saved (outputs currently in /mnt/data/co-develop/data/singv/correct_spin3_full/) </br>

2. Run the following line but change the YYYY and MM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python qconvertsingvfullbatch_v1.py 2024 01 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

<b>Missing data in the dataset is replaced by -999 values for easy filtering. </b>

### Reference Groups for Variable Index:

| 8 Variable Groups       | Order                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reflectivity (2 variables) | 0: radar_reflectivity_at_1km_agl<br>1: total_radar_reflectivity_max_in_column                                                                       |
| Rainfall (3 variables)     | 0: precipitation_rate<br>1: rainfall_accumulation-PT01H<br>2: total_cloud_amount_max_random_overlap                                                  |
| U-wind (4 variables)       | u_wind_on_pressure_levels<br>Larger index is higher height (lower pressure)                                                                         |
| V-wind (4 variables)       | v_wind_on_pressure_levels<br>Larger index is higher height (lower pressure)                                                                         |
| Humidity (5 variables)     | 0: relative_humidity_at_screen_level<br>1-4: relative_humidity_on_pressure_levels<br>Larger index is higher height (lower pressure)                  |
| Temperature (5 variables)  | 0: temperature_at_screen_level<br>1-4: temperature_on_pressure_levels<br>Larger index is higher height (lower pressure)                             |
| Other Winds (3 variables)  | 0: wind_direction_at_10m<br>1: wind_gust_at_10m-PT01H<br>2: wind_speed_at_10m                                                                      |
| Radiation (2 variables)    | 0: total_downward_surface_shortwave_flux<br>1: toa_outgoing_longwave_flux                                                                           |

