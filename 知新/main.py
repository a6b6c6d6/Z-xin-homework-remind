# main.py
import requests
from config import HEADERS, URL_CLASSROOM, URL_HOMEWORK_PAGE, URL_HOMEWORK_DETAIL
from time_utils import time
from helper import get_hw_count, judge
from dingtalk import send_ding

if __name__ == "__main__":
    session = requests.Session()
    headers = HEADERS
    ur1 = URL_CLASSROOM
    a = session.get(ur1, headers=headers).json()
    q = len(a['data']) - 1
    Id = [item['id'] for item in a['data']]
    courseId = [item['courseId'] for item in a['data']]
    unfinishCount = [item['unfinishCount'] for item in a['data']]
    ur3 = URL_HOMEWORK_PAGE
    homeworkId = []
    for i in range(q + 1):
        payload = {
            "classroomId": Id[i],
            "pageNum": 1,
            "pageSize": 1000
        }
        z = session.post(ur3, json=payload, headers=headers).json()
        aaa = [item['homeworkId'] for item in z.get('data', {}).get('list', [])]
        homeworkId.append(aaa)
    courseName = [item['courseName'] for item in a['data']]
    current_time = time()
    for i in range(q + 1):
        ur4 = f"https://stu.z-xin.net/classroom/ {Id}/homework-list?cid={courseId[i]}"
        if (unfinishCount[i] == 0):
            print(f"课程《{courseName[i]}》暂无未完成的作业")
            continue
        for j in range(get_hw_count(homeworkId, i)):
            c = homeworkId[i][j]
            ur2 = f'{URL_HOMEWORK_DETAIL}?homeworkId= {c}'
            b = session.post(ur2, headers=headers).json()
            msg = {
                "课程名称": courseName[i],
                "作业标题": b['data']['homeworkName'],
                "截止时间": b['data']['homeworkDeadlineTime'],
                "作业网站": f"https://stu.z-xin.net/homework-detail/ {c}?cid={courseId[i]}&crmId={Id[i]}",
            }
            deadline = b['data']['homeworkDeadlineTime']
            judge(unfinishCount[i], deadline, msg, courseName[i])