import requests
import random
import time
from datetime import datetime

BACKEND_URL = "http://localhost:5000/data"

while True:
    data = {
        "temperature": round(random.uniform(18, 30), 2),
        "humidity": round(random.uniform(40, 70), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        response = requests.post(BACKEND_URL, json=data)
        print("Sent:", data, "Status:", response.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(5)
