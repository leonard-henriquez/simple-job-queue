from celery import Celery
from .settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

print('URL of broker: ', CELERY_BROKER_URL)
print('URL of backend: ', CELERY_RESULT_BACKEND)
app = Celery(
  'worker',
  broker=CELERY_BROKER_URL,
  backend=CELERY_RESULT_BACKEND,
  include=['worker.tasks']
)

if __name__ == '__main__':
  app.start()
