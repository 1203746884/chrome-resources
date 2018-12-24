# coding=utf-8

import MySQLdb


class DB(object):

    def __init__(self, ip, user, password, db_name):
        """连接数据库"""
        self.connection = MySQLdb.connect(ip, user, password, db_name)
        """获取游标"""
        self.cursor = self.connection.cursor()

    def insert(self,sql):
        try:
            # sql = "insert into tb_name(user_account,login_pwd, user_name)values(%s,%s,%s)"
            """parameters类似数据库的二维数组多条数据插入用executemany,单行用excute"""
            params = [(1001,"dev",'123456','wwxdd','0','1',1,'2018-11-25-11-12-43'),(1002,"test","123456","cwxdd",'0','1',0,'2018-11-25-11-12-44')]
            self.cursor.executemany(sql, params)
            self.connection.commit()
        except SyntaxError as e:
            self.connection.rollback()
            print "语法错误"

    def fetch_data(self, sql):
        try:
            # select * from tb_name  where id =101
            self.cursor.execute(sql) # 执行语句
            self.connection.commit() # 提交数据
        except SyntaxError:
            print "语法错误"
        else:
            # 获取单行数据
            data = self.cursor.fetchone()
            print data
            # 获取多行数据
            datas = self.cursor.fetchall()
            print datas

    def close_db(self):
        self.connection.close()

if __name__ == '__main__':
    db = DB(ip='192.168.229.128 ',user='root',password='123456',db_name='betadb')
    #db.fetch_data(sql="select * from sys_user")
    #db.insert(sql = "insert into sys_user(id,user_account,login_pwd, user_name,user_status,record_status,update_count,create_date)values(%s,%s,%s,%s,%s,%s,%s,%s)")
    db.close_db()






