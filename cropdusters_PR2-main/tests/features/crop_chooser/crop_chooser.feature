Feature: crop_comparison
 	This feature aims to inform users what crop is most suited for their location. Using this feature farmers and analysts 
  will be able to predict the best crops to plant in order to be successful based on a dataset of known crop growing conditions 
  and the typical conditions at your location. 

Background:
 	Given we have obtained data on crop yields for areas in the US (National Agriculture Statistics Survey - US DoA)
		crop_dusters.get_data(“API_LINK”)

Scenario: Display your profits vs. theoretical profits
    Given We have the market value of the crops (Commodity prices available from many API’s on a monthly basis including futures)
		      crop_dusters.get_data(“API_LINK”)
    When the user enters their location, land area, and crop type 
          crop_dusters.estimate_profit(location= ‘st. louis’, area=1, crop_type= ‘corn’ )
    Then  we can estimate their profits for all crops (bar chart showing revenues by crop type)
		
Scenario: Display crop advantages for a given region
    Given we have computed statistics comparing crop yield in one area vs state/us average 
    When the user selects a region
    Then user sees a yield comparison which tells them what plants are most productive for their location 
         (Histogram showing a measure of productivity like harvested kg)