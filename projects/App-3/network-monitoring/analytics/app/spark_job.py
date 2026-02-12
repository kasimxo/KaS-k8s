import random
import time
from pyspark.sql import SparkSession
from state import metrics, lock


def run_spark():
    spark = SparkSession.builder \
        .appName("Analytics") \
        .master("local[*]") \
        .getOrCreate()

    print("Spark started")

    total_latency = 0
    count = 0

    while True:
        # Simulación de datos
        latency = random.randint(10, 100)

        total_latency += latency
        count += 1

        avg = total_latency / count

        with lock:
            metrics["global_latency_avg"] = round(avg, 2)
            metrics["messages_processed"] = count

        time.sleep(1)
