## Script to pre-process radar CAPPI data 

The following script 'qconvertradar.py' is meant to pre-process CAPPI radar output into a consistent grid. Note that this data is already processed via interpolation from the radial scans. Pyproj package is used to convert the original grid (centered on the radar location) to a regular grid.

The script processes the data by individual months. 

The array has been adjusted to interpolate the domain (0.01 degree spacing) to:</br>
&nbsp;&nbsp;&nbsp;&nbsp; Lat: -0.6 to 3.4
&nbsp;&nbsp;&nbsp;&nbsp; Long: 102.0 to 106.0
  
This creates 401 x 401 grid points.
  
<br>

### Current Processing status

Current data has been downloaded for Dec 2023 to Feb 2024 and processed (in /mnt/data/co-develop/data/radar/) 

Additional months to be processed include Mar 2024 to Jul 2024.

<br>

### Instructions for use:

1. Update header and save_folder in qconvertradar.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; header is where the raw radar data files are stored (file directory should be /mnt/data/co-develop/radar/YYYY-MM-DD/ format)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the numpy arrays will be saved (outputs currently in /mnt/data/co-develop/data/radar/) </br>

2. Run the following line but change the YYYY, MM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python qconvertradar.py 2024 01 </br>
3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

<b> Missing data (or days) in the dataset are replaced by -999 values. </b>
<b> Clear sky days in the dataset are replaced by -10 values in whole day. </b>
<b> Interpolation with 'nearest' replaces missing values in a single scan with -10000 (needs to be checked and re-scaled) </b>
