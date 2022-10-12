from celery import Celery
celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379"
celery.conf.result_backend = "redis://localhost:6379"


@celery.task(
    name="onboard_user",
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "countdown": 3},
)
def onboard_user(user_email):
    print(user_email)
    print("send welcome email")
    print("subscribe to newsletter")
    print("Add to CRM")
    print("...")
    return True
