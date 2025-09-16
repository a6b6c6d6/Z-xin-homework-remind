import os         
from gettoken import gettoken
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "zxin-ucenter-token": gettoken(),
}
URL_CLASSROOM = "https://v3.api.z-xin.net/classroom/studentGetClassroom"
URL_HOMEWORK_PAGE = "https://v3.api.z-xin.net/homework/studentGetHomeworkPage"

URL_HOMEWORK_DETAIL = "https://v3.api.z-xin.net/homework/getHomeworkDetail"

