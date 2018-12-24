# coding=utf-8
# URL:https://www.cnblogs.com/lovealways/p/6701662.html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
msg_from = '1932390299@qq.com'  # 发送方邮箱
passwd = 'qwynqamishiecjae'     # 填入发送方邮箱的开通smtp时的那个授权码
msg_to = '1393232463@qq.com'    # 收件人邮箱

subject = "python邮件测试"      # 主题
# content = "这是我使用python smtplib及email模块发送的邮件"  # 正文
file_new="d:\\name1.html"
f = open(file_new,'rb')
#  读取测试报告正文
mail_body = f.read()
f.close()


# 通过  模块构造的带附件的邮件如图
msg = MIMEMultipart()
# 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
# 发送正文
text = MIMEText(mail_body, 'html', 'utf-8')
text['Subject'] = Header('自动化测试报告', 'utf-8')
msg.attach(text)
# 发送附件
# Header()用于定义邮件标题
msg['Subject'] = Header('自动化测试报告', 'utf-8')
msg_file = MIMEText(mail_body, 'html', 'utf-8')
msg_file['Content-Type'] = 'application/octet-stream'
msg_file["Content-Disposition"] = 'attachment; filename="name1.html"'
msg.attach(msg_file)
# msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)  # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print("发送失败")
finally:
    s.quit()
