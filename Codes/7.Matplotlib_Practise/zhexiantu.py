#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   zhexiantu.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-09-17 12:35   Authorcai      1.0      画图练习
'''

import matplotlib as mlt
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import randn

x = np.arange(0,10,0.1)
y = np.sin(x)
plt.plot(x,y,label="linear")

plt.title(r'Sin function')
plt.ylabel("y axis")
plt.xlabel("x axis")