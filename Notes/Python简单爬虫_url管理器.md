## Python简单爬虫

> ### Python简单爬虫结构

#### 使用 URL管理器 的三种下载页面的方法
```python
import urllib.request
import http.cookiejar
# 1.简单下载网页
url = 'http://wwww.baidu.com'

response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(response1.read())

# 2.request

request = urllib.request.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib.request.urlopen(request)

print(response2.getcode())
print(response2.read())

# 3.cj

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

response3 = urllib.request.urlopen(url)

print(response3.getcode())
print(len(response3.read()))
print(cj)  
```