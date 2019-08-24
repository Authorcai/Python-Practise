#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   socket_server.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-11 16:17   Authorcai      1.0       Socket编程
'''

# import lib
import socket

server = socket.socket()

server.bind(("0.0.0.0",8000))
server.listen()

sock,addr = server.accept()
data = ""

while True:
    tmp_data = sock.recv(1024)
    if tmp_data:
        data += tmp_data.decode("utf8")
        if tmp_data.decode('utf8').endswith('#'):
            break
    else:
        break

print(data)
sock.close()