# coding=utf-8
import requests
import unittest
import json
import urllib3
from ddt import ddt,data,unpack
urllib3.disable_warnings()
#application/x-www-urlencoded

test_data=[("http://192.168.229.128:8080/cms/manage/loginJump.do",{"Content-Type": "application/json;charset=UTF-8"},
           "POST",{"userAccount": "admin", "loginPwd": "123456"}),("http://192.168.229.128:8080/cms/manage/saveSysUser.do",{"Content-Type": "application/json;charset=UTF-8"},"POST",{"userName": "zhangssan", "userEmail": "1932390299@qq.com","userMobile": "18871027700", "userSex": "1","userAccount": "dev3", "confirmPwd": "123456", "loginPwd": "123456", "id": ""})]
@ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        r =requests.post(url="http://192.168.229.128:8080/cms/manage/loginJump.do",data={"userAccount": "admin", "loginPwd": "123456"})
        global  cookie
        cls.cookie =r.cookies.get_dict()
    @classmethod
    def tearDownClass(cls):
        pass
    @data(1,2,3)
    def test_ddt(self,num):
       try:
          self.assertTrue(num > 1)
          print "ok"
       except Exception:
          print "失败"
    @data((1,2),(1,3))
    @unpack
    def test_unpack(self,var1,var2):
        try:
            self.assertEqual(var1+1,var2)
            print "True"
        except Exception as e:
            print e
    @data(*test_data)  # import ddt @ddt.data(*test_data)
    @unpack
    def test_requests(self,url,header,method,data):
        pass
if __name__ == "__main__" :
    unittest.main(verbosity=2)
