import sched
import time

scheduler = sched.scheduler()

def say_time():
    print(time.ctime())
    scheduler.enter(delay=10, priority=0, action=say_time)

say_time()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com o sched!')
