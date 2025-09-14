# dingtalk.py
import requests
import json
import time
import hmac
import hashlib
import base64
import os
import urllib.parse
DING_WEBHOOK = "https://oapi.dingtalk.com/robot/send"
ACCESS_TOKEN = os.getenv("DING_ACCESS_TOKEN")
SECRET       = os.getenv("DING_SECRET")       
def _get_sign() -> str:
    """钉钉加签算法，返回 timestamp 和 sign 拼好的 url 参数串"""
    timestamp = str(round(time.time() * 1000))
    secret_enc = SECRET.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, SECRET)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return f"&timestamp={timestamp}&sign={sign}"

def send_ding(msg_dict: dict):
    """入口保持和以前完全一致，外面无需任何改动"""
    title = "⏰ 作业即将截止"
    text = (
        f"### {title}\n"
        f"- 课程名称：{msg_dict['课程名称']}\n"
        f"- 作业标题：{msg_dict['作业标题']}\n"
        f"- 截止时间：{msg_dict['截止时间']}\n"
        f"[作业网站如下]({msg_dict['作业网站']})"
    )
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": title,
            "text": text
        }
    }
    # 拼出带签名的完整 url
    url = f"{DING_WEBHOOK}?access_token={ACCESS_TOKEN}{_get_sign()}"
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(payload), headers=headers)