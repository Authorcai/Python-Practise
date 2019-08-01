"""
设计一个函数返回传入的列表中最大和第二大的元素的值
思路:
    利用max记录列表中的最大值,依次比较得到max的确定值
    利用max2记录列表中第二大的值,在发现在新的最大值时,将旧的max值赋给max2

Version: 0.1
Author: Authorcai
"""
def max2(lst):
    length = len(lst)
    max = lst[0]
    for x in range(1,length):
        if max < lst[x] :
            max2 = max
            max = lst[x]
    return [max,max2]

print(str(max2([23,11,43,66,54,99,21])[0])+" "+str(max2([23,11,43,66,54,99,21])[1]))