import redis
import os
import time
import random
import json

REDIS_HOST = os.getenv("REDIS_HOST", "redis-service")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

antenna_id = os.getenv("HOSTNAME", "unknown")

print(f"Simulator started for antenna: {antenna_id}")

while True:
    packets = random.randint(100, 500)
    loss = random.randint(0, 50)
    latency = random.uniform(10, 100)

    message = {
        "antenna_id": antenna_id,
        "timestamp": int(time.time()),
        "packets": packets,
        "loss": loss,
        "latency": round(latency, 2)
    }

    r.xadd("antenna_stream", message, maxlen=10000)

    print(f"Sent: {message}")

    time.sleep(5)
