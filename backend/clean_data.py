import pandas as pd

df = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")

before = len(df)

df = df.drop_duplicates()
df = df[df["trip_distance"] > 0]
df = df[df["fare_amount"] >= 0]
df = df[
    df["tpep_dropoff_datetime"] >
    df["tpep_pickup_datetime"]
]

after = len(df)

print("Records Before:", before)
print("Records After :", after)

df.to_parquet(
    "data/cleaned_yellow_tripdata_2025_01.parquet",
    index=False
)