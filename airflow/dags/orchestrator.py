from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from inset_records import main
    return main()

default_args = {
    'start_date': datetime(2026, 9, 21),
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    description='A DAG to orchestrate data',
    default_args=default_args,
    schedule=timedelta(minutes=5),
    catchup=False,
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable,
    )
