# coding =utf-8
import datetime
import time

# """method.decorator""""
def timer(fn):
    def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            fn_foo = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > 2:
                print ("{}:{}s".format(fn.__name__, delta))
            return fn_foo
    return wrapper


@timer
def add(x, y):
    time.sleep(3)
    return x + y
foo = timer(add)
foo(4, 6)
print(add(4, 6))

# wrapper =timer(fn)
# wrapper(*args, **kwargs)


# """class.method decorator"""


def decorator(fn):
    def wrapper(self,var):
        fn_foo = fn(self,var)
        return fn_foo
    return wrapper


class Foo(object):
    def __init__(self, name):
        self.age = 36
        self.name = name

    @decorator
    def fn(self, string):
        print "i am class.fn that be decorated:" + string

Foo('zs').fn('variable')


# part3: the decorator with args
def decorates(*dec_args, **dec_kwgrgs):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            fn_foo = fn(*args, **kwargs)
            return fn_foo
        return wrapper
    return decorator

var1_dec = 'var_dec1'
var2_dec = 'var_dec2'


@decorates(var1_dec, var2_dec)
def fxx(fxx_var1, fxx_var2):
    print "decorator.var1:{},decorator.var2:{}####fxx.var1:{},fxx.var2:{}" .format(var1_dec,var2_dec,fxx_var1,fxx_var2)
fxx('tom', 'jack')

# many decorators


def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01 start")
        func(*args, **kwargs)
        print("deco01 end here")
    return wrapper


def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02 start")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper


@deco02
@deco01
def func(x, y):
    print "result is {}".format(x+y)

func(3, 4)
