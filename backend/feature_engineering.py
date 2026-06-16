import pandas as pd

df = pd.read_parquet("data/cleaned_yellow_tripdata_2025_01.parquet")

# Feature 1: Trip Duration
df["duration_minutes"] = (
    df["tpep_dropoff_datetime"] -
    df["tpep_pickup_datetime"]
).dt.total_seconds() / 60

# Feature 2: Average Speed
df["avg_speed"] = (
    df["trip_distance"] /
    (df["duration_minutes"] / 60)
)

# Feature 3: Revenue Per Mile
df["revenue_per_mile"] = (
    df["total_amount"] /
    df["trip_distance"]
)

# Optional bonus features
df["pickup_hour"] = df["tpep_pickup_datetime"].dt.hour

df["day_of_week"] = df["tpep_pickup_datetime"].dt.day_name()

df["is_weekend"] = (
    df["tpep_pickup_datetime"].dt.dayofweek >= 5
)

df.to_parquet(
    "data/final_tripdata.parquet",
    index=False
)

print("Features created successfully!")

print(df[
    [
        "duration_minutes",
        "avg_speed",
        "revenue_per_mile",
        "pickup_hour",
        "day_of_week"
    ]
].head())