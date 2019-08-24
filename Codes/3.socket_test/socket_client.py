#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   socket_client.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-11 16:18   Authorcai      1.0     Socket练习
'''

# socket 客户端
import socket

client = socket.socket()
client.connect(('211.67.55.230',8000))
name = "hakhdkaj"
client.send(name.decode('utf8'))
while True:
    input_data = input()
    client.send(input_data.decode('utf8'))
#client.close()