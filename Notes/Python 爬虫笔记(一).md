## Python 网络爬虫笔记

>### 网络爬虫的过程

#### 爬取静态页面

* 获取页面
    1. 设置`link`,指定访问的网址
    2. 设置headers,指定访问的浏览器的信息
    3. import requestsmokuai,调用requests.get()函数
    详见以下例子:
```python
# coding: UTF-8

import requests
from bs4 import BeautifulSoup
"""
1.获取页面
"""
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0(Window;U;Windows NT6.1;en-US;rv:1.9.1.6) Gecko/20091201 Filefox/3.5.6'}

r = requests.get(link,headers = headers)
# print(r.text)
```

* 读取页面
    1. 利用Beautifulsoup()获取soup对象
    2. 再使用find()函数获取指定的数据
    详见以下例子:
```python
"""
2.提取需要的数据
"""
#使用BeautifulSoup解析这段代码
soup = BeautifulSoup(r.text,"lxml")
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)
```

* 存储数据
    1. 通过python对文件的写入和更新实现数据的存储
    详见以下例子:
```python
"""
3.存储数据
"""
#存储为txt格式文件
with open('title.txt',"a+") as f:
    f.write(title)
    f.close()
```