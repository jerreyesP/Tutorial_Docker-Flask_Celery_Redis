# Tutorial_Docker-Flask_Celery_Redis

Based on the tutorial: https://github.com/soumilshah1995/Python-Flask-Redis-Celery-Docker/tree/main/Part1

## Problems:

 - When I execute _'docker-compose up'_ an errors occurred, it didn't found the route or something like that because i didn't open 'docker-desktop', when I inicilice it, the command execute correctly.
 - There was an error in the dockerfile for the _'COPY'_, I forggoten put the bar '/' on the _requirements.txt_. (https://stackoverflow.com/questions/55072179/failed-to-execute-script-docker-compose)
 - There was an error on the requierements.txt, in the field of _flask_app_, beacse the latest version of _flask_ have some conflicts with this process, because of that i make a modication on the _'requierements.txt'_ and put version under 2.3. -> Flask<=2.3
 - For check the status of Celery, use the command on the console of docker-desktop for celery, in this case, simple_worker: __celery -A tasks status__
 - For execute the periodic task with cron_tab of celery, execute on the console of the service docker, on docker-desktop, for simple_worker, the next command: __celery -A tasks beat -s /tmp/celerybeat-schedule__ (https://stackoverflow.com/questions/44605117/oserror-errno-13-permission-denied-when-initializing-celery-in-docker) (https://stackoverflow.com/questions/56980069/how-to-fix-error-removing-corrupted-schedule-file-celerybeat-schedule-error)

## How execute periodic task with celery

1. Write 'docker-compose up' on the console, in my case was Pycharm
2. Go to Docker-desktop and get inside the console of the service of celery, in this case: simple_worker and write: __celery -A tasks beat -s /tmp/celerybeat-schedule__


Thanks to soumilshah1995, his tutorial help me a lot for understand a little bit docker, celery, redis and all of this. 
_https://github.com/soumilshah1995/Python-Flask-Redis-Celery-Docker_
