from celery import Celery
from celery.result import AsyncResult
import requests
from celeryconfig import *
app = Celery('tasks', broker=CELERY_BROKER_URL,
             backend=CELERY_RESULT_BACKEND)
# app.config_from_object('celeryconfig')
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

app.conf.timezone = 'UTC'
@app.task
def send_request():
    response = requests.get(
        'https://my.arzdigital.com/?getJafangCms=584hg5f4g___^fdg&p=1&type=1,spam')
    # do something with the response
    print(response.json())


# celery -A tasks worker --loglevel=info
# celery -A tasks beat --loglevel=info


result = AsyncResult("0c557e12-6366-4c7d-a976-ada9fb5bbf9f",task_name='tasks', app=app)
if result.ready():
    print(result.get())