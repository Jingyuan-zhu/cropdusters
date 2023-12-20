

# Prewritten Methods and Basic Usage

In the following methods the API parameters are listed for the base call used in the Cropdusters prediction project. By default all calls are setup to automatically save to named json files which can be downloaded. If desired a .csv output can be utilized instead. 

---
### **`def extract_crop_yields(State_Code, commodity_desc, year)`:**
*Gets historical crop yields from the National Agriculture Statistics Survey for the specified parameters*


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

### **`def extract_weather(latitude, longitude, start_date, end_date):`**
*Returns weather data (forecasted or historical) on an hourly and daily basis at the location and dates specified.*

Parameters:

1. `latitude`: The latitude of the location in decimal format.
2. `longitude`: The longitude of the location in decimal format.
    - Note that this is set to manual input in the script for manimum specificity but this can also be set up to take a `City, State` pair or zip code. Refer to the Open-Meteo API docs for more information on this implementation.
3. `start_date`: The first date for which weather is requested
4. `end_date`: **Optional** The end date of the weather window. If not provided the API will return 10 days from the start date. A test checks for the presence of the `end_date` and will error if not provided. Disable this test if using a customized implementation of the method. 

Returns:

1. The extracted weather data for the location and specified date range is saved to a local file `weather_data.json`. The weather parameters included in this output are on an hourly basis are:

    - `temperature_2m`: Air temperature at 2 meters above ground
    - `relative_humidity_2m`: Relative humidity at 2 meters above ground
    - `precipitation`: Total precipitation (rain, showers, snow) sum of the preceding hour
    - `cloudcover`: Total cloud cover as an area fraction
    - `windspeed_10m`: Wind speed at 10 meters above ground in km/h
    - `soil_temperature_0cm`: Temperature in the soil at 0 cm depth. 0 cm is the surface temperature on land or water surface temperature on water depending on location.
    - `soil_moisture_0_to_1cm`: Average soil water content as volumetric mixing ratio at 0-1 cm

2. And on a daily basis are:

    - `temperature_2m_max`: Maximum daily air temperature at 2 meters above ground.
    - `temperature_2m_min`: Minimum daily air temperature at 2 meters above ground.
    - `uv_index_max`: Daily maximum in UV Index.
    - `precipitation_sum`: Sum of daily precipitation (including rain, showers and snowfall).
    - `precipitation_hours`: The number of hours with rain. `Showers_sum` and `Snowfall_sum` are also availible for more specific precipitation types.
    - `start_date`: The input start date.
    - `end_date`: The input end date. Returned as null values if not specified.

``````
    def extract_weather(latitude, longitude, start_date, end_date):
        url =f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m,soil_temperature_0cm,soil_moisture_0_to_1cm&daily=temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_sum,precipitation_hours&start_date={start_date}&end_date={end_date}'
        response = requests.get(url)
        data = response.json()
        with open('weather_data.json', 'w') as f:
            json.dump(data, f)
        return data
``````


### **`def extract_crop_chooser(symbol):`**
*Returns the stock data for a given symbol using the AlphaVantage API*

Parameters:

1. `symbol`: The stock symbol/ticker of intrest. Must be listed on a US exchange such as the Nasdaq or New York Stock Exchange.

Returns:

1. `Metadata`: Composed of information about the symbol, last data refresh, and time zone (by default EST)
2. `Monthly Time Series`: A dictionary of the following parameters for each month. Dictionaries are keyed with the last date for which data was collected (ussually the last day of the month). Data is averaged monthly except for the current month which reflects the average of dates in the month. Data provided from the current month to June 2010 by default. *Note that the below parameters are numbered 1 to 5 in the dictionary and can be accessed by name or index.*
    - `open`: The average open price.
    - `high`: The average maximum price achived by the symbol daily
    - `low`: The average minimum price of the symbol during daily
    - `close`: The average close price.
    - `volume`: The average daily volume of trades rounded to the nearest whole number.

``````
    def extract_crop_chooser(symbol):
        '''
        API_KEY = os.getenv('CROP_CHOOSER_API_KEY')  # noqa: F841
        url =f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}'

        response = requests.get(url)
        data = response.json()
        print(data)
        with open('crop_chooser_data.json', 'w') as f:
            json.dump(data, f)
        return data
``````

<br>
<br>
<br>
Hey 👋 Thanks for checking out the docs! <br>
Make sure to contribute or open an issue to help out the community.
