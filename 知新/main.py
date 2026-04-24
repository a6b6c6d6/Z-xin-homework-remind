# main.py
import requests
from config import get_session_and_token, URL_CLASSROOM, URL_HOMEWORK_PAGE, URL_HOMEWORK_DETAIL, TERM_ID
from time_utils import time, parse_deadline
from helper import get_hw_count, judge
from dingtalk import send_ding

if __name__ == '__main__':
    session, token = get_session_and_token()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
        'zxin-ucenter-token': token,
        'Origin': 'https://stu.z-xin.net',
        'Referer': 'https://stu.z-xin.net/classroom',
        'Content-Type': 'application/json'
    }

    classroom_body = {
        'action': 'studentGet',
        'termId': TERM_ID
    }
    a = session.post(URL_CLASSROOM, headers=headers, json=classroom_body).json()

    q = len(a['data']) - 1
    Id = [item['id'] for item in a['data']]
    teacherCourseId = [item['teacherCourseId'] for item in a['data']]
    unfinishCount = [int(item['unfinishedCount']) for item in a['data']]
    courseName = [item['courseName'] for item in a['data']]

    homeworkId = []
    for i in range(q + 1):
        payload = {
            'action': 'studentPage',
            'classroomId': Id[i],
            'pageNum': 1,
            'pageSize': 20,
            'orderBy': 'createTime',
            'order': 'desc'
        }
        z = session.post(URL_HOMEWORK_PAGE, json=payload, headers=headers).json()
        aaa = [{
            'homeworkId': aa['id'],
            'answerProgress': int(aa.get('answerProgress', 0))
        }
            for aa in z.get('data', {}).get('records', [])]
        homeworkId.append(aaa)

    current_time = time()
    for i in range(q + 1):
        if unfinishCount[i] == 0:
            print(f'课程《{courseName[i]}》暂无未完成的作业')
            continue
        for j in range(get_hw_count(homeworkId, i)):
            c = homeworkId[i][j]['homeworkId']
            answerProgress = homeworkId[i][j]['answerProgress']

            payload2 = {
                'action': 'student',
                'homeworkId': c
            }
            b = session.post(URL_HOMEWORK_DETAIL, json=payload2, headers=headers).json()

            deadline_raw = b['data']['homework']['deadline']
            deadline = parse_deadline(deadline_raw)

            msg = {
                '课程名称': courseName[i],
                '作业标题': b['data']['homework']['name'],
                '截止时间': deadline,
                '作业网站': f'https://stu.z-xin.net/homework-detail/{c}?cid={teacherCourseId[i]}&crmId={Id[i]}',
            }

            judge(unfinishCount[i], deadline, msg, courseName[i], answerProgress)