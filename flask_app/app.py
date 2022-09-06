from flask import Flask
from celery import Celery

# Flask service
app = Flask(__name__)
# Celery service
simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')


# @app.route("/") is a Python decorator that Flask provides to assign URLs in our app to functions easily
@app.route('/simple_start_task')
def call_method():
    # Flask uses standard Python logging (https://flask.palletsprojects.com/en/2.2.x/logging/)
    app.logger.info("Invoking Method")
    # In celery send task by name. https://docs.celeryq.dev/en/stable/reference/celery.html#celery.Celery.send_task
    # In simple_worker/task.py we have one task called longtime_add
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    app.logger.info(r.backend)
    return r.id


@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app = simple_app)
    print("Invoking Method ")
    return "Status of the task: " + str(status.state)


@app.route('/simple_task_results/<task_id>')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    return "Result of the task: " + str(result)