import csv
import requests
from dagster import asset, job, op, ScheduleDefinition, define_asset_job, AssetSelection
import pandas as pd


@asset
def cereals():
    try:
        response = requests.get("https://docs.dagster.io/assets/cereal.csv")
        # lines = response.text.split("\n")
        # cereal_rows = [row for row in csv.DictReader(lines)]
        # print(cereal_rows)
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"{e}")


@asset
def nabisco_cereals(cereals):
    with open("cereals.csv", "w") as f:
        f.write(cereals)
    return 1


@asset
def cereal_protein_fractions():
    """
    For each cereal, records its protein content as a fraction of its total mass.
    """
    df = pd.read_csv(
        "/external/test_proj/dagster/cereals.csv", index_col=False)
    df.set_index('name', inplace=True)

    return df


@asset
def cereal_test_fractions(cereal_protein_fractions):
    df = cereal_protein_fractions
    mask = df['calories'] > 110
    df = df.loc[mask, ['calories']]
    return df


@asset
def print_calories_above_110(cereal_test_fractions):
    print(cereal_test_fractions)


@job
def my_job():
    cereals()
    nabisco_cereals()
    cereal_protein_fractions()
    cereal_test_fractions()
    print_calories_above_110()


asset_job = define_asset_job(
    "asset_job", AssetSelection.groups("some_asset_group"))

basic_schedule = ScheduleDefinition(job=asset_job, cron_schedule="* * * * *")
