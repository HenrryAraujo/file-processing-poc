#----------------------------------------------------
# Unit tests class for the process_csv_files module:
# -> Below Unit Tests are intended to validate
#    both source and target locations used by the
#    main function in program process_csv_files.py
#----------------------------------------------------

#----------------------------------------------------
# Importing Libraries
#----------------------------------------------------

import unittest
import os
from process_csv_files import src_input_path, tgt_output_path

#----------------------------------------------------
# Setting up test variables for program execution
#----------------------------------------------------

test_path_run = os.path.dirname(__file__)
test_src_dir_name = '\source_input_files'
test_tgt_file_name = '\processed_output\\Combined.csv'
test_src_input_path= test_path_run + test_src_dir_name
test_tgt_output_path = test_path_run + test_tgt_file_name

#----------------------------------------------------
# Test Cases for source and destination validation
#----------------------------------------------------

class TestSrcPath(unittest.TestCase):

    def test_src_path(self):
        self.assertTrue(test_src_input_path == src_input_path, "Should be " + (test_path_run + test_src_dir_name))
 
    def test_tgt_path(self):
        self.assertTrue(test_tgt_output_path == tgt_output_path, "Should be " + (test_path_run + test_tgt_file_name))    

if __name__ == '__main__':
    unittest.main()