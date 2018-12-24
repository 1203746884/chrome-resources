# coding=utf-8
str = "abc"
str2 = "acc.txt"
str3 = "w2w3.wode.com"
s = """pass
papsd"""

print str.center(50,'#')
print str.ljust(20,'#')
print str.rjust(20, "#")
print str2.partition('.')
print str2.rpartition('x')
print s.splitlines()
print str2.rsplit('.', -1)
print str3.split('w', 2)
print str3.rpartition('w')
name = u'张三'


def defined():
    if isinstance(name,unicode):
        print name
defined()