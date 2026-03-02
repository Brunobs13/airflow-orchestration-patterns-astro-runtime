"""Weekly ML workflow skeleton DAG.

This DAG represents a simple machine-learning lifecycle orchestration with
three logical phases: preprocessing, training, and evaluation.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


DEFAULT_ARGS = {"owner": "ml-platform", "retries": 2}


def preprocess_data() -> None:
    print("Preprocessing data...")


def train_model() -> None:
    print("Training model...")


def evaluate_model() -> None:
    print("Evaluating model...")


with DAG(
    dag_id="weekly_ml_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@weekly",
    catchup=False,
    default_args=DEFAULT_ARGS,
    tags=["ml", "pipeline", "orchestration"],
) as dag:
    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data,
    )
    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model,
    )
    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model,
    )

    preprocess >> train >> evaluate
