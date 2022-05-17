# 0- Import Required Libraries
import logging
from bq_helper import BigQueryHelper
import os
import pandas as pd
from tqdm import tqdm

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    WORKING_DIR, 'credentials.json')

dataset_name = "crypto_bitcoin"
dataset = BigQueryHelper(
    active_project="bigquery-public-data", dataset_name=dataset_name)
# 3- Listing Tables
# Let's print the tables to check everything went ok so far.
print(f'{dataset.list_tables()}')

# 4- Getting Table Schema:
# The table's schema contains information about the names, types, and modes of each column.
print(dataset.table_schema(table_name='blocks'))

# 5- Estimate the Size of the Query
# Without needing to run the query we can check how much memory a query will scan.
query = " SELECT * FROM `bigquery-public-data.crypto_bitcoin.blocks` "
print(f'{dataset.estimate_query_size(query) * 1e3:.2f} MB')
df = dataset.query_to_pandas(query)
directory = os.path.join(os.path.dirname(__file__))
df.to_csv(directory+ f'/blocks.csv', index=False)
# count = "09"
# for count in range(9, 23):
#     if count == 9:
#         start_time = f'200{count}-01-01'
#         end_time = f'200{count}-12-31'
#     else:
#         start_time = f'20{count}-01-01'
#         end_time = f'20{count}-12-31'
#     query = f"""SELECT * FROM `bigquery-public-data.crypto_bitcoin.transactions` WHERE block_timestamp_month between "{start_time}" and "{end_time}";"""
#     df = dataset.query_to_pandas(query)
#     directory = os.path.join(os.path.dirname(__file__))
#     df.to_csv(directory+ f'/transactions_table_dumps_latest_{count}.csv', index=False)
#     #     # # count = count + 1
#     print(count)
#     #     # if count > 22:
#     #     #     break
