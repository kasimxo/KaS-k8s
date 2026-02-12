from threading import Lock

metrics = {
    "global_latency_avg": 0,
    "messages_processed": 0,
}

lock = Lock()
