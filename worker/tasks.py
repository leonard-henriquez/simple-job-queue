from .worker import app
from time import sleep
from random import random

@app.task
def task_wait_3s():
  print("long time task begin")
  sleep(3)
  print("long time task finished")
  return random()
