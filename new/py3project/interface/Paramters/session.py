# coding=utf-8
import requests
import json
import unittest


class Interface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        req = requests.post(url="http://192.168.229.128:8080/cms/manage/loginJump.do",
                            data={"userAccount": "admin", "loginPwd": "123456"})
        global cookie
        cookie = req.cookies.get_dict()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login(self):
        u"登录平台接口"
        req = requests.post(url="http://192.168.229.128:8080/cms/manage/loginJump.do",
                            data={"userAccount": "admin", "loginPwd": "123456"})
        dicts = json.loads(req.content)
        try:
            self.assertEqual(dicts['msg'], u"登录成功！", "status:200")
        except AssertionError as e:
            print(e)
        else:
            results = req.json()
            print results

    def test_cookie_request(self):
        u"保存用户接口"
        datas = {'userName': 'zhangsan', 'userEmail': '1932390299@qq.com',
                 'userMobile': '18871027706', 'userSex': '1','userAccount': 'dev', 'confirmPwd': '123456', 'loginPwd': '123456', 'id': ''}
        conn = requests.post(url="http://192.168.229.128:8080/cms/manage/saveSysUser.do", data=json.dumps(datas), cookies=cookie)
        result = conn.json()
        print result
if __name__ == "__main__":
    unittest.main()