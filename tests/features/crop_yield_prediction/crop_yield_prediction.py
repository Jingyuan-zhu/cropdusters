#Backgroud
@given('we can obtain corp yields and weather data')
def get_crop_yield():
    return crop_dusters.get_data("API")

def get_weather_data():
    weather_table = crop_dusters.load_data("bigquery-public-data:ghcn_d.ghcnd_2023") # assume we import table from BigQuery
    con = duckdb.connect(database='database.db')    
    weather_data = “””SELECT
        wx.date,
        MAX(prcp) AS prcp,
        MAX(tmin) AS tmin,
        MAX(tmax) AS tmax,
        IF(MAX(haswx) = 'True', 'True', 'False') AS haswx
        FROM (
        SELECT
            wx.date,
            IF (wx.element = 'PRCP', wx.value/10, NULL) AS prcp,
            IF (wx.element = 'TMIN', wx.value/10, NULL) AS tmin,
            IF (wx.element = 'TMAX', wx.value/10, NULL) AS tmax,
            IF (SUBSTR(wx.element, 0, 2) = 'WT', 'True', NULL) AS haswx
        FROM
            [weather_table] AS wx
        WHERE
            id = 'USW00094846'(States Name)
            AND qflag IS NULL )
        GROUP BY
        wx.date
        ORDER BY
        Wx.date”””
    result = con.execute(weather_data)
    result_data = result.fetchdf() # Suppose we need to use some SQL to obtain the data we want
    return result_data

#Scenario1
@given('we can obtain crop yield and weather data')
	yield_row = get_crop_yield()
	weather_row = get_weather_data()

@when('user inputs location and crop type')
	yiled = crop_dusters.yield(location= ‘st. louis’, crop_type= ‘corn’ )

@then('display the yield in 3D plot')
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import pandas as pd
    crop_types = ['Corn', 'Wheat', 'Soybean']
    locations = ['Missouri', 'New York', 'Califormnia']
    data = pd.DataFrame({'CropType': crop_type_data, 'Location': location_data, 'CropYield': crop_yield_data})

    # Create a 3D scatter plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Map crop type and location to numerical values for plotting
    crop_type_mapping = {crop_type: i for i, crop_type in enumerate(crop_types)}
    location_mapping = {location: i for i, location in enumerate(locations)}
    data['CropTypeIndex'] = data['CropType'].map(crop_type_mapping)
    data['LocationIndex'] = data['Location'].map(location_mapping)

    # Scatter plot
    scatter = ax.scatter(data['CropTypeIndex'], data['LocationIndex'], data['CropYield'], c=data['CropYield'], cmap='viridis')
    ax.set_xlabel('Crop Type')
    ax.set_ylabel('Location')
    ax.set_zlabel('Crop Yield')

#Scenario2
@given('we can obtain crop yield and weather data. We reorganize the data into a trainable data set for the ML model')
    weather_data = get_crop_yield()
    crop_yield = get_weather_data()
    data_ML = crop_dusters.organize(weather_data, crop_yield)

@when('user inputs location and crop type')
	prediction = crop_dusters.predict(location= ‘Missouri’, crop_type= ‘corn’, min_temp=15, max_temp=30, prcp=15)

@then('the algorithm returns the prediction for the corp yields')
    model.train(train_data)
    y_predict = model.test(test_data)
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.title('Actual vs. Predicted Crop Yields')
    plt.xlabel('Actual Crop Yields')
    plt.ylabel('Predicted Crop Yields')
    plt.grid(True)
    plt.show()

