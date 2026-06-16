import pandas as pd
from sqlalchemy import create_engine

# Read integrated dataset
df = pd.read_parquet(
    "data/final_integrated_tripdata.parquet"
)

# Rename columns to match MySQL table
df = df.rename(columns={
    "tpep_pickup_datetime": "pickup_time",
    "tpep_dropoff_datetime": "dropoff_time"
})

# Keep only columns that exist in trips table
df = df[
    [
        "VendorID",
        "pickup_time",
        "dropoff_time",
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "fare_amount",
        "total_amount",
        "duration_minutes",
        "avg_speed",
        "revenue_per_mile",
        "pickup_hour",
        "day_of_week",
        "is_weekend"
    ]
]

engine = create_engine(
    "mysql+pymysql://root:123321@localhost/nyc_mobility"
)

df.to_sql(
    "trips",
    engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

print("Trips loaded successfully!")