"""
对urllib2网页下载器的三种方法的实验
1.简单方法下载
2.通过requests下载
3.通过添加特殊情景的处理器下载
"""
import urllib.request
import requests

url = 'http://www.baidu.com'

# 第一种方法
# url
# .urlopen(url)
# .getcode()
# .read()
print('第一种方法')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

# 第二种方法
# url
# request
# .add_header('','')
# .urlopen(request)
# .getcode()
# .read()
print('第二种方法')
request = urllib.request.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
