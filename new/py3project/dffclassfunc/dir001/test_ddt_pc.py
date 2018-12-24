# coding=utf-8
import ddt
import unittest
import time
from  HTMLTestRunner import HTMLTestRunner
dts1='{"key": "value"}'
dts2='fn'
test_data =[('test_name','post','https://www.douban.com','{"key": "value"}','{"Content-Type": "text/plain;charset=UTF-8"}','{"projectName": "pipe", "jobId": "70558866DFF6567A"}','data'),
            ('test_name2','get','https://www.douban.com','{"key": "value"}','{"Content-Type": "text/plain;charset=UTF-8"}','{"projectName": "pipe", "jobId": "60558866DFF6567B"}','json')]
test_tuple=[(dts1,dts2)]
test_name=['fn_name']
test_list=[['str1','str2','str3'],['st1','st2','st3']]
test_dict= [{"username": "zhangsan", "pwd": "zhangsan"},
             {"username": "lisi", "pwd": "lisi"},
             {"username": "wangwu", "pwd": "wangwu"},
             ]
def run():
        suites=unittest.defaultTestLoader.discover('./',pattern='test*.py',top_level_dir=None)

        report_path='./report.html'
        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, title="interface report", description="results like following:",verbosity=2)
            runner.run(suites)
        f.close()
@ddt.ddt
class  Test(unittest.TestCase):
    @ddt.data(*test_data)
    @ddt.unpack
    def test_data(self,test_name,method,url,dict,header,param,type):
        # print test_name,method,url,eval(dict),eval(header),eval(param),type,time.asctime()
        print ""
    @ddt.data(*test_list)
    def test_list(self,var):
        print var

    @ddt.unpack
    @ddt.data(*test_tuple)
    def test_tuple(self,dts1,dts2):
        u"测试接口实验"
        print dts1,dts2

    @ddt.data(*test_dict)
    def test_dict(self,dict):
        print dict.get('username',None)
    def test_7fff(self):
        u"xxxxxxxxxxxx"
        print "ffffffffffffffff"

if __name__ == "__main__":
    run()