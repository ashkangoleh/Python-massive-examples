#!/usr/bin/env python3
from faker import Faker
from random import choice
import json

fake = Faker()


def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


def get_name_age():
    return {"name": fake.name(), "age": choice([i for i in range(10, 50)])}


with open("/drive_data/test_proj/spark_tut/people.json", "a") as file:
    for i in range(100):
        dic = get_name_age()
        file.write(json.dumps(dic))
