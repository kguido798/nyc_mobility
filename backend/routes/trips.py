from flask import Blueprint, jsonify, request
from db import get_connection

trips_bp = Blueprint("trips", __name__)

# GET all trips (pagination)
@trips_bp.route("/", methods=["GET"])
def get_trips():
    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM trips
        LIMIT %s OFFSET %s
    """, (limit, offset))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)


# GET single trip
@trips_bp.route("/<int:trip_id>", methods=["GET"])
def get_trip(trip_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM trips WHERE id = %s", (trip_id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return jsonify({"message": "Trip not found"}), 404

    return jsonify(row)