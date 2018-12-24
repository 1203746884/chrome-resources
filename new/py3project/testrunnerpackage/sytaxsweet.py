# coding =utf-8
import datetime
import time


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
# foo = timer(add)
# foo(4, 6)
print(add(4, 6))

# wrapper =timer(fn)
# wrapper(*args, **kwargs)
# offer x,y before  fn  after
