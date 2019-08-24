#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_3.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-24 13:20   Authorcai      1.0     爬虫连接mysql
'''

# import lib
import pymysql

# 连接数据库
db = pymysql.connect(
    'localhost',
    'root',
    '$Cai1998220$',
    'python_spider'
)
cursor = db.cursor()

# 数据库获取数据
cursor.execute(
    "select *\
    from Person "
)

# 对数据进行处理
data = cursor.fetchone()
print(str(data))

# 关闭数据库
db.close()