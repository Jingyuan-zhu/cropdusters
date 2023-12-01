

# Prewritten Methods and Basic Usage

In the following methods the API parameters are listed for the base call used in the Cropdusters prediction project. By default all calls are setup to automatically save to named json files which can be downloaded. If desired a .csv output can be utilized instead. 

---
### **`def extract_crop_yields(State_Code, commodity_desc, year)`:**

Parameters:

1. `State_Code`: The 2 digit code corresponding to a US state. By default `MO`.
2. `commodity_desc`: The commodity of intrest. By default `Corn`. See list below for a list of availible commodities.
    - __Availible Commodities:__ Barley, Beans, Corn, Cotton, Feed, Hay and Haylage, Oats, Orchards, Peanuts, Potatoes, Rice, Sorghum, Soybeans, Sugarbeets, Sugarcane, Sunflower, Sweet Potato, Tobacco, Vegetable Totals, Wheat.
3. `year`: The year of intrest. By default `2010`. Availible from 1950 forward. 

Returns:

1. None, the data is saved to `crop_yield_data.json`.

``````
    def extract_crop_yields(State_Code, commodity_desc, year)
        API_KEY = os.getenv('CROP_API_KEY')
        url = f"https://quickstats.nass.usda.gov/api/api_GET/?key={API_KEY}&commodity_desc={commodity_desc}&year__GE={year}&state_alpha={State_Code}"
        response = requests.get(url)
        data = response.json()
        with open('crop_yield_data.json', 'w') as f:
            json.dump(data, f)
``````

def extract_weather(latitude, longitude,start_date,end_date):
    '''
    Extract weather data from the Open-Meteo API.

    :param latitude: The latitude of the location.
    :param longitude: The longitude of the location.
    :param start_date: The start date for weather data.
    :param end_date: The end date for weather data.
    :return: The extracted weather data.
    '''
    url =f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m,soil_temperature_0cm,soil_moisture_0_to_1cm&daily=temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_sum,precipitation_hours&start_date={start_date}&end_date={end_date}'
    response = requests.get(url)
    data = response.json()
    with open('weather_data.json', 'w') as f:
        json.dump(data, f)
    return data


def extract_crop_chooser(symbol):
    '''
    Extract stock data for a given symbol using the AlphaVantage API.

    :param symbol: The stock symbol.
    :return: The extracted stock data.
    '''
    API_KEY = os.getenv('CROP_CHOOSER_API_KEY')  # noqa: F841
    url =f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    print(data)
    with open('crop_chooser_data.json', 'w') as f:
        json.dump(data, f)
    return data


