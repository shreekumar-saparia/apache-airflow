from airflow.sdk import dag, task

@dag
def custom_sql_provider():

    @task.sql(
        conn_id="postgres"
    )
    def get_nb_xcom():
        return "select count(*) from xcom"

    get_nb_xcom()

custom_sql_provider()