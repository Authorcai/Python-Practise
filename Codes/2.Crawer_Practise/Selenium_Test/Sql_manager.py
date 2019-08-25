#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Sql_manager.py
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-24 15:20   Authorcai      1.0     数据库处理
'''

# import lib
import pymysql

# # 连接数据库
# db = pymysql.connect(
#     "localhost",
#     "root",
#     "$Cai1998220$",
#     "python_spider"
# )
# cursor = db.cursor()
#
# # 数据库操作
# data = cursor.execute(
#     "select *"
# )
class MySql(object):
    def __init__(self):
        self.addr = "localhost"
        self.user = "root"
        self.pwd  = "Cai1998220"
        self.db_name = "python_spider"
        self.tb_name = "Train"

    def collect(self,dir={}):
        db = pymysql.connect(self.addr, self.user, self.pwd, self.db_name)

        cursor = db.cursor()

        # sql1 = 'insert into `Train`(train_num)values("'+str(dir["train_num"])+'");'
        sql = 'insert into `'+str(self.tb_name)+'`values("'+\
              str(dir["train_date"])+'","'+\
              str(dir["train_num"])+'","'+ \
              str(dir["train_starttime"])+'","'+ \
              str(dir["train_endtime"]) + '","' + \
              str(dir["train_fromstation"]) + '","' + \
              str(dir["train_tostation"]) + '","' + \
              str(dir["train_spendtime"]) + \
              '");'
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print("出现错误")