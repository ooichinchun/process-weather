# Repository for downloading and pre-processing Himawari and other data sources

Scripts for downloading and processing satellite and other data are collected here.

In general, the scripts are meant for sequential processing:
1. Loading raw data from individual files into a single month (by categories)
2. Interpolation and cropping of the raw data into smaller spatial regions (but still larger than TMA)
3. Additional processing as-required (e.g. to predict different time ahead)

### Scripts for downloading Himawari Satellite data

Scripts and instructions for use in order to download the different Himawari bands are provided and described. The script provides for automated downloading of a single band for a single month at a time.

### Scripts for pre-processing Himawari Satellite data

Scripts and instructions for use in order to pre-process the Himawari bands are provided and described. The script collects the bands for a single month and creates 2 numpy arrays per month (with 4 and 3 bands respectively) for inclusion.

### Scripts for pre-processing Sat-TS labels

Scripts and instructions for use in order to load and save the Sat-TS labels from images are provided and described. The script loads the Sat-TS images for a single month and creates a numpy array for the month.

### Scripts for processing radar data

Scripts and instructions for use in order to pre-process the radar data are provided and described.

### Scripts for processing Radar-TS labels

Scripts and instructions for use in order to load and save the Radar-TS labels from images are provided and described. The script loads the Radar-TS images for a single month and creates a numpy array for the month.

### Scripts for processing NWP data

Scripts and instructions for use in order to pre-process NWP data are provided and described.

