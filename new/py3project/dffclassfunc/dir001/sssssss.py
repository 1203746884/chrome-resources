# coding=utf-8
import requests
import json
import ddt
import unittest

@ddt.ddt
class OverRide(unittest.TestCase):
    test_data =[('method','url','data','header','param','type'),('method','url','data','header','param','type')]

    @classmethod
    def setUpClass(cls,method,url,data,header,param,type):
        cls.method =method
        cls.url = url
        cls.data = data
        cls.header = header
        cls.param = param
        cls.type = type
        global session
        s = requests.session()
        requests.post(url="http://xxx",data={'user': "admin","pwd": "123456"},headers={"Content-Type": "application/x-www-form-urlencoded"})
        session =s

    @classmethod
    def tearDownClass(cls):
        """清除cookie"""
        session.cookies.clear()  #也可以这样写 session.cookies=None

    @ddt.data(*test_data)
    def send_request(self,test_data):
        self.method=eval(test_data['method'])
        self.url = eval(test_data['url'])
        self.data =eval(test_data['data'])
        self.header = eval(test_data['header'])
        self.param = eval(test_data['param'])
        self.type = eval(test_data['type'])
        method =self.method
        url=self.url
        if self.method.upper() =="POST":
            param=None
            header=self.header

            if self.type == "json":
                js =None
                data=json.dumps(self.data)  #""" Origin data is dict"""
                # js =self.data
                #  data=None
            elif self.type == "data":
                data=self.data            # x-www-urlencoded
                js=None
            else:
                js=None
                data=self.data
        elif self.method.upper() == "GET":
            header =None
            js=None
            data=None
            if self.param == '':
                param=None
            else:
                param =self.param
        response = session.request(method=method,url=url,data=data,json=js,headers=header,param=param)
        times_out=response.elapsed.total_seconds()
        content= response.content.decode('utf-8')
        dict=[]
        dict['times_out']=times_out
        dict['response']=content
        return dict
    def get_request(self):
        pass
    def args_kwargs(self,*args,**kwargs):
        list=[]
        dict={}
        for arg in args:
            list.append(arg)
        for key,value in kwargs.items():
            dict[key]=value
        return dict,list
if __name__ == "__main__":
    test_data =[('method','url','data','header','param','type'),('method','url','data','header','param','type')]
    override =OverRide()
    override.send_request()
