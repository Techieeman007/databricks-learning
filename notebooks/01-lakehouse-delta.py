# Databricks notebook source
# MAGIC %md
# MAGIC # Day 1: Lakehouse & Delta Lake
# MAGIC Fake IoT telemetry → Delta files in a volume → inspect `_delta_log/` → UPDATE/DELETE → history and time travel.
# MAGIC Notes: `notes/01-lakehouse.md`

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC SELECT * FROM samples.nyctaxi.trips LIMIT 10;

# COMMAND ----------

from pyspark.sql import functions as F

df = (spark.range(1000)
  .withColumn("device_id", F.concat(F.lit("sensor-"), (F.col("id") % 5).cast("string")))
  .withColumn("ts", F.expr("timestampadd(MINUTE, -cast(id AS INT), current_timestamp())"))
  .withColumn("temperature", F.round(20 + F.rand() * 15, 2))
  .withColumn("humidity", F.round(40 + F.rand() * 30, 2))
  .drop("id"))

display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.default.lab;
# MAGIC

# COMMAND ----------

path = "/Volumes/workspace/default/lab/iot_raw"
df.write.format("delta").mode("overwrite").save(path)

display(dbutils.fs.ls(path))
display(dbutils.fs.ls(path + "/_delta_log"))


# COMMAND ----------

display(spark.read.text(path + "/_delta_log/00000000000000000000.json"))



# COMMAND ----------

df.write.mode("overwrite").saveAsTable("workspace.default.iot_bronze")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Pretend sensor-3 was miscalibrated, and drop the sensor-4 data
# MAGIC UPDATE workspace.default.iot_bronze SET temperature = temperature - 2 WHERE device_id = 'sensor-3';
# MAGIC DELETE FROM workspace.default.iot_bronze WHERE device_id = 'sensor-4';
# MAGIC
# MAGIC DESCRIBE HISTORY workspace.default.iot_bronze;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT device_id, COUNT(*) AS n, ROUND(AVG(temperature), 2) AS avg_temp
# MAGIC FROM workspace.default.iot_bronze VERSION AS OF 0
# MAGIC GROUP BY device_id ORDER BY device_id;

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE delta.`/Volumes/workspace/default/lab/iot_raw`
# MAGIC SET temperature = temperature - 2 WHERE device_id = 'sensor-3';
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls(path + "/_delta_log"))
display(spark.read.text(path + "/_delta_log/00000000000000000001.json"))
display(dbutils.fs.ls(path))


# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/Volumes/workspace/default/lab/iot_raw`;
# MAGIC