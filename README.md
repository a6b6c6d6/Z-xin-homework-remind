
# 知新作业截止提醒

每天 23:56 自动抓取“知新”平台上所有未交作业，若某项作业将在 648 h 内截止，则通过钉钉群机器人推送 Markdown 格式提醒。

## 功能
- 登录知新，自动拉取所有课堂及作业列表  
- 仅关注「未提交」且「648 h 内截止」的作业  
- 钉钉机器人加签安全模式，支持 Markdown 跳转链接（一键直达作业详情页）  
- GitHub Actions 定时运行，无需本地部署；也可手动 `workflow_dispatch` 触发

## 快速开始
1. Fork 本仓库  
2. 进入 Settings → Secrets and variables → Actions → New repository secret，依次添加：

| Secret 名称       | 说明 |
|------------------|------|
| `LOGIN_USERNAME` | 知新账号（手机号/学号） |
| `LOGIN_PASSWORD` | 知新密码 |
| `DING_ACCESS_TOKEN` | 钉钉群机器人 WebHook 中 `access_token=xxx` 部分 |
| `DING_SECRET`   | 钉钉机器人“加签”密钥（开启加签后可见） |

3. 默认每天 23:56 自动执行，如需改频率请修改 `.github/workflows/check.yml` 中的 `cron` 表达式  
4. 进入 Actions 面板可手动「Run workflow」立即测试

## 本地调试

 本地配置环境变量（.env）

1. 在项目根目录新建 `.env` 文件（文件名以点开头，无后缀）  
2. 写入以下内容，**等号左右不要留空格**：

```
LOGIN_USERNAME=你的知新账号
LOGIN_PASSWORD=你的知新密码
DING_ACCESS_TOKEN=钉钉机器人access_token
DING_SECRET=钉钉机器人加签密钥
```

3. 安装依赖  

pip install python-dotenv requests


4. 在 `main.py` 顶部添加两行代码：

```python
from dotenv import load_dotenv
load_dotenv()  # 自动加载 .env 到环境变量
```

5. 运行  
```
python main.py
```

终端出现「课程《xxx》暂无48小时内截止的作业或均已完成」即配置成功；钉钉收到 Markdown 提醒则整条链路已打通。


## 推送样例
⏰ 作业即将截止
•  课程名称：离散数学
•  作业标题：第十六周课后作业  哈密顿图，平面图和树
•  截止时间：2025-12-26 13:50:00
•  还剩 4天 5小时 51分钟 48秒 作业网站如下(xxxx)



## 注意事项
- 知新接口偶尔调整，如遇到 401/403 请提 Issue  
- 钉钉机器人每日限额 5000 条，正常学业场景足够  
- 本工具仅限个人学习管理使用，请勿用于商业或高频骚扰


##  License
MIT

