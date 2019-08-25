#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-18 20:37   Authorcai      1.0      爬虫主程序
'''

# 导入工具
import time

import Sql_manager

# 使用selenium自动化测试工具
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect


class Crawer():
    def __init__(self):
        self.mysql = Sql_manager.MySql()
    def craw(self,link):
        """
        1.使用chrome的自动化测试工具
        """
        # link = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-08-30&flag=Y,N,Y'
        driver = selenium.webdriver.Chrome()
        driver.get(link)
        num = 1
        flag = "admit"
        while True:
            num += 1
            if flag == "admit" :
                flag = "deny"
                driver.execute_script(
                    '''
                    var date = document.querySelector("li.sel").nextElementSibling;
                    date.click();
                    '''
                )
                """
                2.使用selenium.webdriverwait实现对动态页面的等待
                """
                # 用webdriverwait 等待加载页面
                locator = (By.XPATH, "//div[@id='sear-result']")
                Wait(driver, 40).until(
                    Expect.presence_of_element_located(locator)
                )

                # 获取各车次列车数据
                trains = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'ticket_')]")
                try:
                    for train in trains:
                        # 利用字典储存座次类别
                        train_info = {'train_date': '', 'train_num': '', 'train_starttime': '', 'train_endtime': '','train_fromstation': '','train_tostation': '', 'train_spendtime': ''}
                        # 获取列车的信息
                        train_infoes = train.find_element_by_xpath(". //td[1]")
                        # 获取列车发车的日期
                        train_info['train_date'] = driver.find_element_by_xpath('//li[@class="sel"]//span[2]').text
                        # 获取列车的车次
                        train_info['train_num'] = train_infoes.find_element_by_xpath(
                            './/div[@class="train"]//a[@class="number"]').text
                        # 获取列车的起始车站
                        train_info['train_fromstation'] = train_infoes.find_element_by_xpath(
                            './/div[@class="cdz"]//strong[1]').text
                        train_info['train_tostation'] = train_infoes.find_element_by_xpath(
                            './/div[@class="cdz"]//strong[2]').text
                        # 获取列车的起始时间,车程耗费时间,是否当天到达
                        train_info['train_starttime'] = train_infoes.find_element_by_xpath(
                            './/div[@class="cds"]//strong[1]').text
                        train_info['train_endtime'] = train_infoes.find_element_by_xpath('.//div[@class="cds"]//strong[2]').text
                        train_info['train_spendtime'] = train_infoes.find_element_by_xpath('.//div[@class="ls"]//strong').text

                        # print(train_info)
                        self.mysql.collect(train_info)
                except:
                    print("爬取出错")
            flag = "admit"


if __name__ == "__main__":
    c = Crawer()
    for i in range(1,2):
        # link = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-'+str("{:0>2d}".format(i+5))+'&flag=Y,N,Y'
        # print(link)
        link = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-08-25&flag=Y,N,Y'
        c.craw(link)
