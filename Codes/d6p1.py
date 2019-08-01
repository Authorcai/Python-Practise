"""
实现计算最大公约数和最小公倍数的函数
思路：
    1.最大公约数：取较小的一个数依次剪1，直到同时被原来的两个数取余结果为0
    2.最小公倍数：两个数的乘积除去最大公约数结果即为最小公倍数
"""
#最大公约数
def MaxDivisor(x,y):
    if x > y:
        divisor = y
    else:
        divisor = x
    while divisor >= 1:
        if x%divisor==0 and y%divisor==0:
            return divisor
        divisor-=1
    return 1
#最小公倍数
def MinMutiple(x,y):
    return x*y // MaxDivisor(x,y)
#程序验证
x = int(input('请输入数1:'))
y = int(input('请输入数2:'))
print('最大公约数:%d, 最小公倍数:%d' %(MaxDivisor(x,y),MinMutiple(x,y)))