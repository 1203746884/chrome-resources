# coding=utf-8
import json
import requests
import unittest
class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.header={"Content-Type":  "application/json; charset=UTF-8"}
        data = {"userAccount": "admin", "loginPwd": "123456"}
        # global session
        session1 = requests.session()
        session1.post(url="http://192.168.229.128:8080/cms/manage/loginJump.do", data=data,headers=cls.header)
        # session =session1
        cls.session = session1
    @classmethod
    def tearDownClass(cls):
        pass

    def test_session(self):
        datas = {'userName': 'zhangsan', 'userEmail': '1932390299@qq.com',
                 'userMobile': '18871027706', 'userSex': '1','userAccount': 'dev', 'confirmPwd': '123456', 'loginPwd': '123456', 'id': ''}
        conn = self.session.post(url="http://192.168.229.128:8080/cms/manage/saveSysUser.do", data=datas,headers={"Content-Type": "text/html;charset=UTF-8"})
        print conn.content
if __name__ == "__main__":
    unittest.main()