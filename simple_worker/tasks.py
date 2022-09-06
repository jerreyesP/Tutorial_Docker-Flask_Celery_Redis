import time
from celery import Celery
from celery.utils.log import get_task_logger
#
import random
# for crontab celery
from celery.schedules import crontab
#

# Get logger for task module by name
logger = get_task_logger(__name__)

app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


@app.task()
def longtime_add(x, y):
    logger.info('Got request - Starting work')
    print(f"Time when task began: {time.time()}")
    time.sleep(4)
    logger.info('Work finished')
    print(f"Time when task finished: {time.time()}")
    return x + y

# Functions added after tutorial

@app.task(bind=True)
def log_info(self):
    print('Request: {0!r}'.format(self.request))


@app.task()
def time_request():
    return time.time()

@app.task()
def suma_random():
    # pipenv run python
    # from simple_worker.tasks import suma_random
    # suma_random()
    logger.info('Got request - Starting work')
    print(f"Time when task began: {time.time()}\n")
    time.sleep(2)
    x = random.randint(1, 99)
    y = random.randint(1, 100)
    print(f"{x} + {y} = {x + y}")
    print(f"\nTime when task finished: {time.time()}")
    logger.info('Work finished')
    return x + y


@app.task()
def resta_crontab():
    print(f"Time when the task began: {time.time()}\n")
    x = random.randint(50,100)
    y = random.randint(10, 25)
    resta = x - y
    print(f"Operation: {x} - {y} = {resta}")
    print(f"\nTime when the task finished: {time.time()}")
    return resta


# add "resta_crontab" task to the beat schedule, periodic task
app.conf.beat_schedule = {
    "resta_crontab-every-minute": {
        "task": "tasks.resta_crontab",
        "schedule": crontab()
    }
}
app.conf.timezone = 'Europe/London'
