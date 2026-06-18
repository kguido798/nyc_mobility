
CREATE TABLE zones (
    LocationID INT PRIMARY KEY,
    Borough VARCHAR(50) NOT NULL,
    Zone VARCHAR(100) NOT NULL,
    service_zone VARCHAR(100)
);

CREATE TABLE trips (
    trip_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    pickup_datetime TIMESTAMP NOT NULL,
    dropoff_datetime TIMESTAMP NOT NULL,
    pickup_location_id INT NOT NULL,
    dropoff_location_id INT NOT NULL,
    passenger_count INT,
    trip_distance DECIMAL(10,2),
    fare_amount DECIMAL(10,2),
    extra DECIMAL(10,2),
    mta_tax DECIMAL(10,2),
    tip_amount DECIMAL(10,2),
    tolls_amount DECIMAL(10,2),
    improvement_surcharge DECIMAL(10,2),
    congestion_surcharge DECIMAL(10,2),
    airport_fee DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    payment_type INT,
    ratecode_id INT,
    store_and_fwd_flag VARCHAR(1),
    trip_duration_minutes DECIMAL(10,2),
    average_speed DECIMAL(10,2),
    fare_per_mile DECIMAL(10,2),
    rush_hour BOOLEAN,
    FOREIGN KEY (pickup_location_id) REFERENCES zones(LocationID),
    FOREIGN KEY (dropoff_location_id) REFERENCES zones(LocationID)
);