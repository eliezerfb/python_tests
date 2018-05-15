import sched
import time

scheduler = sched.scheduler()

def say_time():
    print(time.ctime())
    scheduler.enter(delay=10, priority=1, action=say_time)

def ola():
    print('Olá!')
    scheduler.enter(delay=5, priority=0, action=ola)


def start():
    scheduler.enter(delay=10, priority=1, action=say_time)
    scheduler.enter(delay=5, priority=0, action=ola)

start()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com o sched!')
