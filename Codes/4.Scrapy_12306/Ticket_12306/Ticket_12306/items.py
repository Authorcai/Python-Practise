# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ticket12306Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    车次信息:
    1日期
    2车次
    3起始站
    4终点站
    5发站时间
    6到站时间
    7乘车时长
    """
    date = scrapy.Field()
    train_num = scrapy.Field()
    train_fromstation = scrapy.Field()
    train_tostation = scrapy.Field()
    train_starttime = scrapy.Field()
    train_endtime = scrapy.Field()
    train_spendtime = scrapy.Field()

    """
    车票信息:
    1商务座
    2一等座
    3二等座
    4高级卧铺
    5一等软座
    6动卧
    7硬卧
    8软座
    9硬座
    10无座
    11其他
    """

    train_seats_1 = scrapy.Field()
    train_seats_2 = scrapy.Field()
    train_seats_3 = scrapy.Field()
    train_seats_4 = scrapy.Field()
    train_seats_5 = scrapy.Field()
    train_seats_6 = scrapy.Field()
    train_seats_7 = scrapy.Field()
    train_seats_8 = scrapy.Field()
    train_seats_9 = scrapy.Field()
    train_seats_10 = scrapy.Field()
    train_seats_11 = scrapy.Field()

    # train_seats = {
    #     "商务座":"",
    #     "一等座":"",
    #     "二等座":"",
    #     "高级软卧":"",
    #     "一等软卧":"",
    #     "动卧":"",
    #     "硬卧":"",
    #     "软座":"",
    #     "硬座":"",
    #     "无座":"",
    #     "其他":""
    # }
