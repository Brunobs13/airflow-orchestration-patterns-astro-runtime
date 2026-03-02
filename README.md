# Airflow Orchestration Patterns

Production-style Apache Airflow project that demonstrates reusable DAG patterns for API ingestion, PythonOperator chains, and TaskFlow-based orchestration.

## Project Overview

This repository provides a clean local Airflow environment (Astro Runtime) with multiple DAG design patterns that can be reused in data engineering and ML orchestration projects.

## Business Use Case

Teams often need a shared orchestration baseline before implementing project-specific pipelines. This repo offers that baseline with tested DAG loading, clean scheduling defaults, and explicit retry policies.

## DAG Portfolio

- `daily_spacecraft_ingestion`: TaskFlow + dynamic mapping + external API ingestion.
- `math_sequence_classic`: sequential transformations with `PythonOperator` + XCom.
- `math_sequence_taskflow`: same sequence with TaskFlow decorators.
- `weekly_ml_pipeline`: ML lifecycle skeleton (`preprocess -> train -> evaluate`).

## Tech Stack

- Apache Airflow (Astro Runtime)
- Python 3.11+
- requests
- pytest (DAG import integrity checks)
- Docker (via Astro CLI)

## Repository Structure

```text
.
├── dags/
├── tests/dags/
├── airflow_settings.yaml
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

## Local Run

1. Install Astro CLI and Docker.
2. Start local Airflow:

```bash
astro dev start
```

3. Open Airflow UI at `http://localhost:8080`.
4. Run DAG tests:

```bash
astro dev pytest tests
```

5. Stop local environment:

```bash
astro dev stop
```

## Security Notes

- No credentials are hardcoded in DAG code.
- Keep secrets in Airflow Connections/Variables, not in source files.
- `.env` and local runtime artifacts are excluded from version control.

## Future Improvements

1. Add provider-specific integration tests (HTTP/Postgres hooks).
2. Add CI workflow for DAG import tests on pull requests.
3. Add observability tasks (SLA checks and alert callbacks).
