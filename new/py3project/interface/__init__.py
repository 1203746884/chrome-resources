# coding=utf-8

import requests
import json
# response1 = requests.get('http://httpbin.org/get')

# print(response1.text)
# 可以对比一下Json转化的和直接调用response的Json方法的区别print(response.json())
# print type((json.loads(response1.text))) # dict
# print type((response1.json()))
# print response1.cookies
# print (response1.content)  # string
# print (response1.text)  # unicode

# import requests

# data ={'name':'Arise','age':22}
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#
# response2 = requests.post('http://httpbin.org/post',data = data,headers = headers)
# print(response2.json())
# print response2.headers


# response5 = requests.get('http://www.baidu.com')
#相比urllib，就不需要声明任何变量print(response5.cookies)

# for key,value in response5.cookies.items():
#     print(key + '=' + value)
import json
import requests
s=requests.session()
url='http://www.pubwin.com.cn/tofrom2.jsp'
d={'url':'index.htm','userName':pbwid,'password':pbwpw}
r=s.post(url,data=d)