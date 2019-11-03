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

    # 定义start_request()
    def start_requests(self):
        start_urls = [
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8c%97%E4%BA%AC,TJP&date=2019-11-04&flag=N,N,Y",
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8c%97%E4%BA%AC,TJP&date=2019-11-05&flag=N,N,Y",
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8c%97%E4%BA%AC,TJP&date=2019-11-06&flag=N,N,Y",
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%A4%A9%E6%B4%A5,TJP&date=2019-11-07&flag=N,N,Y",
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8c%97%E4%BA%AC,TJP&date=2019-11-08&flag=N,N,Y",
            "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8c%97%E4%BA%AC,TJP&date=2019-11-09&flag=N,N,Y"
        ]
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
            item['date'] = date.extract()
            item['train_num'] =  train.xpath('. //td[1]//div[@class="train"]//a/text()').extract()
            item['train_fromstation'] = train.xpath('. //td[1]//div[@class="cdz"]//strong[1]/text()').extract()
            item['train_tostation'] = train.xpath('. //td[1]//div[@class="cdz"]//strong[2]/text()').extract()
            item['train_starttime'] = train.xpath('. //td[1]//div[@class="cds"]//strong[1]/text()').extract()
            item['train_endtime'] = train.xpath('. //td[1]//div[@class="cds"]//strong[2]/text()').extract()
            item['train_spendtime'] = train.xpath('. //td[1]//div[@class="ls"]//strong[1]/text()').extract()

            # 列车车票信息
            item['train_seats_1'] = train.xpath('. //td[2]/text()').extract()
            item['train_seats_2'] = train.xpath('. //td[3]/text()').extract()
            item['train_seats_3'] = train.xpath('. //td[4]/text()').extract()
            item['train_seats_4'] = train.xpath('. //td[5]/text()').extract()
            item['train_seats_5'] = train.xpath('. //td[6]/text()').extract()
            item['train_seats_6'] = train.xpath('. //td[7]/text()').extract()
            item['train_seats_7'] = train.xpath('. //td[8]/text()').extract()
            item['train_seats_8'] = train.xpath('. //td[9]/text()').extract()
            item['train_seats_9'] = train.xpath('. //td[10]/text()').extract()
            item['train_seats_10'] = train.xpath('. //td[11]/text()').extract()
            item['train_seats_11'] = train.xpath('. //td[12]/text()').extract()

            print(item)
            # 返回item的迭代器
            yield item

