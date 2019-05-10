from .worker import app
from time import sleep

@app.task
def task_wait_3s():
  print("long time task begin")
  sleep(3)
  print("long time task finished")
