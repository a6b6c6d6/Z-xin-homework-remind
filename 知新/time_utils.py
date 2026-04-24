# time_utils.py
from datetime import datetime, timezone, timedelta


def time():
    beijing_tz = timezone(timedelta(hours=8))
    beijing_time = datetime.now(beijing_tz)
    return beijing_time.strftime("%Y-%m-%d %H:%M:%S")


def parse_deadline(deadline_str: str) -> str:
    """
    将ISO 8601格式的截止时间转换为北京时间字符串
    例如: "2026-04-29T14:20:00.000Z" -> "2026-04-29 22:20:00"
    """
    try:
        dt_utc = datetime.strptime(deadline_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
    except ValueError:
        try:
            dt_utc = datetime.strptime(deadline_str.replace('Z', '+00:00'), "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=timezone.utc)
        except ValueError:
            return deadline_str
    
    dt_beijing = dt_utc.astimezone(timezone(timedelta(hours=8)))
    return dt_beijing.strftime("%Y-%m-%d %H:%M:%S")


def within_7d(deadline_str):
    """检查截止时间是否在一周内"""
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    threshold = timedelta(days=7)
    return -1 if (deadline - beijing_now) < threshold else None


def overdeadline(deadline_str):
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    return -1 if (deadline - beijing_now) < timedelta(seconds=0) else None


def human_left(deadline_str: str) -> str:
    beijing_now = datetime.strptime(time(), "%Y-%m-%d %H:%M:%S")
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M:%S")
    left = deadline - beijing_now
    if left.total_seconds() <= 0:
        return "已截止"
    days = left.days
    hours, rem = divmod(left.seconds, 3600)
    minutes, sec = divmod(rem, 60)
    parts = []
    if days: parts.append(f"{days}天")
    if hours: parts.append(f"{hours}小时")
    if minutes: parts.append(f"{minutes}分钟")
    if sec: parts.append(f"{sec}秒")
    return "还剩 " + " ".join(parts) if parts else "已截止"