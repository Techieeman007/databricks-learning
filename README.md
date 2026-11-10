# Databricks Learning — Techieeman

My learning log for Databricks, covering both data engineering and AI/ML. The goal is to understand the lakehouse architecture, get comfortable with Spark and the Databricks platform (Unity Catalog, Jobs, Delta Live Tables), and use it for ML/AI work (MLflow, Feature Store, Model Serving, Mosaic AI). Along the way I'm building small end-to-end projects in Databricks Free Edition and writing down what I learn in my own words.

## Progress

### Meetup sprint (Nov 10–13, 2026)

Prep for the [Databricks meetup in Coimbatore on Nov 14](meetup/2026-11-14-coimbatore.md).

| Day | Date | Focus | Status |
|-----|------|-------|--------|
| 1 | Mon, Nov 10 | Lakehouse fundamentals + Delta Lake | ⬜ Not started |
| 2 | Tue, Nov 11 | Spark DataFrames + Free Edition hands-on | ⬜ Not started |
| 3 | Wed, Nov 12 | Platform: Unity Catalog, Jobs, DLT | ⬜ Not started |
| 4 | Thu, Nov 13 | AI/ML overview + finalize meetup questions | ⬜ Not started |

### Learning phases

| Phase | Topic | Notes | Status |
|-------|-------|-------|--------|
| 1 | Lakehouse & Delta Lake | [01-lakehouse.md](notes/01-lakehouse.md) | ⬜ Not started |
| 2 | Apache Spark on Databricks | [02-spark.md](notes/02-spark.md) | ⬜ Not started |
| 3 | Platform: Unity Catalog, Workflows, DLT | [03-platform.md](notes/03-platform.md) | ⬜ Not started |
| 4 | AI/ML: MLflow, Feature Store, Model Serving | [04-ai-ml.md](notes/04-ai-ml.md) | ⬜ Not started |
| 5 | Capstone: end-to-end project | [projects/](projects/) | ⬜ Not started |

Status key: ⬜ Not started · 🟨 In progress · ✅ Done

## Repo layout

- [notes/](notes/) — concept notes per phase
- [notebooks/](notebooks/) — notebooks exported from Databricks
- [projects/](projects/) — hands-on projects
- [meetup/](meetup/) — meetup prep and takeaways

## Projects

| Project | Description | Status |
|---------|-------------|--------|
| [iot-lakehouse](projects/iot-lakehouse/) | IoT telemetry pipeline using the medallion architecture (bronze → silver → gold) | ⬜ Planned |
