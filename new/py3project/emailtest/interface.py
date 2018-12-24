# coding=utf-8
import requests


def getToken():
    r = requests.post(
        url='https://ecapi.parkingwang.com/v4/login',
        json={"username": "autoapi",
              "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", "role":2},
        headers={'Content-Type':'application/json;charset=UTF-8', 'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'}
        , timeout=5)
    print (r.json()['data']['token'])


def info_get():
    r = requests.post(
        url='https://ecapi.parkingwang.com/v4/infoGet',
        json={"token": getToken()},
        headers={'Content-Type': 'application/json;charset=UTF-8', 'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'}
        , timeout=5)  # 通过json添加进去token，在进行需登录的接口请求
    print (r.json())
if __name__ == "__main__":
    getToken()
    info_get()
# def isSoonExpire():
#     r=requests.post(
#         url='https://ecapi.parkingwang.com/v4/isSoonExpire',
#         json={"token": getToken()},
#         headers={'Content-Type': 'application/json;charset=UTF-8',
#         'Parkingwang-Client-Source': 'ParkingWangAPIClientWeb'}
#         , timeout=5)
#     print(r.json())  # 也是通过json添加进去token，在进行需登录的接口请求
#
#
#
# import requests
# import  unittest
# import  time as t
#
# class InterfaceTest(unittest.TestCase):
#     def setUp(self):
#         self.url='https://ecapi.parkingwang.com/v4/'
#         self.headers={'Content-Type':'application/json;charset=UTF-8','Parkingwang-Client-Source':'ParkingWangAPIClientWeb'}
#         self.timeout=5
#
#     def tearDown(self):
#         t.sleep(1)
#
#     def getToken(self):
#         r = requests.post(
#             url=self.url+'login',
#             json={"username": "autoapi", "password":
#  "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92","role": 2},
#             headers=self.headers, timeout=self.timeout)
#         return r.json()['data']['token']
#
#     def test_infoGet(self):
#         '''验证:测试infoGet接口是否正确'''
#         r = requests.post(
#             url=self.url+'infoGet',json={"token": self.getToken()},headers=self.headers, timeout=self.timeout)
#         self.assertEqual(r.json()['status'],0)
#         self.assertEqual(r.json()['data']['username'],'autoapi')
#
#     def test_isSoonExpire(self):
#         '''验证：测试isSoonExpire接口是否正确'''
#         r = requests.post(
#             url='https://ecapi.parkingwang.com/v4/isSoonExpire',
# json={"token":self.getToken()},headers=self.headers, timeout=5)
#         self.assertEqual(r.json()['status'],0)
#         self.assertEqual(r.json()['data']['expire'],False)
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
# """执行上面的测试用例后，我们发现二个测试用例都调用了getToken()方法，而getToken()方法我们知道是登录的接口，登录成功后
#
# 获取token，言外之意也就是说登录了二次，缺点很明显，如果在N个测试用例，参数都需要token，都会调用getToken()，那么也会
#
# 出现登录N次，很实现这个方法不是我们想要的，我们要实现的是不管有多少个接口测试用例，登录只能是一次，如果登录多次，会
#
# 出现token无效502的问题，或者引起其他的问题，在这里我们把登录成功后的token存储在文件中，然后从文件中读取，这样就可以
#
# 登录一次，见实现的代码"""
