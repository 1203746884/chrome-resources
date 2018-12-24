# coding=utf-8
# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Chen"
__version__ = "0.8.2"

"""
   由于 HTMLTestRunner 是基于python2开发的，所以在python3调用生成测试报告出现不兼容问题，解决方案如下：
   第94行，将import StringIO修改成import io
   第539行，将self.outputBuffer = StringIO.StringIO()修改成self.outputBuffer = io.StringIO()
   第642行，将if not rmap.has_key(cls):修改成if not cls in rmap:
   第766行，将uo = o.decode('latin-1')修改成uo = e
   第772行，将ue = e.decode('latin-1'   )修改成ue = e
   第631行，将print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改成
   print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))
"""