from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from airflow.utils.dates import days_ago


with DAG(dag_id="test",
         start_date=days_ago(3),
         schedule_interval="@daily",
         catchup=False) as dag:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    @task
    def test1():
        return timestamp
    
    @task
    def test2():
        return timestamp

    
    test2(test1())