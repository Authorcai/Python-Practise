#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tesst_2.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-22 15:23   Authorcai      1.0         爬虫练习
'''
import random

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect

# 使用chrome的自动化测试工具
link = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-08-30&flag=Y,N,Y'
driver = selenium.webdriver.Chrome()
driver.get(link)

#通过selenium.webdriver调用脚本,实现对始发站和终点站的输入以及对搜索按钮的点击
driver.execute_script(
    '''
    var fromStation = document.getElementById('fromStation');
    var toStation = document.getElementById('toStation');
    var btn = document.getElementById('query_ticket');
    var date = 
    fromStation.value='SHH'
    toStation.value='TJP'
    btn.click()
    '''
)

#以元组的形式储存页面解析方式和xpath格式
locator = (By.XPATH, "//div[@id='sear-result']")
#使用selenium.webdriverwait实现对动态页面的等待
Wait(driver,40).until(
    Expect.presence_of_element_located(locator)
)

#对通过selenium对页面信息进行处理
#利用字典储存座次类别
seats={
    1:'商务座',
    2:'一等座',
    3:'二等座',
    4:'高级软卧',
    5:'软卧一等',
    6:'动卧',
    7:'硬卧',
    8:'软座',
    9:'硬座',
    10:'无座',
    11:'其他'
}
seats_info={
    '商务座':'',
    '一等座':'',
    '二等座':'',
    '高级软卧':'',
    '软卧一等':'',
    '动卧':'',
    '硬卧':'',
    '软座':'',
    '硬座':'',
    '无座':'',
    '其他':''
}

#获取本车次的相关信息



#获取各车次列车数据
trains = driver.find_elements(By.XPATH,"//tr[starts-with(@id,'ticket_')]")

print()
for train in trains:
    # 获取列车的信息
    train_infoes = train.find_element_by_xpath(". //td[1]")
    # 获取列车的车次
    train_number = train_infoes.find_element_by_xpath('.//div[@class="train"]//a[@class="number"]').text
    # 获取列车的起始车站
    from_station = train_infoes.find_element_by_xpath('.//div[@class="cdz"]//strong[1]').text
    to_station = train_infoes.find_element_by_xpath('.//div[@class="cdz"]//strong[2]').text
    # 获取列车的起始时间,车程耗费时间,是否当天到达
    start_time = train_infoes.find_element_by_xpath('.//div[@class="cds"]//strong[1]').text
    end_time = train_infoes.find_element_by_xpath('.//div[@class="cds"]//strong[2]').text
    time = train_infoes.find_element_by_xpath('.//div[@class="ls"]//strong').text
    arrive_time = train_infoes.find_element_by_xpath('.//div[@class="ls"]//span').text


    # print("%-7s%-7s%-7s%-7s%-7s%-7s%-7s" %(repr(train_number).rjust(7),repr(from_station).rjust(7),repr(to_station).rjust(7),repr(start_time).rjust(7), repr(end_time).rjust(7), repr(time).rjust(7), repr(arrive_time).rjust(7) ))
    print('{0:-7s}' .format(start_time))

