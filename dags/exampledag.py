"""Daily API ingestion DAG using TaskFlow and dynamic mapping.

This workflow fetches crew metadata from a public API and emits one log task per
record. It serves as a template for external API ingestion patterns in Airflow.
"""

from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import requests


DEFAULT_ARGS = {"owner": "data-platform", "retries": 2}
API_URL = "http://api.open-notify.org/astros.json"


@dag(
    dag_id="daily_spacecraft_ingestion",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=DEFAULT_ARGS,
    tags=["api", "taskflow", "ingestion"],
)
def daily_spacecraft_ingestion():
    @task(outlets=[Dataset("spacecraft_crew_snapshot")])
    def fetch_crew() -> list[dict]:
        """Fetch crew records from external API; fallback to deterministic data."""
        try:
            response = requests.get(API_URL, timeout=10)
            response.raise_for_status()
            payload = response.json()
            return payload.get("people", [])
        except Exception:
            return [
                {"craft": "ISS", "name": "Crew Member A"},
                {"craft": "ISS", "name": "Crew Member B"},
                {"craft": "Tiangong", "name": "Crew Member C"},
            ]

    @task
    def log_crew_member(member: dict) -> None:
        craft = member.get("craft", "unknown")
        name = member.get("name", "unknown")
        print(f"{name} assigned to {craft}")

    log_crew_member.expand(member=fetch_crew())


dag = daily_spacecraft_ingestion()
