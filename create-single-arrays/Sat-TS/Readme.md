## Script to pre-process Sat-TS data 

The following script 'qconvertSatTS.py' is meant to pre-process Sat-TS processed output.

The script processes the data by individual months.

The data is stored with the following <b>hard-coded</b> indexing:<br>
&nbsp;&nbsp;&nbsp;&nbsp; [Time Index, 299:781, 209:911]


    # Define regular grid
    x_grid = np.linspace(80.025, 159.975, 1600)     # Regular grid for x-coordinate
    y_grid = np.linspace(-24.975, 29.975, 1100)     # Regular grid for y-coordinate
    X, Y = np.meshgrid(x_grid, y_grid)  # Meshgrid of regular (x, y) coordinates

    X_SatTS = X[299:781,209:911]
    Y_SatTS = Y[299:781,209:911]


The last two indices have been adjusted to trim the domain size (0.05 degree spacing) to:</br>
&nbsp;&nbsp;&nbsp;&nbsp; Lat: -10.025 to 14.025
&nbsp;&nbsp;&nbsp;&nbsp; Long: 90.475 to 125.525

This creates approximately 482 x 702 grid points.
  
<br>

### Current Processing status

Current data has been downloaded for Dec 2023 to Feb 2024 and processed (in /mnt/data/co-develop/data/SatTS/) 

Additional months to be processed include Mar 2024 to Jul 2024.

<br>

### Instructions for use:

1. Update header and save_folder in qconvertSatTS.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; header is where the raw SatTS data files are stored (file directory should be /mnt/data/co-develop/SatTS/ format)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the numpy arrays will be saved (outputs currently in /mnt/data/co-develop/data/sat_TS/) </br>

2. Run the following line but change YYYY and MM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python qconvertSatTS.py 2024 01 0 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

<b>Missing data (or corrupted data) in the dataset are replaced by -1 values for easy filtering. </b>

### Numpy array band Information:

4 classes in the array
1. RGB = 255,255,0 --> Class 1 (Thunderstorm)
2. RGB = 0,50,0 --> Class 0 (No Thunderstorm)
3. RGB = 0,0,255 --> Class -1 (Corrupted Data)
4. RGB = Black, No color --> Class -1 (Missing Data)

