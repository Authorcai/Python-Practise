#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Time_with_Tem.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-09-13 13:52   Authorcai      1.0         爬虫练习
'''

# 导入第三方库
from matplotlib import pyplot as plt, font_manager as fm

from pylab import *
import random, numpy
import matplotlib


# 配置使图表支持中文显示
myfont = fm.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 绘制曲线
x = list(range(0,120))
y = [random.randint(20,35) for i in range(120)]

plt.plot(x,y)

# 设置坐标轴的刻度
x_new = ["10点{}分".format(i)  for i in range(0,60)]
x_new += ["11点{}分".format(i)  for i in range(0,60)]
plt.xticks(x,x_new,rotation = 45,fontproperities=myfont)

# 显示最终的折线图结果
plt.show()
