# Lakehouse & Delta Lake

Day 1 · Tue, Nov 10, 2026 · Hands-on: [notebooks/01-lakehouse-delta.py](../notebooks/01-lakehouse-delta.py)

## Key ideas

**Lake vs warehouse vs lakehouse**
- **Warehouse:** schema-on-write, ACID, fast SQL. But it's expensive and poor at handling raw, semi-structured or ML data.
- **Data lake:** cheap object storage that takes any format. But it has no transactions, and it easily turns into a "data swamp".
- Companies ran **both** and copied data from the lake into the warehouse. That meant two copies, ETL pipelines that broke, stale data, and two sets of access controls.
- **Lakehouse:** open files in cheap storage, plus a **table layer** that adds transactions, schemas and governance. One copy of the data serves both BI and ML.

**What a Delta table is on disk**
- A folder of **Parquet** files (the data), plus a `_delta_log/` folder of numbered **JSON commits** (`000…000.json`, `000…001.json`, …).
- Each commit lists **actions**: `commitInfo` (who/what/when), `metaData` (schema), `protocol` (required features), and `add`/`remove` (which files are in the table).
- Readers use the **log** to decide which files make up the table, not the folder listing. A commit is written all at once, so readers never see half-finished writes. That's how Delta gets **ACID** on object storage.
- My first write produced **8 Parquet files** because Spark ran it as 8 parallel tasks (more on this on Day 2).

**Updates never edit files in place**
- My `UPDATE` (200 rows of sensor-3) did **not** rewrite the 8 files. With **deletion vectors**, it:
  1. wrote the 200 updated rows into **1 new Parquet file**, and
  2. re-added the 8 old files with a small **deletion vector** (a `.bin` file) that marks the old sensor-3 rows as deleted.
- Metrics from the commit: `numAddedFiles: 1`, `numDeletionVectorsAdded: 8`, `numRemovedFiles: 0`.

**Time travel**
- Old Parquet files stay on disk, and old log versions still point to them, so `VERSION AS OF 0` reads the table as it was.
- `DESCRIBE HISTORY <table>` shows every version, operation and metric.
- Old files are only physically deleted by `VACUUM`, after the retention period (7 days by default).

**Databricks does housekeeping for you (auto-compaction)**
- Right after my UPDATE, a **second commit** appeared: `OPTIMIZE` with `auto -> true`. It compacted 9 files + 8 deletion vectors into **1 file**.
- **Gotcha:** `userName` in the history shows *me* even for automatic operations. Check the `operation` column and `operationParameters.auto` to see what really happened.

**What Databricks adds on top of Spark**
- Managed compute (serverless), Delta with automatic optimisation, Unity Catalog (`catalog.schema.table`, volumes), notebooks, Jobs/Lakeflow, Databricks SQL, MLflow/Mosaic AI, and Genie.

**IoT mapping**
- **Bronze:** raw MQTT JSON → **Silver:** parsed, deduped, validated → **Gold:** hourly KPIs and anomalies.

## In my words

- **Step 3:** I learned to create a storage folder (a volume), how to write data as Delta files, how to list them and view them, and how to display the data using Spark.
- **Version 2 puzzle:** I thought version 2 was me. It was actually Databricks auto-compaction (`OPTIMIZE`, `auto -> true`), triggered by my UPDATE.
- *TODO, in my own words:* after an UPDATE, are the old Parquet files changed? What happens instead?
- *TODO:* why does that make time travel possible, and what deletes old files?
- *TODO:* why did companies run both a lake and a warehouse, and what problem did that cause?
- *TODO:* if I can run Spark myself, what am I paying Databricks for?

## Questions

- When exactly does auto-compaction trigger, and can I control it per table?
- Deletion vectors vs rewriting files: when is each better (read speed vs write speed)?
- What is `_delta_log/_staged_commits/`? (Related to catalog-managed commits?)
- How do Delta tables behave with a high-frequency IoT stream (many small appends)?
- Still to try: run the Step 5 query **without** `VERSION AS OF 0` and compare with version 0.
