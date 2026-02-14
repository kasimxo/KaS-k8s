from threading import Lock

metrics_state = {
    "last_update": None,
    "service_stats": {}
}

lock = Lock()
