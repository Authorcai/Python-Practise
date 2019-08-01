"""
练习:打印杨辉三角
思路: 利用列表的嵌套实现
    1.杨辉三角形如:                  1
                                  1 1
                                 1 2 1
                                1 3 3 1
                               1 4 6 4 1
                            .................
    2.将每行视为一个列表长度递增
    3.利用递归的方式,设计函数求得每一个元素的值

Version: 0.1
Author:Authorcai
"""
def Yhsan(row_len=5):
    lst = [[0 for i in range(row_len)] for j in range(row_len)]
    for i in range(row_len):
        for j in range(i):
            if j==0  or j==row_len-1:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        for j in range(i):
            print(lst[i][j],end="")
        print()
Yhsan(int(input('亲输入行数: ')))