# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 14:29
@Auth:Dali
@QQ:1334029448
"""
import pymysql
from utils.read_yaml import Read_Yaml
class Test_Sql():
    def __init__(self):
        read_y=Read_Yaml('data','login_mysql_data.yaml')
        dic=read_y.read_dict()
        self.conet=pymysql.Connect(host=dic['host'],user=dic['user'],password=dic['password'],db=dic['db'],port=dic['port'])
        self.cursor=self.conet.cursor()

    def select_userid(self):
        self.cursor.execute('select max(id) from sys_user')
        return self.cursor.fetchall()[0][0]
    def insert(self,sql):
        self.cursor.execute(sql)
        self.conet.commit()
    def update(self,sql):
        self.cursor.execute(sql)
        self.conet.commit()

if __name__ == '__main__':
    test_sql=Test_Sql()
    print(test_sql.select_userid())