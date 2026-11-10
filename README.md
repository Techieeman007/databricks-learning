# Databricks Learning — Techieeman

My learning log for Databricks, covering both data engineering and AI/ML. The goal is to understand the lakehouse architecture, get comfortable with Spark and the Databricks platform (Unity Catalog, Jobs, Delta Live Tables), and use it for ML/AI work (MLflow, Feature Store, Model Serving, Mosaic AI). Along the way I'm building small end-to-end projects in Databricks Free Edition and writing down what I learn in my own words.

## Progress

### Meetup sprint (Nov 10–13, 2026)

Prep for the [Databricks User Group Coimbatore meetup on Sat, Nov 14](meetup/2026-11-14-coimbatore.md).

| Day | Date | Focus | Notes | Status |
|-----|------|-------|-------|--------|
| 1 | Tue, Nov 10 | Lake vs warehouse vs lakehouse; what Databricks adds over Spark; Delta Lake basics | [01-lakehouse.md](notes/01-lakehouse.md) | ✅ Done |
| 2 | Wed, Nov 11 | Spark architecture, DataFrames, transformations vs actions, first PySpark notebook | [02-spark.md](notes/02-spark.md) | ⬜ Not started |
| 3 | Thu, Nov 12 | Workspace, compute, Delta (ACID, time travel), Unity Catalog, Databricks SQL, Lakeflow/Jobs | [03-platform.md](notes/03-platform.md) | ⬜ Not started |
| 4 | Fri, Nov 13 | MLflow + model lifecycle, Mosaic AI, Genie; finalize meetup questions | [04-ai-ml.md](notes/04-ai-ml.md) | ⬜ Not started |
| — | Sat, Nov 14 | Databricks User Group Coimbatore meetup | [meetup notes](meetup/2026-11-14-coimbatore.md) | ⬜ Upcoming |

### Learning phases

| Phase | Topic | Notes | Status |
|-------|-------|-------|--------|
| 1 | Lakehouse & Delta Lake | [01-lakehouse.md](notes/01-lakehouse.md) | 🟨 In progress |
| 2 | Apache Spark on Databricks | [02-spark.md](notes/02-spark.md) | ⬜ Not started |
| 3 | Platform: Unity Catalog, Workflows, DLT | [03-platform.md](notes/03-platform.md) | ⬜ Not started |
| 4 | AI/ML: MLflow, Feature Store, Model Serving | [04-ai-ml.md](notes/04-ai-ml.md) | ⬜ Not started |
| 5 | Capstone: end-to-end project | [projects/](projects/) | ⬜ Not started |

Status key: ⬜ Not started · 🟨 In progress · ✅ Done

## Repo layout

- [notes/](notes/) — concept notes per phase
- [notebooks/](notebooks/) — notebooks exported from Databricks (e.g. [Day 1](notebooks/01-lakehouse-delta.py))
- [projects/](projects/) — hands-on projects
- [meetup/](meetup/) — meetup prep and takeaways

## Projects

| Project | Description | Status |
|---------|-------------|--------|
| [iot-lakehouse](projects/iot-lakehouse/) | IoT telemetry pipeline using the medallion architecture (bronze → silver → gold) | ⬜ Planned |
