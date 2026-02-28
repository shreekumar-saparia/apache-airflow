from airflow.sdk import dag, task
from typing import Dict, Any
import logging

@dag
def xcom_example_2():

    @task
    def task_1() -> Dict[str, Any]:
        val = 42
        my_sentence = "Hello World!"
        return {
            "my_val": val,
            "my_sentence": my_sentence
        }

    @task
    def task_2(input: Dict[str, Any]):
        logging.info(input['my_val'])
        logging.info(input['my_sentence'])

    data = task_1()
    task_2(data)

xcom_example_2()
