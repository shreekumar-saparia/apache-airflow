# Getting Started with Apache Airflow

## Setup development environment
1) Install docker and configure 4 CPUs, 8 GB memory and 64 GB disk space.
2) Navigate to this project dir where docker-compose.yaml file is present.
3) Run 
   * docker compose up
   * docker compose down (to bring all container down brought up using previous command)
4) You can open airflow UI at localhost:8080 and use airflow as username and password.


## To test task, follow below steps
1) ssh to airflow scheduler node/container
2) /bin/bash
3) airflow tasks test <dag-id> <task-id>
   * eg, airflow tasks test user_processing create_table
4) This will not create any entry in the airflow meta DB.

## To test assets, follow below steps
1) ssh to airflow scheduler node/container
2) /bin/bash
3) airflow assets list