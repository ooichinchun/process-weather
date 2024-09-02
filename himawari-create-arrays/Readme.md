## Script to pre-process raw Himawari satellite data 

The following scripts have been tested on Himawari downloaded output as per other download scripts.

The downloaded data is put into two sets of data and split by months.

Current data has been downloaded for Dec 2023 to Feb 2024 (To be Updated).

Missing data (or days) in the dataset are replaced by -999 values for easy filtering.

The data is stored with the following indexing:<br>
[Time Index, Band Index, 2299:3501, 274:2025]

The last two indeces have been adjusted to trim the domain size (initial 0.02 degree spacing) to:
Lat: -9.99 to 14.00
Long: 90.50 to 125.49
  
This creates approximately 1200 x 1750 grid points.
  
<br>

### Instructions for use:

1. Navigate to folder 
2. Run the following line but change the band option and date to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python main.py --band 10 --sdate '2023-11-01-00:00' --edate '2023-11-30-23:55' </br>
3. Take note that the files will be written to the following directory as currently set


Arguments: </br>
The numbers have a pre-defined format. 

For example, if we need to download Band 15 we need to give the argument as follows: 

chn - "TIR"  (set as "TIR" by default) </br>
num - 3  (according to Table in Reference Bands below) </br>
	
start_date - date from which the data has to be downloaded </br>
end_date - date until which the data has to be downloaded </br>
save_path - data will be stored under this directory (adjust through --data or directly in parser)

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
