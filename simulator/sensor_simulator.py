import requests
import random
import time

URL = "http://localhost:5000/data"

while True:
    payload = {
        "device_id": "sensor_01",
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2)
    }

    response = requests.post(URL, json=payload)
    print(response.json())

    time.sleep(5)
