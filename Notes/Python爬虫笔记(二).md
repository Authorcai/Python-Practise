## Python 爬取豆瓣视频top250电影

>### Requests 设置
 
#### URL 设置

* 设置 `link`(网址)
* 设置 `params` (字典格式)
* 利用 `requests` (设置key值)

代码举例如下:
```python
import requests
link = 'https://movie.douban.com/'
key_dict = {'key1':'values','key2':'values2'}
r = requests.get(link,paramas = key_dict)
```
***********************

#### headers设置
* 通过headers设置 'user-agent' 'Host'
```python
headers = {'user-agent':'','Host':''}
```

#### 获取页面
* 通过requests 获取页面的数据(html代码)
```python
r = requests.get(link,headers = headers)
# 或者使用post请求
print(r.text)
```

#### 处理页面
* soup = Beautifulsoup(r.text, 'lxml' )
* data_list = []
* data = soup.find(,class_ = '指定的属性' ).a.strip()
* data_list.apend(data)

#### 输出结果
    
