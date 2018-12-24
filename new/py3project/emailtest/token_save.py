# coding:utf-8
import requests
import unittest
import time
import os
import datetime
import smtplib
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner

def getHeaders():
    """获取headers"""
    return {'Content-Type':'application/json;charset=UTF-8','Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}


def login():
    """把token字符串写入到文件中"""
    uri = 'https://ecapi.parkingwang.com/v4/'
    r = requests.post(
        url=uri + 'login',
        json={"username": "autoapi", "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
              "role": 2},
        headers=getHeaders(), timeout=5)
    with open(base_dir(), 'w') as f:
        f.write(r.json()['data']['token'])
    return r.json()['data']['token']

def base_dir():
    '''返回toeken文件的目录文件保存绝对地址'''
    return os.path.join(os.path.dirname(__file__), 'token.md')

def getToken():
    '''读取存储在文件中的token'''
    with open(base_dir(),'r') as f:
        return f.read()

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.url='https://ecapi.parkingwang.com/v4/'

    def tearDown(self):
        time.sleep(1)

    def test_infoGet(self):
        '''验证:测试infoGet接口是否正确'''
        r = requests.post(url=self.url+'infoGet',json={"token": getToken()},headers=getHeaders(), timeout=5)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['username'],'autoapi')

    def test_isSoonExpire(self):
        '''验证：测试isSoonExpire接口是否正确'''
        r = requests.post(url=self.url+'isSoonExpire',json={"token":getToken()},headers=getHeaders(), timeout=5)
        self.assertEqual(r.json()['status'],0)
        self.assertEqual(r.json()['data']['expire'],False)

    def all_case(self):
        case_path = os.path.join(os.getcwd(),'case')

        discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py', top_level_dir=None)
        return discover

    def run_case(self):
        global filename
        filename=os.path.join(os.path.dirname(__file__),'report')

        now = time.strftime("%Y-%m-%d-%H_%M_%S")
        report_path = filename + now + '.html'
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title="interface report", description=" results like following:")
            runner.run(self.all_case())
        f.close()

    def sendmail(self):
        msg_from = '1932390295@qq.com'  # 发送方邮箱
        passwd = 'qwynqamishiecjae'     # 填入发送方邮箱的开通smtp时的那个授权码
        msg_to = '1393232463@qq.com'    # 收件人邮箱

        subject = "python邮件测试"      # 主题

        f = open(filename, 'rb')
        mail_body = f.read()
        f.close()
        msg=MIMEText(mail_body, _subtype='html', _charset='utf-8')

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

    def timer(self,h=23 ,m=48):
        flag = 1
        while flag:
            # 判断是否达到设定时间，例如0:00
            while flag:
                now = datetime.datetime.now()
                # 到达设定时间，结束内循环
                if now.hour == h and now.minute == m:
                    break
                # 不到时间就等10秒之后再次检测
                time.sleep(10)
            # 做正事，一天做一次

            self.run_case()
            flag = 0


if __name__ == '__main__':
    unittest.main()



    # session ：我发给你一张身份证，但只是一张写着身份证号码的纸片。你每次来办事，我去后台查一下你的 id 是不是有效。
    # token ：  我发给你一张加密的身份证，以后你只要出示这张卡片，我就知道你一定是自己人。
