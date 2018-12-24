# coding=utf-8

"""pt1:内部修改全局变量"""
class GlobalParas():
    name = "pig"  # 全局外部
    def call_name(self):

        global name
        name = "fish"   # 全局变量内部
        print name
print GlobalParas().name  #pig
GlobalParas().call_name()  #fish 在函数内部修改全局这一步执行意味着外部全局name变为内部global声称的，后边都得用我内部声称的全局变量
print name  #fish 使用外部修改后的全局变量，

"""pt2: 外部修改全局变量"""

class GlobalVar():
    names = "mm"
    def __init__(self):
         pass
    def call_name(self):
        global names
        names = "gg"
        return names
print GlobalVar().call_name() #gg
print names # gg
names = "jj"
print "pt2 的全局变量是: {}".format(names)  # jj
print GlobalVar().call_name() # gg
print names  # gg

"""pt3: 全局遇上局部"""
face = "handsome"
def see_face():
    face = "ugly"
    print face
see_face()  # ugly  在内部还是听丑的
print face # handsome 外部还是听帅的

"""pt4: 来点骚操作SyntaxWarning: name 'feature' is assigned to before global declaration
  global  feature"""
feature = "have money"
def wealthy():

    feature = "poor"  # 错在这儿
    global  feature
    feature = "very poor"
    print feature
wealthy()
print feature

""" pt5：外部访问内部变量显示未定义NameError: global name 'hobby' is not defined"""
#hobby = "sleep"
def test_hobby():
    global hobby
    hobby = "eat"
    hobby = "run"
    print hobby
print hobby
test_hobby()

"""pt6:赋值之前引用的局部变量“i”UnboundLocalError: local variable 'i' referenced before assignment"""
i =0
def foo():
    print i  #局部变量在使用前没有赋值，因为变量都是从内向外找的，内部没有跑外部找找到为止，否则exception
    i = 9
foo()











