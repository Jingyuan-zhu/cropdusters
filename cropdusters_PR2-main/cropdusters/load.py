"""Load data from local json folder into DuckDB database."""
import pandas as pd
import duckdb
import json 

#load the data file
with open('crop_yield_data.json', 'r') as json_file:
    data = json.load(json_file)

def load_files_into_db(data)-> None:
    """Load all files in the data directory into the database."""

    duckb = duckdb.connect('transform/dev.duckdb')

    if isinstance(data, dict) and "data" in data:
        records = data["data"]

        check_table_sql = "SELECT count(*) AS count FROM information_schema.tables WHERE table_name = 'crop_yield'"
        table_exists = duckb.execute(check_table_sql).fetchone()[0]>0

        if not table_exists:
            create_table_sql = """
            CREATE TABLE crop_yield (
                state_alpha VARCHAR,
                "Value" VARCHAR,
                "year" INTEGER,
                commodity_desc VARCHAR
            )
            """
            duckb.execute(create_table_sql)

        for record in records:
            state_alpha = record.get("state_alpha", '')
            Value = record.get("Value", '')
            year = int(record.get("year", 0)) if record.get("year") else 0
            commodity_desc = record.get("commodity_desc", '')

            insert_data_sql = """
            INSERT INTO crop_yield (state_alpha, "Value", "year", commodity_desc)
            VALUES (?, ?, ?, ?)
            """
            values = (state_alpha, Value, year, commodity_desc)
            duckb.execute(insert_data_sql, values)

        duckb.commit()

        result = duckb.execute("SELECT * FROM crop_yield")
        print(result.fetch_df())
    else:
        print("The JSON data does not match the expected format.")


def load_crop_chooser_into_db()-> None:
    with open('crop_chooser_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Initialize a DuckDB connection
    duckb = duckdb.connect('transform/dev.duckdb')

    # # Check if the table 'crop_yield' exists, and create it if not
    check_table_sql = "SELECT count(*) AS count FROM information_schema.tables WHERE table_name = 'crop_yield'"
    table_exists = duckb.execute(check_table_sql).fetchone()[0] > 0

    if not table_exists:
        create_table_sql = """
        CREATE TABLE crop_yield (
            Symbol VARCHAR,
            date DATE,
            close DECIMAL
            )
        """
        duckb.execute(create_table_sql)

    # Extract data and insert it into the DuckDB table
    if "Monthly Time Series" in data:
        monthly_data = data["Monthly Time Series"]
        for date, values in monthly_data.items():
            symbol = "CORN"
            close_value = values.get("4. close")
            if close_value:
                insert_data_sql = """
                INSERT INTO crop_yield (Symbol, date, close)
                VALUES (?, ?, ?)
                """
                values = (symbol, date, float(close_value))
                duckb.execute(insert_data_sql, values)

        duckb.commit()

        result = duckb.execute("SELECT * FROM crop_yield")
        print(result.fetch_df())
    else:
        print("The JSON data does not match the expected format.")

def load_weather_into_db() -> None:
    with open('weather_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Initialize a DuckDB connection with an in-memory database (not read-only)
    duckb = duckdb.connect('transform/dev.duckdb')

    # Check if the table 'crop_price' exists, and create it if not
    check_table_sql = "SELECT count(*) AS count FROM information_schema.tables WHERE table_name = 'crop_price'"
    table_exists = duckb.execute(check_table_sql).fetchone()[0] > 0
  

    if not table_exists:
        create_table_sql = """
        CREATE TABLE crop_price (
            time VARCHAR,
            temperature_2m_max DECIMAL,
            temperature_2m_min DECIMAL,
            precipitation_sum DECIMAL,
            precipitation_hours DECIMAL,
            cloudcover INT,
            windspeed_10m DECIMAL,
            soil_temperature_0cm DECIMAL,
            soil_moisture_0_to_1cm DECIMAL
        )
        """
        duckb.execute(create_table_sql)

    # Extract hourly data and insert it into the DuckDB table
    if "hourly" in data:
        hourly_data = data["hourly"]
        for i in range(len(hourly_data['time'])):
            time = hourly_data['time'][i]
            temperature_2m_max = float(hourly_data['temperature_2m'][i]) if hourly_data['temperature_2m'][i] else None
            temperature_2m_min = None  # No minimum temperature available in the hourly data

            precipitation_sum = float(hourly_data['precipitation'][i]) if hourly_data['precipitation'][i] else None
            precipitation_hours = None  # No precipitation hours available in the hourly data
            cloudcover = int(hourly_data['cloudcover'][i]) if hourly_data['cloudcover'][i] else None
            windspeed_10m = float(hourly_data['windspeed_10m'][i]) if hourly_data['windspeed_10m'][i] else None
            soil_temperature_0cm = float(hourly_data['soil_temperature_0cm'][i]) if hourly_data['soil_temperature_0cm'][i] else None
            soil_moisture_0_to_1cm = float(hourly_data['soil_moisture_0_to_1cm'][i]) if hourly_data['soil_moisture_0_to_1cm'][i] else None

            insert_data_sql = """
            INSERT INTO crop_price (time, temperature_2m_max, temperature_2m_min, precipitation_sum, precipitation_hours, cloudcover, windspeed_10m, soil_temperature_0cm, soil_moisture_0_to_1cm)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            values = (time, temperature_2m_max, temperature_2m_min, precipitation_sum, precipitation_hours, cloudcover, windspeed_10m, soil_temperature_0cm, soil_moisture_0_to_1cm)
            duckb.execute(insert_data_sql, values)

        duckb.commit()

        result = duckb.execute("SELECT * FROM crop_price")
        print(result.fetch_df())
    else:
        print("The JSON data does not match the expected format.")

# Call the function to load daily crop price data into the database
load_weather_into_db()







