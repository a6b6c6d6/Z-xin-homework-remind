# helper.py
from time_utils import within_7d, overdeadline
from dingtalk import send_ding


def get_hw_count(list, aaa):
    return len(list[aaa])


def judge(unfinishCount_i, deadline, msg, courseName_i, answerProgress):
    if answerProgress == 0 and within_7d(deadline) == -1 and unfinishCount_i != 0 and overdeadline(deadline) != -1:
        print(msg)
        send_ding(msg)
    else:
        print(f'课程《{courseName_i}》暂无一周期内截止的作业或均已完成')