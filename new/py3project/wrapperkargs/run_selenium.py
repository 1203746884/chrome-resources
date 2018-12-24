# coding =utf-8
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
import time


class TestSuiteRun(object):

    def add_suites(self):
        cur_path =os.getcwd()
        suites = unittest.defaultTestLoader.discover(cur_path, pattern='test*.py', top_level_dir=None)
        return suites
        # unit = unittest.TestSuite()
        # for suite in suites:
        #     print suite
        #     for case in suite:
        #         print case
        #         unit.addTests(case)
        # print unit
        # return unit

    def run(self, report_path):
            with open(report_path, 'wb') as f:
                runner = HTMLTestRunner(stream=f, title="interface report",
                                        description="results like following:", verbosity=2)
                runner.run(self.add_suites())
            f.close()
if __name__ ==  "__main__":
    job = time.strftime("%Y%m%M%H%M%S", time.localtime(time.time()))
    report_path = r"C:\Users\Administrator\PycharmProjects\py3project\wrapperkargs\{}_report.html".format(job)
    testsuiterun = TestSuiteRun()
    testsuiterun.run(report_path)
