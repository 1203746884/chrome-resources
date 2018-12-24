# coding=utf-8
from logging_dealwith import TestLogger

logs = TestLogger('./logs').console_log()


class Test(object):
    var = "variable"

    def __init__(self, name, feature):
        self.name = name
        self.feature = feature
        self.age = 22

    def walk(self, place):
        print place

    @staticmethod
    def play(string):
        print string
        logs.info("addfbjjfhhn")

    @staticmethod
    def eat(food):
        print food

    @classmethod
    def drink(cls, drinker):
        print drinker
if __name__ == "__main__":
    # Test("myself", "handsome").walk("paris")
    # Test("myself", "handsome").play("str")
    # Test.eat("banana")
    # Test("myself", "handsome").drink("water")
    # Test.drink("soup")
    a = Test("myself", "handsome")
    b = Test("myself", "handsome")
    a.play("sssss")
print Test("ss", "ff").var
print a.age, b.age
print (a is b)
print (a == b)


