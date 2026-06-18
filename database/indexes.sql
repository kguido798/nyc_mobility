CREATE INDEX idx_pickup_time
ON trips(pickup_datetime);

CREATE INDEX idx_dropoff_time
ON trips(dropoff_datetime);

CREATE INDEX idx_pickup_zone
ON trips(pickup_location_id);

CREATE INDEX idx_dropoff_zone
ON trips(dropoff_location_id);

CREATE INDEX idx_trip_distance
ON trips(trip_distance);

CREATE INDEX idx_total_amount
ON trips(total_amount);