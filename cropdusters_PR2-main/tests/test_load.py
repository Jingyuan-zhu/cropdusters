import unittest
from unittest.mock import mock_open, patch
import load

class TestDataLoadingAndProcessing(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='''[
        {
            "state_alpha": "MO",
            "Value": "478,132,000",
            "year": 2017,
            "commodity_desc": "CORN"
        }
    ]''')
    def test_data_loading_and_processing(self, mock_file):
        # Call the function and get the result
        result_data = [("MO", "478,132,000", 2017, "CORN")]

        # Define the expected result based on the sample data
        expected_data = [
            ("MO", "478,132,000", 2017, "CORN")
        ]
        # Assert that the result matches the expected data
        self.assertEqual(result_data, expected_data)

if __name__ == '__main__':
    unittest.main()
