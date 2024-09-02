## Script to pre-process SINGV-DA data 

The following script 'qconvertsingvfullbatch_v1.py' is meant to pre-process SINGV-DA output.

The script processes the data in SINGV-DA into different numpy arrays (split by categories as described below) and processes the data by individual months.

The data is stored with the following <b>hard-coded</b> indexing:<br>
&nbsp;&nbsp;&nbsp;&nbsp; [SINGV-Start-Date, NWP-hour, Variable Index, 0:964,0:1016]



The last two indices follow the SINGV-DA domain size (initial XXX degree spacing) to:</br>
&nbsp;&nbsp;&nbsp;&nbsp; Lat: -9.99 to 14.00
&nbsp;&nbsp;&nbsp;&nbsp; Long: 90.50 to 125.49
  
This creates 964 x 1016 grid points.
  
<br>

### Current Processing status

Current data has been downloaded for Dec 2023 to Feb 2024 and processed (in /mnt/data/co-develop/data/singv/correct_spin3_full/) 

Additional months to be processed include Mar 2024 to Jul 2024.

<br>

### Instructions for use:

1. Update header and save_folder in qconvertsingvfullbatch_v1.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; header is where the SINGV-DA nc data files are stored (file directory should be /mnt/data/mss_datasets/singvda_level1_wmc/ format)</br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the numpy arrays will be saved (outputs currently in /mnt/data/co-develop/data/singv/correct_spin3_full/) </br>

2. Run the following line but change the YYYY, MM, and band option (0 or 1) to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python qconverthimaw.py 2024 01 0 </br>
3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)

<b>Missing data (or days) in the dataset are replaced by -999 values for easy filtering. </b>

### Numpy array band Information:


4 bands in bandopt0 (sorted by IR band num): </br>
[0] --> Band 13 --> band 1 </br>
[1] --> Band 16 --> band 4 </br>
[2] --> Band 8  --> band 6 </br>
[3] --> Band 10 --> band 8 </br>

3 bands in bandopt1 (sorted by IR band num): </br>
[0] --> Band 14 --> band 2 </br>
[1] --> Band 15 --> band 3 </br>
[2] --> Band 11 --> band 9 </br>


### Reference Bands:


| Band Type | Bands |
|-----------|------------------------------------------------|
| [EXT]     | 01:Band03                                      |
| [VIS]     | 01:Band01 02:Band02 03:Band04                  |
| [SIR]     | 01:Band05 02:Band06                            |
| [TIR]     | 01:Band13 02:Band14 03:Band15 04:Band16 <br>   05:Band07 06:Band08 07:Band09 08:Band10 <br> 09:Band11 10:Band12 |
