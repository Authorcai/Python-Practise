"""
第一个爬虫代码：获取页面
爬虫步骤:
    1.获取页面: requests headers link
    2.提取需要的数据:
    3.存储数据:存储至csv或数据库
Version: 0.1
Author: Authorcai
"""

# coding: UTF-8

import requests
from bs4 import BeautifulSoup
"""
    1.获取页面
"""
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0(Window;U;Windows NT6.1;en-US;rv:1.9.1.6) Gecko/20091201 Filefox/3.5.6'}

r = requests.get(link,headers = headers)
#print(r.text)

"""
    2.提取需要的数据
"""
#使用BeautifulSoup解析这段代码
soup = BeautifulSoup(r.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

"""
    3.存储数据
"""
#存储为txt格式文件
with open('title.txt',"a+") as f:
    f.write(title)
    f.close()