# CLAUDE.md — Databricks learning repo

Handoff from a planning session in the Claude app (Nov 10, 2026). Read this first.

## Who and what
- Owner: Alwin (GitHub `Techieeman007`, brand "Techieeman"). Background: Python, SQL, IoT
  (MQTT, ThingsBoard), AWS/GCP, ML pipelines, GPU infra, model deployment.
- Goal: learn Databricks from a **data engineering + AI/ML** angle (hybrid track) and build
  public content in this repo as he goes. Notes may later become Medium posts for
  "Techieeman's Engineering Knowledge Base".
- First milestone: **Databricks User Group Coimbatore meetup, Sat Nov 14, 2026,
  9:30 AM–1:30 PM IST** (Welcomhotel by ITC, Race Course). Demos planned: Genie, OmniGent,
  enterprise AI/ML use cases. Speakers are Databricks FDEs.
- Hands-on environment: Databricks Free Edition.

## Your role: tutor + scribe
Each session follows this loop:
1. **Teach** the day's topic concisely, tied to his IoT background where it helps.
2. **Quiz** him with 2–4 short questions; correct misconceptions plainly.
3. **Hands-on**: give a small task to run in Databricks Free Edition.
4. **Write the notes**: fill the matching `notes/0X-*.md` (sections: Key ideas / In my words /
   Questions). "In my words" must come from HIS answers, lightly edited — not your prose.
5. Update the README status tables, then commit with a clear message. Ask before pushing.

Keep notes short, accurate, and in his voice. Prefer official Databricks docs; check
product names/features against docs.databricks.com when unsure (they change often).

## Sprint plan (fix README dates: Nov 10, 2026 is a TUESDAY)
| Day | Date | Topic | Notes file |
|---|---|---|---|
| 1 | Tue Nov 10 | Lake vs warehouse vs lakehouse; what Databricks adds over Spark; Delta Lake basics | notes/01-lakehouse.md |
| 2 | Wed Nov 11 | Spark architecture (driver/executors), DataFrames, transformations vs actions, PySpark + first notebook | notes/02-spark.md |
| 3 | Thu Nov 12 | Workspace, compute (classic vs serverless), Delta (ACID, time travel), Unity Catalog (catalog.schema.table), Databricks SQL, Lakeflow/Jobs | notes/03-platform.md |
| 4 | Fri Nov 13 | MLflow + model lifecycle, Mosaic AI, Genie; finalize meetup questions | notes/04-ai-ml.md, meetup/ |
| — | Sat Nov 14 | Meetup — afterwards, capture takeaways in meetup/2026-11-14-coimbatore.md | |

Later phases: pipelines (medallion, streaming), ML/AI (feature eng, registry, serving, RAG,
agents), production (governance, performance, cost, CI/CD).

## Where Day 1 stands
Day 1 lesson was already taught in the Claude app. Covered: warehouse (schema-on-write,
ACID, costly, poor for raw/ML data) vs lake (cheap, any format, no transactions, "swamp")
vs lakehouse (open files + table layer). Delta table = Parquet files + `_delta_log/` JSON
commits. Databricks = managed platform around Spark adding compute mgmt, Delta, Unity
Catalog, notebooks/Jobs/Lakeflow, Databricks SQL, MLflow/Mosaic AI, Genie. IoT mapping:
bronze (raw MQTT JSON) → silver (parsed, deduped, validated) → gold (hourly KPIs, anomalies).

Pending: he has NOT yet answered the Day 1 quiz. Start by asking:
1. Why did companies run both a lake and a warehouse, and what problem did that cause?
2. Physically, what is a Delta table on disk?
3. If you can run Spark yourself, what are you paying Databricks for?
Then: confirm he signed up for Free Edition and explored Catalog → `samples`; write
notes/01-lakehouse.md from his answers; mark Day 1 done in README; commit.

## Meetup questions to seed meetup/2026-11-14-coimbatore.md
- How does Databricks differ from running Apache Spark yourself?
- Handling millions of IoT telemetry events in real time — Structured Streaming vs batch?
- How does Unity Catalog manage access across teams?
- Classic vs serverless compute trade-offs?
- How do MLflow and Mosaic AI support RAG / agentic apps in production?
- Architecting real-time industrial IoT: ingestion → medallion → predictive maintenance + AI analytics?
- What skills should an AI/ML engineer prioritise to get proficient on Databricks?

## Main project (after the meetup)
`projects/iot-lakehouse/`: simulated MQTT sensor telemetry → bronze/silver/gold Delta tables
→ KPI dashboard → later an anomaly/predictive-maintenance model tracked in MLflow.
Notebooks exported as `.py` source into `notebooks/` or the project folder.

## Conventions
- Commit messages: short imperative ("Add Day 1 lakehouse notes").
- Never commit credentials, tokens, or workspace URLs with IDs.
