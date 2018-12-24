# coding=utf-8
class Test:
    def __init__(self, name):
        """_get_hobby一个下划线开头表示protected保护变量属性或者方法，只可以被类和子类调
           __age 双下划线开头表示private私有属性或者方法更加苛刻，只可以类内部调用不可以被外部调用
           没有下划线默认为public公共方法或变量，任何类方法都可以调
           私有属性方法访问不可以直接通过类的对象访问会抛异常，但是可以用instance._ClassName__method()来访问，属性则用
           instance._ClassName__age来访问
           protected属性方法访问，通过instance._method(),属性直接instance.attribute
        """
        self.name = name   # public attribute
        self.__age = 5      # private attribute
        self._get_hobby = "eat"  # protected attribute

    # private method
    def __get_age(self):
        return self.__age

    # protected method
    def _get(self):
        return self._get_hobby

if __name__ == "__main__":
    p = Test('candy')  # instance
    # print(p.__get_age() ) # 抛出异常，不能直接对象访问私有方法
    print p._Test__get_age(), p._Test__age  # 访问私有方法
    print p._get(), p._get_hobby   # 访问保护方法

