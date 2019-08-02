"""
实现判断一个数是不是素数的函数

Version 0.1
Author: Authorcai
"""
def isSushu(x):
    num = x-1
    while num > 1:
        if x%num == 0:
            return False
        num -= 1
    return True
#设计程序检验函数功能
x = int(input('请输入一个数'))
if isSushu(x):
    print("这是个素数")