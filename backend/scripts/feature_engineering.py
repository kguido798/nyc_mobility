def create_trip_duration(df):

    df["trip_duration_minutes"] = (
        (
            df["tpep_dropoff_datetime"]
            -
            df["tpep_pickup_datetime"]
        )
        .dt.total_seconds()
        / 60
    )

    return df


def create_average_speed(df):

    df["average_speed"] = (
        df["trip_distance"]
        /
        (df["trip_duration_minutes"] / 60)
    )

    return df


def create_fare_per_mile(df):

    df["fare_per_mile"] = (
        df["fare_amount"]
        /
        df["trip_distance"]
    )

    return df


def create_rush_hour(df):

    hours = df["tpep_pickup_datetime"].dt.hour

    df["rush_hour"] = (
        ((hours >= 7) & (hours <= 10))
        |
        ((hours >= 16) & (hours <= 19))
    )

    return df