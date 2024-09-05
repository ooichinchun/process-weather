## Script to downsample all the processed data 

There are 5 scripts:
1. downsample_radar.py
2. downsample_radarTS.py
3. downsample_satel.py
4. downsample_sat_ts.py
5. downsample_singv.py (updated to downsample_singv_all_time.py for only spatial downsampling)


The script processes the data by individual months and crops everything back to 128 x 128 within the radar domain.

    # Define regular grid centered on Radar (x,y)
    # Center of Radar grid at 1.35, 103.97
    x_grid = np.linspace(103.34, 104.61, 128)     # Regular grid for x-coordinate
    y_grid = np.linspace(0.72, 1.99, 128)     # Regular grid for y-coordinate
    X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates


We use this radar grid to interpolate the satellite and SINGV data to a consistent grid.
  
<br>

### Instructions for use:

#### Radar data

1. Update data_folder and save_folder in downsample_radar.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; data_folder is where the radar grid and radar data files are stored (file directory should be /mnt/data/co-develop/data/radar/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the downsampled array will be saved (outputs currently in /mnt/data/co-develop/downsample_data/radar/) </br>

2. Run the following line but change YYYYMM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python downsample_radar.py 202401 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)


#### Radar-TS data

1. Update data_folder, radar_grid_folder and save_folder in downsample_radarTS.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; data_folder is where the radar grid and radar data files are stored (file directory should be /mnt/data/co-develop/data/radar_TS/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; radar_grid_folder is where the radar grid and radar data files are stored (file directory should be /mnt/data/co-develop/data/radar/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the downsampled array will be saved (outputs currently in /mnt/data/co-develop/downsample_data/radar_ts/) </br>

2. Run the following line but change YYYYMM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python downsample_radarTS.py 202401 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)


#### Satellite data

1. Update data_folder and save_folder in downsample_satel.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; data_folder is where the data files are stored (file directory should be /mnt/data/co-develop/data/satel/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the downsampled array will be saved (outputs currently in /mnt/data/co-develop/downsample_data/satel/) </br>

2. Run the following line but change YYYYMM to relevant parameters. An additional argument corresponds to the band group. </br>
&nbsp;&nbsp;&nbsp;&nbsp; python downsample_satel.py 202401 0 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

#<b>Missing data (or corrupted data) in the dataset may be replaced by -555 values for easy filtering. No -555 should appear though. </b>

#### Sat-TS data

1. Update data_folder and save_folder in downsample_sat_ts.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; data_folder is where the data files are stored (file directory should be /mnt/data/co-develop/data/sat_TS/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the downsampled array will be saved (outputs currently in /mnt/data/co-develop/downsample_data/sat_ts/) </br>

2. Run the following line but change YYYYMM to relevant parameters. </br>
&nbsp;&nbsp;&nbsp;&nbsp; python downsample_sat_ts.py 202401 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)




#### SINGV data

1. Update data_folder and save_folder in downsample_singv.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; singv_data_folder is where the data files are stored (file directory should be /mnt/data/co-develop/data/singv/correct_spin3_full/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; singv_grid_folder is where the singv grid and radar data files are stored (file directory should be /mnt/data/co-develop/data/singv/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; radar_grid_folder is where the radar grid and radar data files are stored (file directory should be /mnt/data/co-develop/data/radar/)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the downsampled array will be saved (outputs currently in /mnt/data/co-develop/downsample_data/singv/) </br>

2. Run the following line but change YYYYMM to relevant parameters. An additional argument corresponds to the SINGV variable group (single digit only). </br>
&nbsp;&nbsp;&nbsp;&nbsp; python downsample_singv.py 202401 0 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

The latest version only downsamples in space but not in time --> downsample_singv_all_time.py --> Use this instead for post-hoc time extraction

#<b>Missing data (or corrupted data) in the dataset may be replaced by -555 values for easy filtering. No -555 should appear though. </b>
