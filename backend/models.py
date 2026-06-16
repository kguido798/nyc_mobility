from database import db

class Zone(db.Model):

    __tablename__ = "zones"

    location_id = db.Column(db.Integer, primary_key=True)

    borough = db.Column(db.String(50))

    zone_name = db.Column(db.String(100))

    service_zone = db.Column(db.String(100))


class Trip(db.Model):

    __tablename__ = "trips"

    trip_id = db.Column(db.BigInteger, primary_key=True)

    pickup_datetime = db.Column(db.DateTime)

    dropoff_datetime = db.Column(db.DateTime)

    pickup_location_id = db.Column(
        db.Integer,
        db.ForeignKey("zones.location_id")
    )

    dropoff_location_id = db.Column(
        db.Integer,
        db.ForeignKey("zones.location_id")
    )

    passenger_count = db.Column(db.Integer)

    trip_distance = db.Column(db.Float)

    fare_amount = db.Column(db.Float)

    tip_amount = db.Column(db.Float)

    total_amount = db.Column(db.Float)

    trip_duration_minutes = db.Column(db.Float)

    average_speed = db.Column(db.Float)

    fare_per_mile = db.Column(db.Float)

    rush_hour = db.Column(db.Boolean)