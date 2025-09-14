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
def human_left(deadline_str: str) -> str:
    from datetime import datetime
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline    = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    left = deadline - beijing_now
    if left.total_seconds() <= 0:
        return "已截止"
    days    = left.days
    hours,  rem = divmod(left.seconds, 3600)
    minutes, sec = divmod(rem, 60)
    parts = []
    if days:    parts.append(f"{days}天")
    if hours:   parts.append(f"{hours}小时")
    if minutes: parts.append(f"{minutes}分钟")
    if sec:     parts.append(f"{sec}秒")
    return "还剩 " + " ".join(parts) if parts else "已截止"
