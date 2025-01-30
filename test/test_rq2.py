import unittest
import os
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch
import rq2

class TestRQ2Function(unittest.TestCase):

    """Here I'm creating temporary files and clearing them after the test"""
    def setUp(self):

        self.temp_input_dir = tempfile.mkdtemp()
        self.temp_output_dir = tempfile.mkdtemp()

    def tearDown(self):

        shutil.rmtree(self.temp_input_dir)
        shutil.rmtree(self.temp_output_dir)

    def create_test_json_file(self, filename, content):
        """This is a method to create test JSON files"""
        file_path = os.path.join(self.temp_input_dir, filename)
        with open(file_path, 'w') as f:
            json.dump(content, f)
        return file_path
###################################################################

    def test_swh(self):

        """This is for testing the detection of SWH"""
        test_data = [
                {
                    "community": "ENVRI",
                    "githublink": "https://github.com/QuantConnect/Research"
                },
                {
                    "community": "ENVRI",
                    "githublink": "https://github.com/unitaryfund/research"
                }

        ]
        self.create_test_json_file('output_test1.json', test_data)
        
        # This is a mock input to avoid manual input during testing
        with patch('builtins.input', side_effect=[
            self.temp_input_dir, 
            'test_output_swh_rq2.json', 
            self.temp_output_dir
        ]):
            token = "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhMTMxYTQ1My1hM2IyLTQwMTUtODQ2Ny05MzAyZjk3MTFkOGEifQ"            
            rq2.rq2(
                self.temp_input_dir, 
                token,
                'test_output_swh_rq2.json', 
                self.temp_output_dir
            )
        
        # This is  to verify output file was created
        output_path = os.path.join(self.temp_output_dir, 'test_output_swh_rq2.json', 
)
        self.assertTrue(os.path.exists(output_path))
        
        # This is to check the output of the file
        with open(output_path, 'r') as f:
            result = json.load(f)
        
        self.assertEqual(result['swh']['summary']["count_in_swh"], 1)
        self.assertEqual(result['swh']['summary']["count_not_in_swh"], 1)

        
if __name__ == '__main__':
    unittest.main()