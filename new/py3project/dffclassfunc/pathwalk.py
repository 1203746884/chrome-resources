# coding=utf-8
import os
path = os.getcwd()
list1 = []
list2 = []


def os_walk():
    for parent,dirnames,filenames in os.walk(path):
        for dirname in dirnames :
            dir = os.path.join(parent,dirname)
            list1.append(dir)
        for filename in filenames:
            abs = os.path.join(parent, filename)
            list2.append(abs)
    print list1, "\n", list2, "\n", len(list2)
if __name__ == "__main__":
    os_walk()
