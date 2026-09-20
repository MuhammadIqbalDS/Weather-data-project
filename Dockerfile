FROM apache/airflow:slim-3.3.2

USER airflow

RUN pip install --no-cache-dir psycopg2-binary asyncpg