#pip install wakaq
import logging
from datetime import timedelta
from wakaq import WakaQ, Queue, CronTask


wakaq = WakaQ(
    host="arz.local",
    port=6379,
    # List your queues and their priorities.
    # Queues can be defined as Queue instances, tuples, or just a str.
    queues=[
        (0, 'a-high-priority-queue'),
        (1, 'a-medium-priority-queue'),
        (2, 'a-low-priority-queue'),
        'default-lowest-priority-queue',
        Queue('another-queue', priority=3, default_max_retries=5),
    ],

    # Number of worker processes. Must be an int or str which evaluates to an
    # int. The variable "cores" is replaced with the number of processors on
    # the current machine.
    concurrency="cores*4",

    # Raise SoftTimeout in a task if it runs longer than 30 seconds.
    soft_timeout=30,  # seconds

    # SIGKILL a task if it runs longer than 1 minute.
    hard_timeout=timedelta(minutes=1),

    # If the task soft timeouts, retry up to 3 times. Max retries comes first
    # from the task decorator if set, next from the Queue's default_max_retries,
    # lastly from the option below. If No default_max_retries is found, the task
    # is not retried on a soft timeout.
    default_max_retries=3,

    # Combat memory leaks by reloading a worker (the one using the most RAM),
    # when the total machine RAM usage is at or greater than 98%.
    max_mem_percent=98,

    # Combat memory leaks by reloading a worker after it's processed 5000 tasks.
    max_tasks_per_worker=5000,

    # Schedule two tasks, the first runs every minute, the second once every ten minutes.
    # Scheduled tasks can be passed as CronTask instances or tuples.
    schedules=[

        # Runs mytask on the queue with priority 1.
        CronTask('* * * * *', 'mytask', queue='a-medium-priority-queue', args=[2, 2], kwargs={}),

        # Runs mytask once every 5 minutes.
        ('*/5 * * * *', 'mytask', [1, 1], {}),

        # Runs anothertask on the default lowest priority queue.
        ('*/10 * * * *', 'anothertask'),
    ],
)


@wakaq.task(queue='a-medium-priority-queue', max_retries=7)
def mytask(x, y):
    return x+y


@wakaq.task
def anothertask():
    mytask(1,1)


@wakaq.wrap_tasks_with
def custom_task_decorator(fn):
    def inner(*args, **kwargs):
        # do something before each task runs
        fn(*args, **kwargs)
        # do something after each task runs
    return inner


if __name__ == '__main__':
    # add 1 plus 1 on a worker somewhere, overwriting the task's queue from medium to high
    mytask.delay(1, 1, queue='a-high-priority-queue')
    # add 1 plus 1 on a worker somewhere, running on the default lowest priority queue
    anothertask.delay()