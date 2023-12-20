Feature: crop_yield_prediction
This feature aims to inform users what their yield would look like for given crops in given locations with given meteorological data.

Background: 
Given we already obtained data for different crop yields across the United States organized by States. We also have daily weather data. 
	specific_crop_yields = crop_dusters.get_data(“API”)
	weather_table = crop_dusters.load_data
(“API_bigquery-public-data:ghcn_d.ghcnd_2023”)
		
Scenario: Display crop yields based on location and crop type
     Given we already have the tables that store yields for    
different crop type and locations     
When User inputs both location and crop type
	crop_dusters.estimate_profit(location= ‘st. louis’, 
crop_type= ‘corn’ )
     Then we display the yield using the 3D plot
		yield = crop_dusters.3d_plot(‘corn’, ‘st. louis’)

Scenario: Predict crop yields based on location, crop type, minimum temperature, maximum temperature, and precipitation
      Given we have data for crop yields and weather
 specific_crop_yields = crop_dusters.get_data(“API”)
 weather_table = crop_dusters.load_data
(“API_bigquery-public-data:ghcn_d.ghcnd_2023”)
      When user input location, crop type, minimum temperature, 
 maximum temperature, and precipitation
      Then the algorithm returns the yield prediction