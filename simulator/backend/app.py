from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

CSV_FILE = "sensor_data.csv"

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["timestamp"],
            data["temperature"],
            data["humidity"]
        ])

    return jsonify({"status": "success"}), 200


@app.route("/data", methods=["GET"])
def get_data():
    records = []
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        pass

    return jsonify(records)
    

if __name__ == "__main__":
    app.run(debug=True)
