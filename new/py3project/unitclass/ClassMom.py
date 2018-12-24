# coding =utf-8
class ClassMom(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    # public method
    def method(self):
        print self.__name
        print ClassMom.test()  # class.method
        print self.test()     # instance.method

    # private method
    def __get_age(self):
        print " i am private method "

    @staticmethod
    def test():
        return "test"

    def method2(self):
        return self.__name
class_mom = ClassMom("administer", 19)
print class_mom.method2()
class_mom.method()
# print class_mom.__name
print ClassMom.method2(class_mom)
# class_mom.__get_age()    # instance can not greet private method
class_mom._ClassMom__get_age()   # instance._class__method()
print class_mom._ClassMom__name  # instance,_class__attribute




