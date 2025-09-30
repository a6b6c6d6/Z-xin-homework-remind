# helper.py
from time_utils import within_48h, overdeadline
from dingtalk import send_ding

def get_hw_count(list, aaa):
    return len(list[aaa])

def judge(unfinishCount_i, deadline, msg, courseName_i,answerProgress):
    if answerProgress==0 and within_48h(deadline) == -1 and unfinishCount_i != 0 and overdeadline(deadline) != -1:
        print(msg)          # 保留终端输出
        send_ding(msg)      # 新增钉钉提醒
    else:

        print(f"课程《{courseName_i}》暂无48小时内截止的作业或均已完成")
