from airflow import DAG
from airflow.decorators import task
from datetime import datetime
from airflow.utils.dates import days_ago


with DAG(dag_id="get_price_GGL",
         start_date=days_ago(3),
         schedule_interval="@weekly",
         catchup=False) as dag:
    @task
    def extract(symbol):
        return symbol
    
    @task
    def process(symbol):
        return symbol
    
    @task
    def store(symbol):
        return symbol
    
    store(process(extract(3243)))