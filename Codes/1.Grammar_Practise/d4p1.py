"""
输入一个数，判断其是不是素数

Version: 0.1
Author: Authorcai
"""

for x in range(0,100):
    a = 2
    flag = 0
    while a < x:
        if x%a == 0:
            flag = 1
        a += 1
    if flag == 0:
        print("%d 为素数" % x)