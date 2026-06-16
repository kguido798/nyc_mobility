import pandas as pd

df = pd.read_parquet("data/final_integrated_tripdata.parquet")

df.to_csv(
    "data/final_integrated_tripdata.csv",
    index=False
)

print("CSV created successfully!")