"""
对动态页面的网络爬虫，利用浏览器的 "检查" 功能
Version : 0.1
Author : Authorcai
"""
import requests
import json


def getWeb():
    link = 'https://api-zero.livere.com/v1/comments/list?' \
           'callback=jQuery112408968122676277035_1564727576286&' \
           'limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%' \
           '2Flist&consumerSeq=1020&' \
           'livereSeq=28583&smartloginSeq=5154&_=1564727576288'
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    r = requests.get(link,headers = headers)
    #print(r.text)

    json_string = r.text
    #涵盖了{}中的全部内容
    json_string = json_string[json_string.find('{'):-2]
    #将字符串响应体转换为json数据
    json_data = json.loads(json_string)
    #对json数据进行处理,获取评论信息
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        message = eachone['content']
        print(message)

getWeb()