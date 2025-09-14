# time_utils.py
from datetime import datetime, timezone, timedelta

def time():
    beijing_tz = timezone(timedelta(hours=8))
    beijing_time = datetime.now(beijing_tz)
    return beijing_time.strftime("%Y-%m-%d %H:%M:%S")

def within_48h(deadline_str):
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    rrr = timedelta(hours=148, minutes=43, seconds=21)
    return -1 if (deadline - beijing_now) < rrr else None

def overdeadline(deadline_str):
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    return -1 if (deadline - beijing_now) < timedelta(seconds=0) else None