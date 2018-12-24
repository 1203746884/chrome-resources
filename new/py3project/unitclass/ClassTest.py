# coding = utf-8
import unittest


class ClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start....")

    @classmethod
    def tearDownClass(cls):
        print("ending....")

    def setUp(self):
        print("BeforeMethod")

    def tearDown(self):
        print("AfterMethod")

    @staticmethod
    def test1():
        print("####test1")

    @staticmethod
    def test2():
        print("##test2###")
# class ClassUse(unittest.TestCase):


if __name__ == "__main__" :
    unittest.main()
