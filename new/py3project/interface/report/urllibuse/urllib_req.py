# coding =utf -8
import urllib
import urllib2
url = 'http://www.cnblogs.com/poerli/p/6429673.html'
req = urllib2.Request(url,unverifiable=False)
read = urllib2.urlopen(req).read()
print read

# Pt2
import httplib
import urllib
url ="http://localhost:8888/cms"
json ={'key': 'value'}
urlencode = urllib.urlencode(json)
header ={'xxy':'uu'}
connection =httplib.HTTPConnection('localhost')
connection.request(method='POST',url =urlencode, body=urlencode,headers= header)
res = connection.getresponse()
read = res.read()

# pt3 =pt2 :
import urllib
import urllib2

json = {'key', 'value'}
url_encode = urllib.urlencode(json)
url_ = "http://192.168.81.16/cgi-bin/python_test/session.py"
req = urllib2.Request(url=url_, data=url_encode)
res = urllib2.urlopen(req)
read_lines = res.read()


