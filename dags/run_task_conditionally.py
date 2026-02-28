from airflow.sdk import dag, task
import logging

@dag
def run_task_conditionally():

    @task
    def a():
        return 1

    @task.branch
    def b(val: int):
        if val == 1:
            return ['equal_1', 'if_1']
        else:
            return ['greater_than_1']

    @task
    def equal_1(val: int):
        logging.info(f"equal_1: {val}")

    @task
    def if_1(val: int):
        logging.info(f"if_1: {val}")

    @task
    def greater_than_1(val: int):
        logging.info(f"greater_than_1: {val}")

    val = a()
    b(val) >> [equal_1(val), if_1(val), greater_than_1(val)]

run_task_conditionally()