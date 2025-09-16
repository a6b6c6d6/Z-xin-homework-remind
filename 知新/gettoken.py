import os
import requests
def gettoken():
    un = os.getenv('LOGIN_USERNAME')
    pw = os.getenv('LOGIN_PASSWORD')
    url="https://auth.z-xin.net/api/user/loginByPassword"
    payload={
        "password":pw,
        'username' :un
    }
    headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    }
    response=requests.post(url,json=payload,headers=headers).json()
    token=response['data']['satoken']
    return token
