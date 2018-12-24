# coding=utf-8
class Tea:
    var = 0

    def __init__(self, name):
        self.name = name
        self.age = 3
        print self.__class__.var

    @classmethod
    def get(cls):
        print cls.var

    @staticmethod
    def add(x, y):
        # z = Tea('ss').age  # self.age 实例属性通过实例调
        return x+y

    def set(self):
        print self.__class__.name

if __name__ == "__main__":
    print Tea.add(1, 2)
    # print Tea.age  # 报错 class has no attribute
    print Tea.var


class Foo(object):
    def __init__(self):
        self.var = 1

    def hi(self):
        print 's'


class Foo2(Foo):
    def __init__(self, var_foo2):
        Foo.__init__(self)   # 调父类__init__
        print self.var
        self.var_foo2 = var_foo2
