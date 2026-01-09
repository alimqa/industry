from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

sensor_data = []

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    record = {
        "device_id": data.get("device_id"),
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
        "timestamp": datetime.utcnow().isoformat()
    }

    sensor_data.append(record)

    return jsonify({"status": "success", "data": record}), 200

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(sensor_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
