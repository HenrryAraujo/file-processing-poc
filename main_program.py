import pandas as pd
import csv
import os
import pathlib
import shutil
from string import digits

#-----------------------------------------------
# Base variables and Initial Global Settings
#-----------------------------------------------

path_run = os.path.dirname(__file__)
path_rejected = path_run + '\\rejected_files\\'

#-----------------------------------------------
# Proccessing list of files in source folder
#-----------------------------------------------

def get_files_to_process(source_folder, output_file_path):
    files = os.listdir(source_folder)
    textfiles = [file for file in files if file.endswith(".csv") or file.endswith('.txt')]
    with open (output_file_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(('Source IP','Environment'))
        for files in textfiles:
            if files.endswith('csv'):
                df_file = pd.read_csv(os.path.join(source_folder,files), delimiter= None if files.endswith('csv') else '\t')
                for index, row in df_file.iterrows():
                    env_name = "".join(filter(lambda x: not x.isdigit(), files))
                    writer.writerow((row[0], env_name.removesuffix('.csv')))
            # else:
            #    shutil.move(path_rejected + files, files)

#-----------------------------------------------clear
# Setup variables for Running
#-----------------------------------------------

src_dir_name = r'\source_input_files'
tgt_dir_name = r'\processed_files\final_Combined.csv'
src_input_path= path_run + src_dir_name
tgt_output_path = path_run + tgt_dir_name

#-----------------------------------------------
# Callign main method
#-----------------------------------------------

get_files_to_process(src_input_path, tgt_output_path)