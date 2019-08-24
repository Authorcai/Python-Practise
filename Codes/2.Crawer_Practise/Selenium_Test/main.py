#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-18 20:37   Authorcai      1.0         爬虫练习
'''

# import lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 配置浏览器
driver = webdriver.Chrome()
driver.get("http://www.google.com")


