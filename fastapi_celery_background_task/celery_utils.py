"""
Celery utilities
"""
from celery import current_app as current_celery_app
from celery.result import AsyncResult

from celery_config import settings


def create_celery():
    """Create celery instance

    Returns:
        current_app: return celery app with update configuration
    """
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace='CELERY')
    celery_app.conf.update(task_track_started=True)
    celery_app.conf.update(task_serializer='pickle')
    celery_app.conf.update(result_serializer='pickle')
    celery_app.conf.update(accept_content=['pickle', 'json'])
    celery_app.conf.update(result_expires=200)
    celery_app.conf.update(result_persistent=True)
    celery_app.conf.update(worker_send_task_events=False)
    celery_app.conf.update(worker_prefetch_multiplier=1)
    celery_app.conf.update(result_extended=True)

    return celery_app


def get_task_info(task_id):
    """get task info from a given task id

    Args:
        task_id (str): task id to retrieve information

    Returns:
        dict: return task info and status
    """
    task_result = AsyncResult(task_id)

    result = {
        # "task_id": task_id,
        "task_status": task_result.status,
        "task_info": task_result.get(),
    }
    return result
