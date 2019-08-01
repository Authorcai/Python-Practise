"""
练习 : 使用Python爬虫访问静态页面

"""
import requests
from bs4 import BeautifulSoup

# 定制URL参数
key_dic = {'key1': 'value1', 'key2': 'value2'}
link = 'http://httpbin.org/get'

r = requests.get(link, params=key_dic)
print('URL已经正确编码:', r.url)
print('字符串方式的响应体: \n', r.text)
