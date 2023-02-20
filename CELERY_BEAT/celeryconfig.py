from celery.schedules import crontab
CELERY_BROKER_URL = 'redis://arz.local:6379/0'
CELERY_RESULT_BACKEND = 'redis://arz.local:6379/0'
CELERY_TIMEZONE = 'UTC'

CELERY_BEAT_SCHEDULE = {
    'send-request-every-minute': {
        'task': 'tasks.send_request',
        # 'schedule': crontab(minute=0, hour='*'),
        'schedule': crontab()
    },
    'add-every-30-seconds': {
        'task': 'tasks.send_request',
        'schedule': 30.0,
        # 'args': (16, 16)
    },

    'yearly-task': {
        'task': 'my_task',
        # run once a year on Jan 1st
        'schedule': crontab(minute=0, hour=0, day_of_month=1, month_of_year=1),
    },
    'monthly-task': {
        'task': 'my_task',
        # run once a month on the 1st
        'schedule': crontab(minute=0, hour=0, day_of_month=1),
    },
    'weekly-task': {
        'task': 'my_task',
        # run once a week on Sunday
        'schedule': crontab(minute=0, hour=0, day_of_week=0),
    },
    'daily-task': {
        'task': 'my_task',
        'schedule': crontab(minute=0, hour=0),  # run once a day at midnight
    },
    'hourly-task': {
        'task': 'my_task',
        # run once an hour at the start of the hour
        'schedule': crontab(minute=0),
    },
    'every-15-min-task': {
        'task': 'my_task',
        'schedule': crontab(minute='*/15'),  # run every 15 minutes
    },
    'weekday-work-hours-task': {
        'task': 'my_task',
        # run every weekday from 9am to 5pm
        'schedule': crontab(minute=0, hour='9-17', day_of_week='1-5'),
    },

}
# 'every-15-min-task': {
#     'task': 'my_task',
#     'schedule': '*/15 * * * *',  # run every 15 minutes
# },