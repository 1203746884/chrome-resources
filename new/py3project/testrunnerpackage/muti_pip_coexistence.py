# coding=utf-8
# URL:https://www.python.org/downloads/

__author__ = "Chen"
__version__ = "python2.x and python3.x"

"""
假设现在需要多版本python共存，python2.x用来空间数据主要配合ArcGIS和python3.x做算法处理
so,先进入python35修改python.exe 为 python3.exe,修改pythonw.exe为pythonw3.exe
python27里面保持不动
调用python3离线操作，进行python3 -m  setup.py  install  离线安装包
此时针对python35进行pip进行升级操作指令：python3 -m pip install --upgrade pip --force-reinstall
然后调用 指令：pip --version 和 pip3 --version  验证pip修改效果 pip 调用时就可以以pip
代表python27的pip ,pip3 代表 python35 的pip 进行在线安装升级指令；安装卸载指令怎么调用呢for example:
pip3 uninstall requests 卸载requests库文件，pip3 install  cx_Oracle 安装数据库驱动在线命令
至此问题完美解决，解决问题的方法很多，最适合的就是最好的；
"""
