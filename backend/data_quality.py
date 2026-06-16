import pandas as pd

df = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")

print("===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())