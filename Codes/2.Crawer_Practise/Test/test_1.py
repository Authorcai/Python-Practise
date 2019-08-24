#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_1.py
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    --------------------------------------------------
2019-08-19 20:57   Authorcai      1.0     利用request BeautifulSoup实现豆瓣top250电影标题内容抓取和输出
'''

import urllib.request
from bs4 import BeautifulSoup
import json

link = "https://movie.douban.com/top250"
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Host':'movie.douban.com'
}




# print(re.getheaders())
# print(re.getcode())
# print(re.read())




num = 0
while num <= 9:
    link_new = link+'?start='+str(num*25)+'&filter='
    re = urllib.request.urlopen(link_new)
    re.headers = header
    soup = BeautifulSoup(
        re.read(),
        'html.parser',
        from_encoding='utf8'
    )
    nodes = soup.find_all('div', class_='hd')
    i = num*25+1
    for node in nodes:
        print("no." + str(i) + ' ', end='')
        print(node.a.span.get_text())
        i += 1
    num += 1