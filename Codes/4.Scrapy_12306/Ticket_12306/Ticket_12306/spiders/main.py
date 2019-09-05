#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-26 12:11   Authorcai      1.0      爬虫练习
'''

# import lib
import time
import scrapy
import selenium.webdriver
from Ticket_12306.items import Ticket12306Item
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect

class main_Spider(scrapy.spiders.Spider):
    """
    设置spider要求的name, start_urls, parse()
    """
    # 1.name
    name = "ticket"
    # 2.start_urls
    base_url_1 = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-"
    base_url_2 = "&flag=N,N,Y"
    page = 4
    base_url_page = str("{:0>2d}".format(page))
    start_urls = [
        base_url_1+base_url_page+base_url_2
    ]
    # start_urls = [
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-04&flag=N,N,Y",
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-05&flag=N,N,Y",
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-06&flag=N,N,Y",
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-07&flag=N,N,Y",
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-08&flag=N,N,Y",
    #     "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-09-09&flag=N,N,Y"
    # ]
    # 使用selenium进行初始化
    def __init__(self):
        self.browser = selenium.webdriver.Chrome()

    # 3.parse()
    def parse(self,response):
        # 获取url
        self.browser.get(response.url)
        x = response.url
        Wait(self.browser, 100).until(
            Expect.presence_of_element_located((By.XPATH, '//tr[starts-with(@id,"ticket_")][34    ]'))
        )
        # 取得日期
        date = self.browser.find_element_by_xpath('//li[@class="sel"]/span[2]')
        trains = self.browser.find_elements_by_xpath('//tr[starts-with(@id,"ticket_")]')
        # 将item定义为列表
        item = Ticket12306Item()
        # 遍历每条车次的信息
        for train in trains:
            # 列车车次信息
            item['date'] = date.text
            item['train_num'] =  train.find_element_by_xpath('. //td[1]//div[@class="train"]//a').text
            item['train_fromstation'] = train.find_element_by_xpath('. //td[1]//div[@class="cdz"]//strong[1]').text
            item['train_tostation'] = train.find_element_by_xpath('. //td[1]//div[@class="cdz"]//strong[2]').text
            item['train_starttime'] = train.find_element_by_xpath('. //td[1]//div[@class="cds"]//strong[1]').text
            item['train_endtime'] = train.find_element_by_xpath('. //td[1]//div[@class="cds"]//strong[2]').text
            item['train_spendtime'] = train.find_element_by_xpath('. //td[1]//div[@class="ls"]//strong[1]').text

            # 列车车票信息
            item['train_seats_1'] = train.find_element_by_xpath('. //td[2]').text
            item['train_seats_2'] = train.find_element_by_xpath('. //td[3]').text
            item['train_seats_3'] = train.find_element_by_xpath('. //td[4]').text
            item['train_seats_4'] = train.find_element_by_xpath('. //td[5]').text
            item['train_seats_5'] = train.find_element_by_xpath('. //td[6]').text
            item['train_seats_6'] = train.find_element_by_xpath('. //td[7]').text
            item['train_seats_7'] = train.find_element_by_xpath('. //td[8]').text
            item['train_seats_8'] = train.find_element_by_xpath('. //td[9]').text
            item['train_seats_9'] = train.find_element_by_xpath('. //td[10]').text
            item['train_seats_10'] = train.find_element_by_xpath('. //td[11]').text
            item['train_seats_11'] = train.find_element_by_xpath('. //td[12]').text

            # 返回item的迭代器
            yield item

