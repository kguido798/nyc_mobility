import os
import pandas as pd
from sqlalchemy import create_engine

from clean_data import clean_dataset

from feature_engineering import (
    create_trip_duration,
    create_average_speed,
    create_fare_per_mile,
    create_rush_hour
)

DATABASE_URL = (
    "postgresql://postgres:password@localhost/nyc_taxi"
)

engine = create_engine(DATABASE_URL)

df = pd.read_parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

df = clean_dataset(df)

df = create_trip_duration(df)

df = create_average_speed(df)

df = create_fare_per_mile(df)

df = create_rush_hour(df)

df.to_sql(
    "trips",
    engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully.")