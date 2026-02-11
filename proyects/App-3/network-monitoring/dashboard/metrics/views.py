import requests
from django.shortcuts import render

def dashboard(request):
    try:
        response = requests.get("http://processor-service:8000/metrics", timeout=1)
        data = response.json()
    except Exception:
        # Datos mock si el procesador no está disponible
        data = {
            "global_latency_avg": 42,
            "top_failing_antennas": [
                {"id": "ANT-1", "loss": 12},
                {"id": "ANT-3", "loss": 9},
            ],
        }

    return render(request, "dashboard.html", {"data": data})
