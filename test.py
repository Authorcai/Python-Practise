# 使用网络爬虫

import requests
from bs4 import BeautifulSoup

# 1.设定link 和 headers,获取页面
link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0(Window;U;Windows NT6.1;en-US;rv:1.9.1.6) Gecko/20091201 Filefox/3.5.6'}
r = requests.get(link, headers=headers)
# print(r.text)

# 2.设定搜索信息,用find(),获取数据

soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()

print(title)

# 3.存储数据

with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
