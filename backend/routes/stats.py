from flask import Blueprint, jsonify, request
from db import get_connection

stats_bp = Blueprint("stats", __name__)

# Summary stats
@stats_bp.route("/summary", methods=["GET"])
def summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            COUNT(*) as totalTrips,
            AVG(fare_amount) as averageFare,
            AVG(trip_distance) as averageDistance,
            SUM(fare_amount) as totalRevenue
        FROM trips
    """)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(result)


# Top pickup zones
@stats_bp.route("/top-pickups", methods=["GET"])
def top_pickups():
    limit = int(request.args.get("limit", 10))

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT pickup_location_id, COUNT(*) as trip_count
        FROM trips
        GROUP BY pickup_location_id
        ORDER BY trip_count DESC
        LIMIT %s
    """, (limit,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)