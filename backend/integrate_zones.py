import pandas as pd

trips = pd.read_parquet("data/final_tripdata.parquet")

zones = pd.read_csv("data/taxi_zone_lookup.csv")

# Pickup zone information
pickup_zones = zones.rename(columns={
    "LocationID": "PULocationID",
    "Borough": "pickup_borough",
    "Zone": "pickup_zone"
})

# Dropoff zone information
dropoff_zones = zones.rename(columns={
    "LocationID": "DOLocationID",
    "Borough": "dropoff_borough",
    "Zone": "dropoff_zone"
})

trips = trips.merge(
    pickup_zones[
        ["PULocationID", "pickup_borough", "pickup_zone"]
    ],
    on="PULocationID",
    how="left"
)

trips = trips.merge(
    dropoff_zones[
        ["DOLocationID", "dropoff_borough", "dropoff_zone"]
    ],
    on="DOLocationID",
    how="left"
)

print(trips[
    [
        "PULocationID",
        "pickup_borough",
        "pickup_zone"
    ]
].head())

trips.to_parquet(
    "data/final_integrated_tripdata.parquet",
    index=False
)

print("Integration complete.")