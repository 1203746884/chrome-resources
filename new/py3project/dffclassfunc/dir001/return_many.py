# coding=utf-8
import ddt
import unittest
test_data=[{"k1": "v1"},{"k2": "v2"}]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*test_data)
    def  test_dict(self,dict):
        print dict
if __name__ == "__main__":
    unittest.main(verbosity=2)