"""
计算指定的年月日时这一年的第几天
思路:
    1.设置一个列表date[31,28,31,30,31,30,31,31,30,31,30,31]
    2.判断当前是否为闰年,若是则设置date[1] = 29
    3.用for-in循环加上if语句判断,计算当前年月日时这一年的第几天
Version: 0.1
Author: Authhorcai
"""
def preDate(lst):
    date = [31,28,31,30,31,30,31,31,30,31,30,31]
    #年份所在的 位置
    posY = lst.find('-')
    #月份所在的位置
    posM = lst.rfind('-')
    #得到年份 月份 日数
    Year = int(lst[0:posY])
    Month = int(lst[posY+1:posM])
    Day = int(lst[posM+1:len(lst)])

    if (Year%4==0 and Year%100!=0) or (Year%400 == 0):
        date[1] = 29
    Sum = 0
    for m in range(0,Month-1):
        Sum += date[m]
    return Sum+Day

print(preDate('2000-3-22'))