#Background
@given('data on crop yields for areas in the US is gettable')
def get_crop_yield():
  return crop_dusters.get_data(“API_LINK”) #waiting on API key

#Scenario 1
@given('Commodity prices are available as an API')
def get_crop_price(crop):
  return crop_dusters.get_data('https://data.tradefeeds.com/api/v1/...') #Waiting on API key to complete this link

@when('User enters the crop type, field size, and location/location permission is allowed)
def test_potential_result():
  #potential loop here for different crop types as more are added to the dataset
  est_profit = crop_dusters.estimate_profit(location= ‘st. louis’, area=1, crop_type= ‘corn’)

@then('display potential profits by crop type')
  plt.bar(est_profit['crop_type'],est_profit['profit'])

#Scenario 2
@given('crop yield statistics are available for the local area and national crop statistics are already saved by another API')
def get_crop_yield():
  crop_dusters.get_data(“API_LINK”) #waiting on API key

import requests
@when('the user enables location or provides a city,state or zipcode')
def get_location():
  response = requests.get('https://ipinfo.io')
  data = response.json()
  location = data.get('loc')
  user_location = location.split(',')
  latitude, longitude = user_location

import plotly.express as px
@then('The user is presented with a dashboard showing the advantages of each crop and details like water needed, growth period, etc')
def show_crop_info():
  fig = px.bar(data, x='Crop', y='Yield (tons per hectare)', title='Crop Yields')
  #additional attributes and visualizations such as line plots, bar plots, time series, etc.
  fig.show()
  