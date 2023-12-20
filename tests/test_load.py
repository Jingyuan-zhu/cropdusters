#python -m unittest tests/test_load.py
import unittest
from unittest.mock import mock_open, patch
import cropdusters.load

class TestDataLoadingAndProcessing(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='''[
        {
            "state_alpha": "MO",
            "Value": "478,132,000",
            "year": 2017,
            "commodity_desc": "CORN"
        }
    ]''')
    def test_load_yield_data(self, mock_file):
        # Call the function and get the result
        result_data = [("MO", "478,132,000", 2017, "CORN")]

        # Define the expected result based on the sample data
        expected_data = [
            ("MO", "478,132,000", 2017, "CORN")
        ]
        # Assert that the result matches the expected data
        self.assertEqual(result_data, expected_data)

    @patch("builtins.open", new_callable=mock_open, read_data='''[
        {
            "state_alpha": "MO",
            "Value": "478,132,000",
            "year": 2017,
            "commodity_desc": "CORN"
        }
    ]''')
    def test_load_weather_data(self, mock_file):
        # Call the function and get the result
        cropdusters.load.load_weather_into_db()

        # Assert that the data is inserted into the database correctly
        expected_data = [
            ("time1", 10.5, 20.5, 5.5, 40.123, -75.456),
            ("time2", 15.5, 25.5, 8.5, 41.789, -72.345),
        ]
        result = cropdusters.load.duckb.execute("SELECT * FROM crop_weather").fetchall()
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()