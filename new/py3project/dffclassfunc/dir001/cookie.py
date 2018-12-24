# coding=utf-8
import cookielib
import urllib2
import requests

class CookieClass(object):
    def __init__(self,url):
        self.url=url

    """cookie_object:用来声明一个cookie对象来保存cookie；
       handler:用来保存获取句柄打开的网页的cookie到cookie_object对象的一个处理器；
       opener:一个用来打开直制定网页一个句柄
    """
    def cookie_object(self):
        cookie_object=cookielib.CookieJar()
        handler=urllib2.HTTPCookieProcessor(cookie_object)
        opener=urllib2.build_opener(handler)
        opener.open(self.url,timeout=5)
        for item in cookie_object:
            print item.name,item.value,item.domain,item.path

    """file_cookie_object: 声明一个文件对象来保存cookie;
    ignore_discard=True: 将被丢弃的cookie会被保存,
    ignore_expires=True： ./cookie.txt已存在cookie,新的cookie会覆盖旧的
    """
    def file_cookie_object(self):
        file_name="./cookie.txt"
        file_cookie_object=cookielib.MozillaCookieJar(file_name)
        handler=urllib2.HTTPCookieProcessor(file_cookie_object)
        opener=urllib2.build_opener(handler)
        opener.open(self.url,timeout=5)
        file_cookie_object.save(ignore_discard=True,ignore_expires=True)

    """load读取文件保存cookie"""
    def load_file_cookie(self):
        self.file_cookie_object()
        # 对象用来保存读取的cookie
        cookies =cookielib.MozillaCookieJar()
        cookies.load('./cookie.txt',ignore_expires=True,ignore_discard=True)
        handler=urllib2.HTTPCookieProcessor(cookies)
        opener=urllib2.build_opener(handler)
        opener.open(self.url,timeout=5)
        print cookies

    """拓展：cookie增删改查"""
    def operate_cookie(self):
        session =requests.session()
        session.get(self.url)
        # add cookies
        session.cookies.set("key","value")
        # del cookie另一种写法
        session.cookies.set("key", None)
        # get cookies
        cookies=session.cookies.get_dict()
        # del cookies 两个方法都可以下面
        # session.cookies=None
        session.cookies.clear()
        """update cookies ,此方法在跳过验证很有用前提你先要手动登录一次获取session,当然UI自动化会用driver.add_cookie（{"key": ,"value"}）
        连续添加username,pwd的cookie键值对解决跳过验证码滑块,前提都是要获取一次登陆后的session再来进行抓包添加新增cookie解决"""
        obj =requests.cookies.RequestsCookieJar()
        obj.set("key", "value")
        session.cookies.update(obj)
if __name__ == "__main__":
    url="http://www.douban.com"
    cookie = CookieClass(url)
    cookie.load_file_cookie()