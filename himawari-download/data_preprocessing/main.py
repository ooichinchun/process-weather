#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import count2tbb
import multiprocessing
import concurrent.futures
from pathlib import Path
import argparse

download_data_dir = '/mnt/ssd/public_datasets/himawari/ooicc/band8/'

parser = argparse.ArgumentParser(description='Himawari Satellite Data Download')
parser.add_argument('--data', default=download_data_dir, type=Path, metavar='DIR',
                    help='path to dataset')
parser.add_argument('--workers', default=0, type=int, metavar='N',
                    help='number of data loader workers')
parser.add_argument('--sdate', default='2023-12-01-00:00', type=str, metavar='DATE',
                    help='start date to download')
parser.add_argument('--edate', default='2023-12-31-23:55',
                    type=str, metavar='DATE',
                    help='end date for download')
parser.add_argument('--band', default=8, type=int)


if __name__ == "__main__":
    args = parser.parse_args()
    
    count2tbb.main(req_path='./count2tbb_v101',save_path = args.data,
          sdate =args.sdate, edate =args.edate,
          tstep = 5, chn ='TIR', num = str(args.band), compiler = 'gfortran', debug=1,
      )


