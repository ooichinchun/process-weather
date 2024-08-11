## Script to download Himawari satellite data 

The following scripts have been provided by Vignesh Raman based on prior work from the following Github link

[https://github.com/zxdawn/Himawari-8-gridded](https://github.com/zxdawn/Himawari-8-gridded)

Libraries required are described in the above Github link. 

<br>

### Instructions for use:

1. Navigate to ./data_preprocessing/ 
2. Run the following line but change the band and date to relevant parameters </br>
&nbsp;&nbsp;&nbsp;&nbsp; python main.py --band 10 --sdate '2023-11-01-00:00' --edate '2023-11-30-23:55' </br>
3. Take note that the intermediate files will over-write each other if multiple bands are being downloaded simultaneously to the same data directory


Arguments: </br>
The numbers have a pre-defined format. 

For example, if we need to download Band 15 we need to give the argument as follows: 

chn - "TIR"  (set as "TIR" by default) </br>
num - 3  (according to Table in Reference Bands below) </br>
	
start_date - date from which the data has to be downloaded </br>
end_date - date until which the data has to be downloaded </br>
save_path - data will be stored under this directory (adjust through --data or directly in parser)

### Sample commands:

Sample commands for the 4 (and 3) important bands are:

<br>

### Reference Bands:


| Band Type | Bands |
|-----------|------------------------------------------------|
| [EXT]     | 01:Band03                                      |
| [VIS]     | 01:Band01 02:Band02 03:Band04                  |
| [SIR]     | 01:Band05 02:Band06                            |
| [TIR]     | 01:Band13 02:Band14 03:Band15 04:Band16 <br>   05:Band07 06:Band08 07:Band09 08:Band10 <br> 09:Band11 10:Band12 |


