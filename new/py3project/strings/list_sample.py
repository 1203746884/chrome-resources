# coding =utf-8
import random

print random.randint(1, 10)  # a<=x<=b
print random.randrange(1, 3)  # a<=x<b
print random.random()  # 0<= x <1
print random.randrange(1, 5, 2)  # a<=x <b
# s = u'\xb3\xc2\xbd\xa8\xc3\xf4'
# a = s.encode('unicode_escape').decode('string_escape')
s = u'\xb3\xc2\xbd\xa8\xc3\xf4'
print s.encode('raw_unicode_escape')