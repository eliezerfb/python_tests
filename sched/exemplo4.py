"""Marcar um evento em um tempo específico definindo a data e hora"""

import sched
import time

from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def say_time():
    print(time.ctime())

scheduler.enterabs(datetime(2018, 5, 15, 14, 33).timestamp(),
                   priority=100,
                   action=say_time)

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com o sched!')
