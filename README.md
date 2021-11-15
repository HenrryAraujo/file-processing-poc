# file-processing-poc
PoC to showcase data processing in python

Current Python code  traverses through the files in the "source_input_files" folder and generates the output file "combined.csv" file in folder "processed_files"

The PoC is intended to fulfill below requirements:

a. Try to make it as generic as possible such that if a new file called NA Preview.csv gets dropped in the same folder, the script will be able to process it and rows in the combined.csv file will be added with the environment value being set to NA Preview.

b. Same applies if a new file called Asia Prod 4.csv gets dropped. It should add new rows to the combined.csv file with the environment being set to Asia Prod

c. Use best coding practices and write production ready code.

d. Please add unit tests for your code 

e. We will be running the code on our end once it is submitted, please have the code successfully execute without any errors 


# SETUP AND RUN INSTRUCTIONS:

To Run this program successfully, please note:
--> Make sure to use a running environment configured with Python 3.x compatible, and able to load/import supporting libraries

--> Copy program folder (and its contents) into your working directory - preferable a location able to read/write

--> Place/Update source files to process into folder: "source_input_files"

--> Once program has executed, find output file located inside folder "processed_output"


---> To Run Main Program from command prompt, execute following command:

                python process_csv_files.py

---> to Run Test Cases from command prompt, execute following command:

                python test_process_csv_files.py


--> Note1: the input format expected is csv, any other format (xls, txt, etc.) won't be processed

--> Note2: This program was written using Visual Studio Code and Python 3.8 in a windows 10 PC.
            But in case of opening and running Main Program or Test Cases in another IDE, 
            please load content of root folder into the Python IDE of your choice and follow 
            code execution steps accordingly to such IDE.


Disclaimer: **The content of this repo and the logic provided within the current python programs enclosed 
              is intended to be used to showcase concepts related to the use of python for Data Engineering, 
              with the aim of a job interview or an academic evaluation.** 
            
Disclaimer: **The author does not take any responsibility of any unexpected results 
              of running these programs outside of such aforementioned contexts**
