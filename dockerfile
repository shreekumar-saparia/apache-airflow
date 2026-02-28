from apache/airflow:3.0.0

copy my-sdk /opt/airflow/my-sdk

RUN pip install -e /opt/airflow/my-sdk