# coding=utf-8
import requests
import json
import ddt
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from ReadExcel import Excel

path=r"f://myexcel.xlsx"
st_name='Sheet1'
test_data= Excel(path,st_name).read_excel()

def run():
        suites=unittest.defaultTestLoader.discover('./',pattern='test*.py',top_level_dir=None)

        report_path='./report.html'
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title="interface report", description="results like following:",verbosity=1)
            runner.run(suites)
        f.close()
@ddt.ddt
class OverRide(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # global session
        # s = requests.session()
        # requests.post(url="http://xxx",data={'user': "admin","pwd": "123456"},headers={"Content-Type": "application/x-www-form-urlencoded"})
        # session =s
        print "---------------开始加载--------------"
    @classmethod
    def tearDownClass(cls):
        """清除cookie"""
        # session.cookies.clear()  #也可以这样写 session.cookies=None
        print "----------------释放完成-------------"
    @ddt.data(*test_data)
    def test_data(self,dict):
        self.test_name=dict['test_name']
        self.method=dict['method'].upper()
        self.url = dict['url']
        self.data =eval(dict['data'])
        self.header = eval(dict['header'])
        self.param = eval(dict['param'])
        self.type = dict['type']
        print "当前执行用例名称：{}".format(self.test_name), time.asctime()
        print self.test_name,self.method,self.data,self.header,self.param,self.type
        #method =self.method
        # url=self.url
        # if self.method.upper() =="POST":
        #     param=None
        #     header=self.header
        #
        #     if self.type == "json":
        #         js =None
        #         data=json.dumps(self.data)  #""" Origin data is dict"""
        #
        #     elif self.type == "data":
        #         data=self.data            # x-www-urlencoded
        #         js=None
        #     else:
        #         js =None
        #         data=self.data
        # elif self.method.upper() == "GET":
        #     header =None
        #     js=None
        #     data=None
        #     if self.param == '':
        #         param=None
        #     else:
        #         param =self.param
        # response = session.request(method=method,url=url,data=data,json=js,headers=header,param=param)
        # times_out=response.elapsed.total_seconds()
        # content= response.content.decode('utf-8')
        # dict=[]
        # dict['times_out']=times_out
        # dict['response']=content
        # return dict

if __name__ == "__main__":
    # run()
    unittest.main(verbosity=1)
