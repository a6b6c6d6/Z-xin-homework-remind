import requests
import os

TERM_ID = "2015701567531511810"

def get_session_and_token():
    session = requests.Session()
    un = os.getenv("LOGIN_USERNAME")
    pw = os.getenv("LOGIN_PASSWORD")
    url = "https://auth.z-xin.net/api/portal/auth/login"
    payload = {"username": un, "password": pw}
    headers = {"user-agent": "Mozilla/5.0", "Content-Type": "application/json"}
    response = session.post(url, json=payload, headers=headers).json()
    if response.get("code") != 200:
        raise Exception("Login failed")
    token = session.cookies.get("zxin-ucenter-token")
    return session, token

URL_CLASSROOM = "https://stu.z-xin.net/api/classroom"
URL_HOMEWORK_PAGE = "https://stu.z-xin.net/api/homework"
URL_HOMEWORK_DETAIL = "https://stu.z-xin.net/api/homework/detail"