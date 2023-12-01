import unittest
from unittest.mock import patch
from extract import extract_crop_chooser

class TestExtractCropChooser(unittest.TestCase):
    
    @patch('extract.requests.get')
    def test_extract_crop_chooser(self, mock_get):
        mock_data = {
            "Monthly Time Series": {
                "2021-08-31": {
                    "1. open": "148.3100",
                    "2. high": "157.2600",
                    "3. low": "146.9100",
                    "4. close": "155.3700",
                    "5. volume": "123456789"
                },
                "2021-07-30": {
                    "1. open": "140.0000",
                    "2. high": "150.0000",
                    "3. low": "139.0000",
                    "4. close": "148.0000",
                    "5. volume": "987654321"
                }
            }
        }
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        symbol = "AAPL"
        expected_data = mock_data
        
        actual_data = extract_crop_chooser(symbol)
        
        self.assertEqual(actual_data, expected_data)import unittest

from extract import extract_weather

class TestExtractWeather(unittest.TestCase):
    
    @patch('extract.requests.get')
    def test_extract_weather(self, mock_get):
        mock_data = {
            "2021-08-31": {
                "tmax": 30.0,
                "tmin": 20.0,
                "precipitation": 0.0
            },
            "2021-09-01": {
                "tmax": 31.0,
                "tmin": 21.0,
                "precipitation": 0.0
            }
        }
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        latitude = 41.88
        longitude = -87.62
        start_date = datetime.date(2021, 8, 31)
        end_date = datetime.date(2021, 9, 1)
        variables = "tmax,tmin,precipitation"
        timezone = "America/Chicago"
        expected_data = mock_data
        
        actual_data = extract_weather(latitude, longitude, start_date, end_date, variables, timezone)
        
        self.assertEqual(actual_data, expected_data)import unittest

from extract import extract_crop_yields

class TestExtractCropYields(unittest.TestCase):
    
    @patch('extract.requests.get')
    def test_extract_crop_yields(self, mock_get):
        mock_data = {
            "data": [
                {
                    "commodity_desc": "Corn",
                    "state_alpha": "MO",
                    "year": "2010",
                    "Value": "1234"
                },
                {
                    "commodity_desc": "Corn",
                    "state_alpha": "MO",
                    "year": "2010",
                    "Value": "5678"
                }
            ]
        }
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        
        state_code = "MO"
        commodity_desc = "Corn"
        year = 2010
        expected_data = mock_data
        
        actual_data = extract_crop_yields(state_code, commodity_desc, year)
        
        self.assertEqual(actual_data, expected_data)