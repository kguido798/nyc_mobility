import pandas as pd

raw = pd.read_parquet("data/yellow_tripdata_2025-01.parquet")
clean = pd.read_parquet("data/cleaned_yellow_tripdata_2025_01.parquet")

print("Raw Records:", len(raw))
print("Clean Records:", len(clean))
print("Removed Records:", len(raw) - len(clean))