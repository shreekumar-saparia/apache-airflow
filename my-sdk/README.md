# my-sdk

## Follow below install custom provider in airflow

1) comment below line from docker-compose.yaml file<br>
   * image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:3.0.0}
2) Uncomment below line
   * build: .
2) Run below command
   * docker compose up --build