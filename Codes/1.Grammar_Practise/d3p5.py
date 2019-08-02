"""
计算百钱百鸡问题

Version: 0.1
Author: Authorcai
"""
a = b =c =0

while a < 20:
    while b < 34:
        while c < 300:
            if (a+b+c == 100) and (5*a + 3*b + c/100 == 100):
                print("公鸡数量：%d,母鸡数量：%d，小鸡数量：%d" %(a,b,c))
            c+=1
        b+=1
    a+=1
print("公鸡数量：%d,母鸡数量：%d，小鸡数量：%d" %(a,b,c))