# coding =utf-8
class ClassGrandma(object):

    @staticmethod
    def get_age():
        print"ordinary method"

    @staticmethod
    def __private_method():
        print u"privatemethod "
ss =ClassGrandma()
ss._ClassGrandma__private_method()