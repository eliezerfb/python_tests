"""Marcar um evento em um tempo específico (a cada x minutos ou segundos)"""

import sched
import time

from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def reschedule():
    "Zere os segundos de now() e some + 1 minuto"
    new_target = datetime.now().replace(microsecond=0)
    new_target += timedelta(seconds=30)
    print(new_target)

    scheduler.enterabs(new_target.timestamp(), priority=100, action=say_time)



def say_time():
    print(time.ctime())
    reschedule()

reschedule()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com o sched!')
