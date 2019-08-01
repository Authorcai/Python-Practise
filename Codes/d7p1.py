"""
练习:在屏幕上显示文字跑马灯

思路:
    用while循环,通过屏幕的休眠和字符的截取实现跑马灯效果
Version: 0.1
Author: Authocai
"""

import os
import time

def paoMaden(name):
    while True:
        os.system('clear')
        print(name)
        time.sleep(0.2)
        name = name[1:] + name[0]

paoMaden("北京欢迎您,为您开天辟地")