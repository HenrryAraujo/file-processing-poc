#----------------------------------------------------
# Python program to process csv files:
# -> Below program is intended to showcase some 
#    Python functionalities to process data 
#    from csv files.
#
#    The program will process any new incoming file and
#    set its ip detils identifies by file name prefix 
#----------------------------------------------------

#----------------------------------------------------
# Importing Libraries
#----------------------------------------------------

import pandas as pd
import csv
import os
from pathlib import Path

#----------------------------------------------------
# Base variables and Initial Global Settings
# and Setup variables for Running
#----------------------------------------------------

path_run = os.path.dirname(__file__)
src_dir_name = '\source_input_files'
tgt_file_name = '\processed_output\\Combined.csv'
src_input_path= path_run + src_dir_name
tgt_output_path = path_run + tgt_file_name

#----------------------------------------------------
# Function to Proccess files in source folder
#----------------------------------------------------

def get_process_ip_details(source_folder, output_file_path):
    files = os.listdir(source_folder)
    textfiles = [file for file in files if file.endswith(".csv")]
    with open (output_file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(('Source IP','Environment'))
        for files in textfiles:
                df_file = pd.read_csv(os.path.join(source_folder,files), delimiter= None if files.endswith('csv') else '\t')
                for index, row in df_file.iterrows():
                    env_name = "".join(filter(lambda x: not x.isdigit(), files))
                    writer.writerow((row[0], env_name.removesuffix('.csv')))

#----------------------------------------------------
# Triggering main method - for stand alone run
#----------------------------------------------------

if Path(src_input_path).is_dir():
    get_process_ip_details(src_input_path, tgt_output_path)
else:
    print('Double Check Source Path')
