# coding=utf-8

import unittest


class ClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("starting before all method,i just do one times")

    @classmethod
    def tearDownClass(cls):
        print("ending after all method ended,i just do one times")

    def setUp(self):
        print("prepare  before every method,must execute me one times")

    def tearDown(self):
        print("ending after each method finish ,must execute me one time")

    # tip:python 测试用例必须以test开头
    def test_method1(self):
        print("i am method 1")

    def test_method2(self):
        print("i am method2")
if __name__ == "__main__":
    unittest.main()
