import logging
import requests
from django.shortcuts import render

logger = logging.getLogger(__name__)

def dashboard(request):
    try:
        response = requests.get(
            "http://analytics-service:8000/metrics",
            timeout=1
        )

        logger.info("Analytics response status: %s", response.status_code)

        data = response.json()

        logger.info("Analytics payload: %s", data)

    except Exception as e:
        logger.exception("Error fetching metrics from analytics-service")

        data = {
            "error": "Could not fetch data from server"
        }

    return render(request, "dashboard.html", {"data": data})
