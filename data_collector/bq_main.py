from google.cloud import bigquery as bq
import os
from google.oauth2 import service_account
import pandas as pd


WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    WORKING_DIR, 'credentials.json')
credentials_file = os.path.join(WORKING_DIR, 'credentials.json')

credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=[
        "https://www.googleapis.com/auth/cloud-platform"],
)
table_id = "bigquery-public-data.crypto_bitcoin.transactions"
client = bq.Client(credentials=credentials, project=credentials.project_id)
query = """SELECT * FROM `bigquery-public-data.crypto_bitcoin.transactions` WHERE block_timestamp_month between "2009-01-14" and "2009-02-14" limit 10;"""

query_job = bq.QueryJobConfig(allow_large_results=True)



for count in range(13, 23):
    if count == 9:
        start_time = f'200{count}-01-01'
        end_time = f'200{count}-12-31'
    else:
        start_time = f'20{count}-01-01'
        end_time = f'20{count}-12-31'
    query = f"""SELECT * FROM `bigquery-public-data.crypto_bitcoin.transactions` WHERE block_timestamp_month between "{start_time}" and "{end_time}";"""
    directory = os.path.join(os.path.dirname(__file__))
    df = client.query(query, job_config=query_job).to_dataframe()
    df.to_csv(
        directory + f'/transactions_table_dumps_latest_{count}.csv', index=False)
    #     # # count = count + 1
    print(count)
    #     # if count > 22:
    #     #     break
