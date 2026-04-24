import os
import requests

def gettoken(session):
    """
    新登录API: POST https://auth.z-xin.net/api/portal/auth/login
    token通过cookie zxin-ucenter-token自动获取，不再返回satoken
    返回 (session, token)
    """
    un = os.getenv('LOGIN_USERNAME')
    pw = os.getenv('LOGIN_PASSWORD')
    url = "https://auth.z-xin.net/api/portal/auth/login"
    payload = {
        "username": un,
        "password": pw
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
        "Content-Type": "application/json"
    }
    response = session.post(url, json=payload, headers=headers).json()
    if response.get("code") != 200:
        raise Exception(f"登录失败: {response}")
    # token通过cookie获取
    token = session.cookies.get("zxin-ucenter-token")
    return token