from celery import Celery
from .settings import BROKER_URL

print('URL of broker: ', BROKER_URL)
app = Celery(
  'worker',
  broker=BROKER_URL,
  backend='amqp://',
  include=['app.tasks']
)

if __name__ == '__main__':
  app.start()
