import pandas as pd

df = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")

print("===== DATA QUALITY REPORT =====")
print("Total Records:", len(df))
print()

print("Missing Values:")
print(df.isnull().sum())
print()

print("Duplicate Records:", df.duplicated().sum())

print("Negative Distances:",
      (df["trip_distance"] < 0).sum())

print("Negative Fares:",
      (df["fare_amount"] < 0).sum())

print("Pickup After Dropoff:",
      (
          df["tpep_dropoff_datetime"] <
          df["tpep_pickup_datetime"]
      ).sum())