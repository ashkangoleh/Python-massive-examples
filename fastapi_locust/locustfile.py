from locust import HttpUser, task, between
import random

sentences = [
    "That's just what i needed today",
    "I love coding in python",
    "well that a surprise",
    "Ashkan hates eating shits"
]


class AppUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def index_page(self):
        self.client.get("/api/")

    @task
    def sentiment_page(self):
        my_text = random.choice(sentences)
        self.client.get(f"/api/sentiment/{my_text}")



# locust -f locustfile.py --host http://localhost:8080 --users 500