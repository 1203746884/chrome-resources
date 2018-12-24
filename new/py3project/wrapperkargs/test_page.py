# coding=utf-8
import unittest
from selenium import webdriver
from basic_info import PageObject
from time import sleep


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        sleep(1)
        # cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.name = "zhangsan"
        sleep(2)
        cls.url="http://192.168.229.128:8080/cms/manage/login.do"
        cls.driver.get(cls.url)
        sleep(1)
        # PageObject(cls.driver).login()
        print" i am class method ,do i before all method start"

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.close()
        print "i am class method ,do i after all method finished"

    def test1_login(self):
        u"用户登录"
        PageObject(self.driver).login()

    def test2_action(self):
        u"用户点击"
        PageObject(self.driver).test().click()
        print "success"

    def test3_class(self):
        u"调试"
        print "class.attribute:{},class.dui_xiang:{}".format(self.name, self)

if __name__ == "__main__":
    unittest.main(verbosity=2)
