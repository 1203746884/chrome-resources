# coding=utf-8
import os
"""
print os.listdir(os.getcwd())  # get dir all files
print os.path.dirname(__file__)，获取文件的父目录路径
print os.path.abspath(__file__)  # get pwd获取绝对路径文件的.py
print os.path.dirname(os.path.abspath(__file__))   # get dir of pwd 获取绝度路径的父目录
print os.path.realpath(__file__)  # get pwd 获取真实路径同绝对路径
print os.getcwd()  # get current dir path 获取当前目录的父目录路径
"""


def get_filename(path):
    lists = []
    files = os.listdir(path)
    for i in files:
        file_path = os.path.join(path, i)
        if os.path.isdir(file_path):
            get_filename(file_path)
        lists.append(file_path)

    return lists


def count_file(path):
    count = 0
    list_file = get_filename(path)
    for j in list_file:
            count += 1
    return count

# print count_file(r'C:\Users\Administrator\PycharmProjects\py3project\interface')
# print get_filename(r'C:\Users\Administrator\PycharmProjects\py3project\interface')

path = os.getcwd()
for parent,dirnames,filenames in os.walk(path):
    for dirname in dirnames :
        print os.path.join(parent,dirname)
    for filename in filenames:
        print os.path.join(parent, filename)





