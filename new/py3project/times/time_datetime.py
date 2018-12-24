# coding =utf-8
import time
import datetime
import requests
# requests.packages.urllib3.disable_warnings()
r = requests.get('https://www.baidu.com/', verify=False)
# print(r.text)
# print(time.time())
# print(time.ctime())
# print(time.localtime())
print(time.strftime('job_%Y%m%d%H%M%S', time.localtime()))
# print(datetime.datetime.now())
# print(datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S'))
# now = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime())
# import os
# print(os.listdir(r'C:\Users\Administrator\PycharmProjects\py3project\times'))