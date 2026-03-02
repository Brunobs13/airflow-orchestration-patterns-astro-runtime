"""TaskFlow API sequence DAG.

Same arithmetic pipeline as the classic DAG, implemented with TaskFlow
decorators and XCom return values.
"""

from datetime import datetime

from airflow import DAG
from airflow.decorators import task


DEFAULT_ARGS = {"owner": "data-platform", "retries": 2}


with DAG(
    dag_id="math_sequence_taskflow",
    start_date=datetime(2024, 1, 1),
    schedule="@once",
    catchup=False,
    default_args=DEFAULT_ARGS,
    tags=["math", "taskflow", "pipeline"],
) as dag:
    @task
    def start_number() -> int:
        value = 10
        print(f"Starting number: {value}")
        return value

    @task
    def add_five(number: int) -> int:
        result = number + 5
        print(f"Add 5: {number} + 5 = {result}")
        return result

    @task
    def multiply_by_two(number: int) -> int:
        result = number * 2
        print(f"Multiply by 2: {number} * 2 = {result}")
        return result

    @task
    def subtract_three(number: int) -> int:
        result = number - 3
        print(f"Subtract 3: {number} - 3 = {result}")
        return result

    @task
    def square_number(number: int) -> int:
        result = number**2
        print(f"Square result: {number}^2 = {result}")
        return result

    square_number(subtract_three(multiply_by_two(add_five(start_number()))))
