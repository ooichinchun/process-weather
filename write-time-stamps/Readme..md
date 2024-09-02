## Script to write timestamps for each month for different time steps 

The following scripts 'write_date_XXX.py' write arrays with the expected time steps.

The script processes the data by individual months.

The length of the arrays will match the number of data entries expected for each month for each dataset:
1. Radar --> 5 min interval
2. Satellite --> 10 min interval
3. SINGV --> 1 hour interval per run (3 hours between runs)

<br>

### Instructions for use:

1. Update save_folder in *.py. </br>
&nbsp;&nbsp;&nbsp;&nbsp; save_folder is where the numpy arrays will be saved </br>

2. Run the following line but change YYYY and MM to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python write_data_XXX.py 2024 01 </br>

3. Note that the files will be written to the directory as set in save_folder (make sure to check the file directory is updated)
