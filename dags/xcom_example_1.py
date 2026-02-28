from airflow.sdk import dag, task, get_current_context
import logging

@dag
def xcom_example_1():

    @task
    def t1():
        val = 42
        context = get_current_context()
        context['ti'].xcom_push(key='my_unique_key', value=val)

    @task
    def t2():
        context = get_current_context()
        val = context['ti'].xcom_pull(task_ids='t1', key='my_unique_key')
        logging.info(val)

    t1() >> t2()

xcom_example_1()