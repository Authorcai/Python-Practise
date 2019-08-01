"""
实现判断一个数是不是回文数的函数

Version: 0.1
Author: Authocai
"""
#判断函数
def isHuiwen(x):
    temp = x
    sum = 0
    while x:
        sum = (sum*10 + x%10)
        x = x//10
    if sum == temp:
        return True
    else:
        return False
#程序调用函数实现判断回文数功能
x = int(input('请输入一个数:'))
if isHuiwen(x):
    print('这是个回文数')