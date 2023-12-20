import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def extract_crop_yields(State_Code = "MO", commodity_desc = "Corn", year = 2010):
    '''
    Get a list of the crops we want, call this API for each state, for each crop from the USDA API.

    :param State_Code: The state code (default: "MO").
    :param commodity_desc: The commodity description (default: "Corn").
    :param year: The year for data extraction (default: 2010).
    :return: None

    '''
    API_KEY = os.getenv('CROP_API_KEY')
    url = f"https://quickstats.nass.usda.gov/api/api_GET/?key={API_KEY}&commodity_desc={commodity_desc}&year__GE={year}&state_alpha={State_Code}"
    response = requests.get(url)
    data = response.json()
    with open('/workspaces/cropdusters_PR2/cropdusters/crop_yield_data.json', 'w') as f:
        json.dump(data, f)
    return data



def extract_weather(latitude, longitude, start_date, end_date):
    '''
    Extract weather data from the Open-Meteo API.

    :param latitude: The latitude of the location.
    :param longitude: The longitude of the location.
    :param start_date: The start date for weather data.
    :param end_date: The end date for weather data.
    :return: The extracted weather data.
    '''
    url =f'https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum'
    response = requests.get(url)
    data = response.json()
    with open('/workspaces/cropdusters_PR2/cropdusters/weather_data.json', 'w') as f:
        json.dump(data, f)
    return data


def extract_crop_chooser(symbol):
    '''
    Extract stock data for a given symbol using the AlphaVantage API.

    :param symbol: The stock symbol.
    :return: The extracted stock data.
    '''
    API_KEY = os.getenv('CROP_CHOOSER_API_KEY')
    url =f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    print(data)
    with open('/workspaces/cropdusters_PR2/cropdusters/crop_chooser_data.json', 'w') as f:
        json.dump(data, f)
    return data


