# coding =utf-8
import os
import unittest
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner


def all_cases():
        case_path = os.getcwd()

        discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
        return discover


def run(report_path):
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title="interface report", description="results like following:", verbosity=2)
            runner.run(all_cases())
        f.close()


def timer(report_path, hour, minute):
    flag = 1
    while flag:
        while flag:
            now = datetime.datetime.now()
            if now.hour == hour and now.minute == minute:
                break
            time.sleep(10)
        # run(report_path)
        email_send(report_path)
        flag = 0


def email_send(report_path):
        run(report_path)
        msg_from = '1932390299@qq.com'  # sender
        passwd = 'qwynqamishiecjae'     # authentication  code
        msg_to = '1393232463@qq.com'    # receiver
        subject = "python_email_test"
        f = open(report_path, 'rb')
        mail_body = f.read()
        f.close()
        msg=MIMEText(mail_body, _subtype='html', _charset='utf-8')

        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("send success")
        except smtplib.SMTPException as e:
            print("send fail")
        finally:
            s.quit()
if __name__ == "__main__":
        job_name = time.strftime('job_%Y%m%d%H%M%S', time.localtime()) + '.html'
        path = os.path.join(os.path.dirname(__file__), 'report')
        # # path = os.path.join(r'C:\Users\Administrator\PycharmProjects\py3project\interface', 'report')
        report_path = os.path.join(path, job_name)
        email_send(report_path)

