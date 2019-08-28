# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class Ticket12306Pipeline(object):
    # 连接数据库
    def __init__(self):
        """
        连接数据库,其中数据库信息为
        ip:连接的数据库的位置
        user:用户名
        passwd:用户密码
        db_name:数据库名
        table_name:数据表名
        """
        self.ip = "localhost"
        self.user = "root"
        self.passwd = "Cai1998220"
        self.db_name = "python_spider"
        self.table_name = "Full_Train"
        self.db = pymysql.Connect(self.ip,self.user,self.passwd,self.db_name)
        self.cursor = self.db.cursor()

    # 存储数据
    def process_item(self, item, spider):
        sql = "insert into `"+self.table_name+"` values( "+'"'+\
        item['date']+'"'+","+'"'+\
        item['train_num']+'"'+","+'"'+\
        item['train_fromstation']+'"'+","+'"'+\
        item['train_tostation']+'"'+","+'"'+\
        item['train_starttime']+'"'+","+'"'+\
        item['train_endtime']+'"'+","+'"'+\
        item['train_spendtime']+'"'+","+'"'+\
        item['train_seats_1']+'"'+","+'"'+\
        item['train_seats_2']+'"'+","+'"'+\
        item['train_seats_3']+'"'+","+'"'+\
        item['train_seats_4']+'"'+","+'"'+\
        item['train_seats_5']+'"'+","+'"'+\
        item['train_seats_6']+'"'+","+'"'+\
        item['train_seats_7']+'"'+","+'"'+\
        item['train_seats_8']+'"'+","+'"'+\
        item['train_seats_9']+'"'+","+'"'+\
        item['train_seats_10']+'"'+","+'"'+\
        item['train_seats_11']+'"'+")"
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print("出现错误")

        return item

    # 关闭数据库连接
    def process_close(self):
        self.db.close()