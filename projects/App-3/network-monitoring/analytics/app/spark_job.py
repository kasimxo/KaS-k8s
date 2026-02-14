from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as spark_sum, avg, countDistinct, col
import threading
import time

from redis_consumer import read_batch
from state import metrics_state

spark = SparkSession.builder \
    .appName("AnalyticsJob") \
    .getOrCreate()

def process_batch(batch):
    if not batch:
        return

    df = spark.createDataFrame(batch)

    df = (
        df.withColumn("packets", col("packets").cast("int"))
        .withColumn("loss", col("loss").cast("int"))
        .withColumn("latency", col("latency").cast("double"))
    )

    # Estadísticas globales (sin groupBy)
    stats = df.agg(
        spark_sum("packets").alias("total_packets"),
        spark_sum("loss").alias("total_loss"),
        avg("latency").alias("avg_latency"),
        countDistinct("antenna_id").alias("active_antennas")
    )

    row = stats.collect()[0]

    loss_rate = (
        row["total_loss"] / row["total_packets"]
        if row["total_packets"] > 0 else 0
    )

    result = {
        "total_packets": row["total_packets"],
        "total_loss": row["total_loss"],
        "loss_rate": loss_rate,
        "avg_latency": row["avg_latency"],
        "active_antennas": row["active_antennas"],
    }

    metrics_state["service_stats"] = result
    metrics_state["last_update"] = time.time()

def spark_loop():
    while True:
        batch = read_batch()
        process_batch(batch)
        time.sleep(5)

def start_background_job():
    thread = threading.Thread(target=spark_loop, daemon=True)
    thread.start()
