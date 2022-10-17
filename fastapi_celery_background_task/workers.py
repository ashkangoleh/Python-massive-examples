"""
celery workers
"""
import time
from celery import shared_task
# from celery.result import AsyncResult
# from celery_config import settings
# SIGN_UP_Q = Celery("SIGN_UP_Q", broker="redis://localhost:6379/",
#                 backend="db+postgresql+psycopg2://root:1@localhost:5432/")
# SIGN_IN_Q = Celery("SIGN_IN_Q", broker="redis://localhost:6379/",
#                 backend="db+postgresql+psycopg2://root:1@localhost:5432/")
# SIGN_IN_Q.conf.update(result_extended=True)
# SIGN_IN_Q.conf.update(result_extended=True)
# celery = Celery(__name__)
# celery.conf.broker_url = "redis://localhost:6379"
# celery.conf.result_backend = "db+postgresql+psycopg2://root:1@localhost:5432/root"
# celery.select_queues(
# [    "sign_up",
#     "sign_in"]
# )


# @SIGN_IN_Q.task(name="signing_in",
#     autoretry_for=(Exception,),
#     retry_kwargs={"max_retries": 3, "countdown": 3},
# )
# def onboard_user(user_email):
#     print(user_email)
#     print(f"{onboard_user.__name__}")
#     print("...")


@shared_task(name="sign_in",
             autoretry_for=(Exception,),
             retry_kwargs={"max_retries": 3, "countdown": 3},
             )
def onboard_user_sign_in(self, user_email):
    """
    onboard_user sign in user with email address
    """
    self.update_state(state="SUCCESS", meta={'user_email': user_email})
    print(user_email)
    print(f"{onboard_user_sign_in.__name__}")
    print("...")


# @SIGN_UP_Q.task(name="sign_up",
#     autoretry_for=(Exception,),
#     retry_kwargs={"max_retries": 3, "countdown": 3},
# )
# def onboard_user(user_email):
#     print(user_email)
#     print("send welcome email")
#     print("sent")
#     print("...")
#     time.sleep(10)
#     # result = SIGN_UP_Q.AsyncResult(user_email)
#     return user_email,"OK"


@shared_task(name="sign_up",
             autoretry_for=(Exception,),
             retry_kwargs={"max_retries": 3, "countdown": 3},
             )
def onboard_user_sign_up(user_email):
    """
    onboard_user sign up user with email address
    """
    print(user_email)
    print("send welcome email")
    print("sent")
    print("...")
    time.sleep(10)
    # result = SIGN_UP_Q.AsyncResult(user_email)
    return user_email, "OK"
