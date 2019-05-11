import time
from os import environ
from celery import Celery

CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
CELERY_RESULT_BACKEND = environ["CELERY_RESULT_BACKEND"]

print('URL of broker: ', CELERY_BROKER_URL)
print('URL of backend: ', CELERY_RESULT_BACKEND)
worker = Celery(
    'worker',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=['worker.tasks']
)

print('Start!')
for i in range(100):
  print('New task #', i)
  result = worker.send_task('worker.tasks.task_wait_3s')
  print(result.get())

exit()
