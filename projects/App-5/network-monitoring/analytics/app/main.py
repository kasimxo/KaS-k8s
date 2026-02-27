import logging
from fastapi import FastAPI
from spark_job import start_background_job
from state import metrics_state

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Arranca el job en background al iniciar la app
start_background_job()
logger.info("Analytics service started and background Spark job launched")

@app.get("/metrics")
def get_metrics():
    try:
        service_stats = metrics_state.get("service_stats", {})
        last_update = metrics_state.get("last_update")

        if service_stats:
            logger.info(
                "Metrics requested | packets=%s | loss_rate=%.4f | avg_latency=%.2f | antennas=%s | last_update=%s",
                service_stats.get("total_packets", 0),
                service_stats.get("loss_rate", 0.0),
                service_stats.get("avg_latency", 0.0),
                service_stats.get("active_antennas", 0),
                last_update,
            )
        else:
            logger.info("Metrics requested | no data yet | last_update=%s", last_update)

        return metrics_state

    except Exception as e:
        logger.exception("Error while serving /metrics endpoint")
        raise
