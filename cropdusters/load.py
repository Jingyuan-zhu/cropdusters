import pandas as pd
import duckdb
import json 

def load_crop_price_into_db()-> None:
    """Load all files in the data directory into the database."""
    with open('/workspaces/cropdusters_PR2/cropdusters/crop_yield_data.json', 'r') as json_file:
        data = json.load(json_file)

    duckb = duckdb.connect('dev.duckdb')

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
    with open('/workspaces/cropdusters_PR2/cropdusters/crop_chooser_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Initialize a DuckDB connection
    duckb = duckdb.connect('dev.duckdb')

    # # Check if the table 'crop_yield' exists, and create it if not
    check_table_sql = "SELECT count(*) AS count FROM information_schema.tables WHERE table_name = 'crop_price'"
    table_exists = duckb.execute(check_table_sql).fetchone()[0] > 0

    if not table_exists:
        create_table_sql = """
        CREATE TABLE crop_price (
            Symbol VARCHAR,
            date DATE,
            close DECIMAL
            )
        """
        duckb.execute(create_table_sql)

    if "Monthly Time Series" in data:
        monthly_data = data["Monthly Time Series"]
        for date, values in monthly_data.items():
            symbol = "CORN"
            close_value = values.get("4. close")
            if close_value:
                insert_data_sql = """
                INSERT INTO crop_price (Symbol, date, close)
                VALUES (?, ?, ?)
                """
                values = (symbol, date, float(close_value))
                duckb.execute(insert_data_sql, values)

        duckb.commit()
        result = duckb.execute("SELECT * FROM crop_price")
        print(result.fetch_df())
    else:
        print("The JSON data does not match the expected format.")

def load_weather_into_db() -> None:
    with open('/workspaces/cropdusters_PR2/cropdusters/weather_data.json', 'r') as json_file:
        data = json.load(json_file)

    # Initialize a DuckDB connection with an in-memory database
    duckb = duckdb.connect('dev.duckdb')

    # Check if the table 'crop_price' exists, and create it if not
    check_table_sql = "SELECT count(*) AS count FROM information_schema.tables WHERE table_name = 'crop_weather'"
    table_exists = duckb.execute(check_table_sql).fetchone()[0] > 0
    if not table_exists:
        create_table_sql = """
        CREATE TABLE crop_weather (
            time VARCHAR,
            tmin DECIMAL,
            tmax DECIMAL,
            precipitation DECIMAL,
            latitude DECIMAL,
            longitude DECIMAL,
        )
        """
        duckb.execute(create_table_sql)

    for time, weather in data.items():
        tmax = weather["tmax"]
        tmin = weather["tmin"]
        precipitation = weather["precipitation"]
        latitude = weather["latitude"]
        longitude = weather["longitude"]

        insert_data_sql = """
        INSERT INTO crop_weather (time,tmin,tmax,precipitation,latitude,longitude)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (time, tmin,tmax,precipitation, latitude, longitude)
        duckb.execute(insert_data_sql, values)

        duckb.commit()

    result = duckb.execute("SELECT * FROM crop_weather")
    print(result.fetch_df())

# Remove all tables if changing schema
def delete_tables():
    duckb = duckdb.connect('dev.duckdb')
    duckb.execute("DROP TABLE crop_price")
    duckb.execute("DROP TABLE crop_yield")
    duckb.execute("DROP TABLE crop_weather")


load_weather_into_db()
load_crop_chooser_into_db()
load_crop_price_into_db()






