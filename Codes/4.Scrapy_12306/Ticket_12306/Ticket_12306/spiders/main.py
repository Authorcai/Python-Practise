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
from urllib import parse
import datetime
from items import Ticket12306Item


class main_Spider(scrapy.spiders.Spider):
    """
    设置spider要求的name, start_urls, parse()
    """
    # 1.name
    name = "ticket"
    # 2.start_urls
    '''base_url_1 = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-11-"
    base_url_2 = "&flag=N,N,Y"
    page = 4
    base_url_page = str("{:0>2d}".format(page))
    start_urls = [
        base_url_1+base_url_page+base_url_2
    ]'''

    # 定义方法用于获取start url
    def getStart(self):
        # 新建字典用于映射车站和网址代码之间的关系
        # 城市信息
        contents = {}
        # 编码 代码
        contents['武汉'] = [parse.quote('武汉'), 'WHN']
        contents['武昌'] = [parse.quote('武昌'), 'WCN']
        contents['汉口'] = [parse.quote('汉口'), 'HKN']
        contents['宜昌东'] = [parse.quote('宜昌东'), 'HAN']
        contents['襄阳'] = [parse.quote('襄阳'), 'XFN']

        # 车站
        fs = ['武汉', '武昌', '汉口', '宜昌东', '襄阳']
        ts = ['武汉', '武昌', '汉口', '宜昌东', '襄阳']
        # 日期
        dates = []
        time.strftime("%Y-%m-%d", time.localtime())
        nowtime = datetime.datetime.now()
        for i in range(5):
            futuretime = nowtime + datetime.timedelta(days=+i)
            futuretime = futuretime.strftime("%Y-%m-%d")
            dates.append(futuretime)
        # 生成url
        start_urls = []

        for fstation in fs:
            for tstation in ts:
                if fstation != tstation:
                    for date in dates:
                        url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=" + ','.join(contents[fstation]) + "&ts=" + ','.join(contents[tstation]) + "&date=" + date + "&flag=N,N,Y"
                        start_urls.append(url)

        return start_urls

    # 定义start_request()
    def start_requests(self):

        start_urls = self.getStart()
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def __init__(self):
        pass

    # 3.parse()
    def parse(self,response):
        # 获取url

        # 取得日期
        date = response.xpath('//li[@class="sel"]/span[2]/text()')
        trains = response.xpath('//tr[starts-with(@id,"ticket_")]')
        # 将item定义为列表
        item = Ticket12306Item()
        # 遍历每条车次的信息
        for train in trains:
            # 列车车次信息
            try:
                item['date'] = date.get()
                item['train_num'] =  train.xpath('. //td[1]//div[@class="train"]//a/text()').get()
                item['train_fromstation'] = train.xpath('. //td[1]//div[@class="cdz"]//strong[1]/text()').get()
                item['train_tostation'] = train.xpath('. //td[1]//div[@class="cdz"]//strong[2]/text()').get()
                item['train_starttime'] = train.xpath('. //td[1]//div[@class="cds"]//strong[1]/text()').get()
                item['train_endtime'] = train.xpath('. //td[1]//div[@class="cds"]//strong[2]/text()').get()
                item['train_spendtime'] = train.xpath('. //td[1]//div[@class="ls"]//strong[1]/text()').get()

                # 列车车票信息
                # item['train_seats_1'] = train.xpath('. //td[2]/text()')[].
                item['train_seats_1'] = train.xpath('. //td[3]/text()').get()
                item['train_seats_2'] = train.xpath('. //td[3]/text()').get()
                item['train_seats_3'] = train.xpath('. //td[4]/text()').get()
                item['train_seats_4'] = train.xpath('. //td[5]/text()').get()
                item['train_seats_5'] = train.xpath('. //td[6]/text()').get()
                item['train_seats_6'] = train.xpath('. //td[7]/text()').get()
                item['train_seats_7'] = train.xpath('. //td[8]/text()').get()
                item['train_seats_8'] = train.xpath('. //td[9]/text()').get()
                item['train_seats_9'] = train.xpath('. //td[10]/text()').get()
                item['train_seats_10'] = train.xpath('. //td[11]/text()').get()
                item['train_seats_11'] = train.xpath('. //td[12]/text()').get()
            except:
                 print('出错')

            print(item)
            # 返回item的迭代器
            yield item

