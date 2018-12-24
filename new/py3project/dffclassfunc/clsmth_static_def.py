# coding:utf-8
class Test(object):
    """walk 为普通方法只能被对象instance调用，play 为静态方法可以被对象和ClassName调用，
        eat为类方法，可以被对象和ClassName调用。
        此外PEP8中一种编程风格，self通常用作实例方法的第一参数，cls通常用作类方法的第一参数;
        即通常用self来传递当前类对象的实例，cls传递当前类对象,self和cls的不是强制的,staticmethod第一参数可以不传
    """

    def __init__(self, name):
        self.age = 33
        self.name = name

    def walk(self, place):
        print place, self.walk.__name__, self

    @staticmethod
    def play(string):
        print string

    @classmethod
    def eat(cls, food):
        print food, cls, cls.walk.__name__
if __name__ == "__main__":
    instance = Test("ShangHai")
    instance.walk("huangpu_river")
    instance.play("fire")
    Test.play("water")
    instance.eat("apple")
    Test.eat("banana")
