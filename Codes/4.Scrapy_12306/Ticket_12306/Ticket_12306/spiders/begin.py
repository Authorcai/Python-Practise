#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   begin.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-26 16:00   Authorcai      1.0         爬虫练习
'''

# import lib
 
from scrapy import cmdline

cmdline.execute("scrapy crawl ticket".split())