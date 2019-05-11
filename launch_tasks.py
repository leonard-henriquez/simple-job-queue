import time
from worker.tasks import task_wait_3s

print('Start!')
for i in range(100):
  print('New task #', i)
  result = task_wait_3s.delay()
  print(result.get())

exit()
