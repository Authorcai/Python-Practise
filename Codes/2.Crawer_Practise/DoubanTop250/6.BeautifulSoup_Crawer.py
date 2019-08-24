from bs4 import BeautifulSoup

"""
这是对网页解析器的练习,使用BeautifulSoup实现结构化解析
1.创建BeautifulSoup对象
2.搜索节点
3.访问节点信息

Version: 0.1
Author: Authorcai
"""
html_doc = ''
soup = BeautifulSoup(
    html_doc,
    'html.parser'
)

list1 = soup.find_all('div')
list2 = soup.find_all('a',class_='')
list3 = soup.find_all('a',href = '',string = '')

for each in list1:
    print(each.get_text())