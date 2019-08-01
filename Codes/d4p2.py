"""
输入两个数，计算二者的最大公约数和最小公倍数

Verison: 0.1
Author: Authorcai
"""
x =  int(input("输入正整数x："))
y =  int(input("输入正整数y："))
con = 1         #最大公约数
com = 1         #最小公倍数

if x < y:
    con = x
    com = y
else:
    con = y
    com = x
#循环求得最大公约数和最小公倍数
while con >= 1:
    if x%con ==0 and y%con ==0:
        print('最大公约数为：%d' %con)
        break;
    con -= 1
while com <= x*y:
    if com%y==0 and com%x==0:
        print('最小公倍数为：%d' %com)
        break;
    com += 1