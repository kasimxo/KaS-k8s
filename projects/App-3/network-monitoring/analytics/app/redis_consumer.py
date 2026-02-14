import redis
import os
import json

REDIS_HOST = os.getenv("REDIS_HOST", "redis-service")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

STREAM_NAME = "antenna_stream"

last_id = "0-0"

def read_batch(count=100):
    global last_id

    messages = r.xread(
        {STREAM_NAME: last_id},
        count=count,
        block=2000
    )

    batch = []

    for stream, entries in messages:
        for msg_id, data in entries:
            batch.append(data)
            last_id = msg_id

    return batch
