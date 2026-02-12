from fastapi import FastAPI
from threading import Thread
from spark_job import run_spark
from state import metrics

app = FastAPI()


@app.on_event("startup")
def startup_event():
    thread = Thread(target=run_spark, daemon=True)
    thread.start()


@app.get("/metrics")
def get_metrics():
    return metrics
