"""
练习：打印各种三角形图案

Version: 0.1
Author: Authorcai
"""

#参照terminal的打印格式，只能是按行输出，故循环嵌套y在外，x在内，y从5～0，x从0～5
"""
"                           *
"                           **
"                           ***
"                           ****
"                           *****
"""
print('图案一',end='')
y = 5;
while y <= 5 and y > 0:
    print('\n')
    x = 0
    while x <= 5:
        if y <= -1*x + 5:
            print('*',end='')
        x += 1
    y -= 1
#图案二
"""
                            ******
                            *****
                            ****
                            ***
                            **
                            *
"""
print('\n图案二',end='')
y = 5
while y <= 5 and y >= 0:
    print('\n')
    x = 0
    while x <= 5:
        if y >= -1*x + 5:
            print('*',end='')
        x += 1
    y -= 1
#图案三
print('\n图案三',end='')
y = 5
while y <= 5 and y >= 0:
    print('\n')
    x = 0
    while x <= 10:
        if y<=x and (y <= -1*x + 10):       #搞不懂
            print('*',end='')
        x += 1
    y -= 1