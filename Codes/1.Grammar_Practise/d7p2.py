"""
设计一个函数产生指定长度的验证码,验证码由大小写字母和数字构成
思路:
    设置一个初始字符串,包括数字和大小写字母,设定长度,用for-in循环随机得到索引位置并取得字符串元素连接至空串山
Version: 0.1
Author: Authorcai
"""
import random

def yanZhenma(code_len=10):
    code = ""
    str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790"
    length = len(str)

    for n in range(code_len) :
        m = random.randint(0,length)
        para = str[m]
        code = code + para
    return code

num = int(input('请输入想要获取的验证码的长度'))
print(yanZhenma(num))
