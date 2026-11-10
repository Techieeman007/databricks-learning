# IoT Lakehouse

> 🚧 Placeholder. This project hasn't been started yet.

An IoT telemetry pipeline on Databricks using the medallion architecture.

## Planned architecture

| Layer | Purpose |
|-------|---------|
| **Bronze** | Raw device telemetry ingested as-is (e.g. JSON events via Auto Loader) |
| **Silver** | Cleaned, deduplicated, typed readings with schema enforcement |
| **Gold** | Aggregates for analytics, e.g. per-device hourly stats and anomaly flags |

## To do

- [ ] Pick or generate a sample telemetry dataset
- [ ] Bronze ingestion
- [ ] Silver transformations + data quality checks
- [ ] Gold aggregates
- [ ] Orchestrate as a Job / DLT pipeline
