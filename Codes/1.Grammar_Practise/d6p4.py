"""
写一个程序判断一个数是不是回文素数
思路:
    分别调用判断回文和判断素数的函数即可
Version: 0.1
Author:Authorcai
"""
from d6p2 import isHuiwen
from d6p3 import isSushu
x = int(input('请输入一个数:'))
if isSushu(x) and isHuiwen():
    print("是回文素数")
else:
    print("不是回文素数")