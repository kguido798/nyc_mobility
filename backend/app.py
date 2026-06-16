from flask import Flask, jsonify
from flask_cors import CORS

from routes.trips import trips_bp
from routes.stats import stats_bp

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(trips_bp, url_prefix="/api/trips")
app.register_blueprint(stats_bp, url_prefix="/api/stats")

@app.route("/")
def home():
    return jsonify({"message": "NYC Mobility API running"})

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)