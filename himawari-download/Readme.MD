## Script to download Himawari satellite data 

The following scripts have been provided by Vignesh Raman based on prior work from the following Github link

[https://github.com/zxdawn/Himawari-8-gridded](https://github.com/zxdawn/Himawari-8-gridded)

### Requirements:

Libraries required are per the above Github link. 
    	
    
### Reference Bands:

-----------------------------------
[EXT] | 01:Band03
-----------------------------------
[VIS] | 01:Band01 02:Band02 03:Band04
-----------------------------------
[SIR] | 01:Band05 02:Band06
-----------------------------------
[TIR] | 01:Band13 02:Band14 03:Band15 04:Band16 05:Band07 </br>
        06:Band08 07:Band09 08:Band10 09:Band11 10:Band12
-----------------------------------


### Instructions for Use

1. Navigate to src/data_preprocessing
2. Run the following line but change the band and date to relevant parameters 
   
python main.py --band 10 --sdate '2023-11-01-00:00' --edate '2023-11-30-23:55'


Arguments: </br>
The numbers have to be given in this format. For example, if we need to download Band 15 we need to give the argument as follows: </br>
	chn - "TIR"  (set at "TIR" by default) </br>
	num - 3  (according to Table in Reference Bands above) </br>
	
start_date - date from which the data has to be downloaded </br>
end_date - date until which the data has to be downloaded </br>
save_path - data will be stored under this directory (adjust through --data or directly in parser)
