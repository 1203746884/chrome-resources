# coding=utf-8
import yaml
import json
import ddt
import unittest
#https://blog.csdn.net/xuxunxiong954/article/details/80569881
#https://www.cnblogs.com/chendai21/p/8675982.html
"""写入yaml"""
with open('./dump.yaml','w') as f:
     d ={
        'student':{
            'name':'aa',
            'age':20,
            'love':{
                'ball':'volleyball',
                'book':'Python'
            }
        },
        'teacher':{
            'name': 'bb',
            'age': 20
        },
        'data':[2,3,4,5]
     }
     yaml.dump(d,f)

# """读取yaml内容"""
with open("./dump.yaml", 'r') as f:
    datas=yaml.load(f)
    print datas
# @ddt.ddt
# class Ymal(unittest.TestCase):
#
#     @ddt.file_data('./dump.yaml')
#     def test_my(self,**kwargs):
#         print kwargs
# if __name__=='__main__':
#     unittest.main(verbosity=1)