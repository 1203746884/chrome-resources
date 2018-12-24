# coding=utf-8
import pymysql
import os
import ConfigParser
config_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(config_dir, "config.ini")
config = ConfigParser.SafeConfigParser()
config.read(config_path)
ip = config.get('config','ip')
user = config.get('config','user')
password =config.get('config','password')
db_name = config.get('config','db_name')
port = int(config.get('config','port'))
print
class PyMysql(object):

    def __init__(self,ip,user,password,db_name,port):
        self.connect=pymysql.connect(ip,user,password,db_name,port,charset='utf8')
        self.cursor= self.connect.cursor()
        if not self.cursor:
            raise (NameError,"connected failed")
        else:
            print  "connected success"
    """
        params:  many默认为None，只给sql时,默认只差寻第一行数据，当需要多行执行前n行时传入int
                 根据传入int值查询结果的前n行的数据，如果想要查询所有则传入all,不需要加引号;
    """
    def exe_query(self,sql,many=None):
        self.cursor.execute(sql)
        if many:
            if type(many) is int:
                result_line=self.cursor.fetchmany(many)
                if many <= len(self.cursor.fetchall()):
                    if result_line:
                            print "获取查询成功,查询前{}行结果为：{}".format(many,result_line)
                            return result_line
                    else:
                        raise(NameError,"查询失败，目标信息不存在或 Invalid SyntaxError")
                else:
                    print "many越界超出实际的结果行数，实际最大行数为{}".format(len(result_line))
            elif many == all:
                result_line=self.cursor.fetchall()
                if result_line:
                    print "即将获取所有查询结果....wait please!"
                    print "获取所有查询结果为:{}".format(result_line)
                else:
                    print "很遗憾，查询结果不存在，查询对象不存在或sql语法错误"
        else:
            result_line = self.cursor.fetchone()
            if result_line:
                print "查询成功,第一行row数据为: {}".format(result_line)
            else:
                raise (NameError, "查询结果不存在或Invalid SyntaxError")

    def exe_inert(self,sql,param):
        if len(param) == 1 :
            try:
                self.cursor.execute(sql,param)
                self.connect.commit()
            except Exception  as e:
                self.connect.rollback()
                print e
            else:
                promote = "插入单行数据成功"
                print promote

        elif len(param) >= 2 :
            try :
                self.cursor.executemany(sql,param)
                self.connect.commit()
            except Exception as e:
                self.connect.rollback()
            else:
                promote = "插入多行数据成功"
                print promote
    def  disconnect(self):
             self.connect.close()

if __name__ == "__main__":
    connection= PyMysql(ip,user,password,db_name,port)
    connection.exe_query("select * from sys_user",all)
    connection.disconnect()
