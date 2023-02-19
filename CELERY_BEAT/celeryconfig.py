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
}
