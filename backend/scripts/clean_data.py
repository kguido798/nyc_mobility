import pandas as pd

def clean_dataset(df):

    df = df.drop_duplicates()

    df = df.dropna()

    df = df[df["trip_distance"] > 0]

    df = df[df["trip_distance"] < 100]

    df = df[df["fare_amount"] > 0]

    return df