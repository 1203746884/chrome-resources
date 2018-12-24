# coding=utf-8
from selenium import webdriver
import unittest


class Login(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
                cls.driver = webdriver.Chrome()
                cls.driver.maximize_window()
                cls.driver.implicitly_wait(30)
                cls.driver.get('https://www.baidu.com/')

        def test01(self):
                u'验证网页title是否正确'
                self.assertTrue(str(self.driver.title).startswith('百度一下'))

        def test02(self):
                u'验证网址是否正确'
                self.assertEqual(self.driver.current_url, 'https://www.baidu.com/')

        @classmethod
        def tearDownClass(cls):
                # cls.driver.quit()
                pass

        @staticmethod
        def suite():
                suite = unittest.makeSuite(Login)  # 传入类名Login
                return suite

        # @staticmethod
        # def suite():
        #     suite=unittest.TestLoader.loadTestsFromTestCase(Login)  # 传入的也是类名
        #     return suite

if __name__ == '__main__':
        unittest.TextTestRunner(verbosity=2).run(Login.suite())
