## PYthon爬取动态网页:爬取评论内容

>### AJAX 技术

#### AJAX加载网页
* AJAX 通过网页脚本动态的发送请求,获取数据
* AJAX 使得网页在更新数据的时候,没有改变url,即没有对整个页面进行更新
************

>### 对动态页面的爬虫

#### 解析真实地址抓取
* 抓包 : 利用浏览器的检查功能,通过找到数据的真实地址,获取数据
* 通过在网址 <https://http://www.santostang.com/2018/07/04/hello-world/> 中通过检查,在NetWork>Preview中找到link? ,通过查看Headers确定url和Headers具体的数值
* 举例:
```python
    link = 'https://api-zero.livere.com/v1/comments/list?' \
           'callback=jQuery112408968122676277035_1564727576286&' \
           'limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%' \
           '2Flist&consumerSeq=1020&' \
           'livereSeq=28583&smartloginSeq=5154&_=1564727576288'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
```

#### 获取数据
* 通过url 和 headers 发送请求,得到响应的内容,格式为字符串
```python
import requests 

r = requests.get(link,headers = headers)
#print(r.text)
```
* 指定读取的字符串响应体的范围,转换成json数据格式
```python
    json_string = r.text
    #涵盖了{}中的全部内容
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.load(json_string)
    comment_list = json_data['results']['comments']
```
* 通过json数据读取指定的title('content')并输出
```python
for eachone in comment_list:
    message = eachone['content']
    print(message)    
```