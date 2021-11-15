#-----------------------------------------------
# Unit tests for get_files_to_process module. 
# -> below Unit Tests are intended to validate
# -> both soure and target locations 
# -> used by test_source_ip_files.py
#-----------------------------------------------

import unittest
import os
from process_csv_files import src_input_path, tgt_output_path

#-----------------------------------------------
# Setup variables for Running
#-----------------------------------------------

test_path_run = os.path.dirname(__file__)

#-----------------------------------------------
# Setup Test Cases for source and destination
#-----------------------------------------------

class TestSrcPath(unittest.TestCase):

    def test_src_path(self):
        self.assertTrue(test_path_run + r'\source_input_files' == src_input_path, "Should be " + src_input_path)
 
    def test_tgt_path(self):
        self.assertTrue(test_path_run + r'\processed_files\final_Combined.csv' == tgt_output_path, "Should be " + tgt_output_path)    

if __name__ == '__main__':
    unittest.main()