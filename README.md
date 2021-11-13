# file-processing-poc
PoC to showcase data processing in python

Current Python code  traverses through the files in the "source_input_files" folder and generates the output file "combined.csv" file in folder "processe_files"

The PoC is intended to fulfill below requirements:
    a. Try to make it as generic as possible such that if a new file called NA Preview.csv gets dropped in the same folder, the script will be able to process it and rows in the combined.csv file will be added with the environment value being set to NA Preview. 
    b. Same applies if a new file called Asia Prod 4.csv gets dropped. It should add new rows to the combined.csv file with the environment being set to Asia Prod
    c. Use best coding practices and write production ready code.
    d. Please add unit tests for your code 
    e. We will be running the code on our end once it is submitted, please have the code successfully execute without any errors 
