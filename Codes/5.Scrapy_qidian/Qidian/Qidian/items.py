# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 用于记录小说的基本信息
class QidianItem(scrapy.Item):
    # 小说编号
    id = scrapy.Field()
    # 小说姓名
    name = scrapy.Field()
    # 小说链接
    link = scrapy.Field()
    # 小说最新章节
    new_para = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说连载字数
    words = scrapy.Field()
    # 小说更新时间
    date = scrapy.Field()
    # 小说状态
    status = scrapy.Field()

# 用于记录某一小说的章节信息
class DocumentItem(scrapy.Item):
    # 章节编号
    id = scrapy.Field()
    # 章节名
    name = scrapy.Field()
    # 章节链接
    link = scrapy.Field()
    # 章节内容
    content = scrapy.Field()