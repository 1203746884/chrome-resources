# coding=utf-8
class Class:
    """类变量为所有实例共享的变量"""
    var = "vars"

    def __init__(self,ggg,age):
                """实例变量为每个实例独有的属性变量"""
                self.ggg = ggg
                self.age = age
    def set(self):

                print test.ggg  # 实例对象来引用变量
                print self.var  # 引用类属性
                print self.ggg   # 引用实例变量
                print Class.var   # 引用类属性
    def get(self):
        print "xxx"
if __name__ =="__main__":
    test = Class('ggg','a11')
    print test.ggg ,test.age,test.var,Class.var
    # 使用实例对象引用属性稍微复杂一些，因为实例对象可引用类属性以及实例属性，总是先到实例对象中查找属性，再到类属性中查找属性；