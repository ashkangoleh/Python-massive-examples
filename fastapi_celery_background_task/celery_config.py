"""
Celery configuration
"""
import os
from functools import lru_cache
from kombu import Queue


# def route_task(name):
def route_task(name, args, kwargs, options, task=None, **kw):
    """
    Route Task
    args: name:str
    """
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class BaseConfig:
    """
    Base configuration
    """
    broker_url: str = os.environ.get(
        "CELERY_BROKER_URL", "redis://localhost:6379/")
    # result_backend: str = os.environ.get("CELERY_RESULT_BACKEND",
    # "db+postgresql+psycopg2://root:1@localhost:5432/root")
    result_backend: str = "db+postgresql+psycopg2://root:1@localhost:5432/root"
    # result_backend: str = os.environ.get("result_backend", "rpc://")
    result_extended: bool = True
    CELERY_TASK_QUEUES: list = (
        # default queue
        Queue("celery"),
        # custom queue
        Queue("sign_up"),
        Queue("sign_in"),
    )

    CELERY_TASK_ROUTES = (route_task,)

    @property
    def broker_url_str(self):
        """
        return broker url info
        """
        return f"configuration_recorder_data is {self.broker_url}"

    @property
    def result_backend_str(self):
        """
        return broker url info
        """
        return f"configuration_recorder_data is {self.result_backend}"

    @property
    def tasks_queue_list(self):
        """
        return tasks queue list
        """
        return f"configuration_recorder_data is {self.CELERY_TASK_QUEUES}"


class DevelopmentConfig(BaseConfig):
    """DevelopmentConfig

    Args:
        BaseConfig (Class): Base configuration
    """
    pass


@lru_cache()
def get_settings():
    """settings instance

    Returns:
        class: class configuration settings
    """
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
