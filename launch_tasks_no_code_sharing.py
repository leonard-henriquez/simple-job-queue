import time
from os import environ
from celery import Celery

CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = environ["CELERY_RESULT_BACKEND"]

app = Celery(
    'worker',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=['app.tasks']
)

print('Start!')
for i in range(100):
  print('New task #', i)
  result = app.send_task('task_wait_3s')

exit()
