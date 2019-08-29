#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   QIdian_Spider.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-29 15:32   Authorcai      1.0    起点小说爬取
'''
import scrapy
from Qidian.Qidian.items import QidianItem, DocumentItem
class QidianSpider(scrapy.spiders):
    name = 'qdSpider'
    start_urls = []
    def parse(self,response):
        books = response.xpath()
        for book in books:
            id = book.xpath()
            name = book.xpath()
            link = book.xpath()
            new_para = book.xpath()
            author = book.xpath()
            words = book.xpath()
            date = book.xpath()
            status = book.xpath()

            item = QidianItem()
            item['id'] = id
            item['name'] = name
            item['link'] = link
            item['new_para'] = new_para
            item['author'] = author
            item['words'] = words
            item['date'] = date
            item['status'] = status

            yield item
            yield scrapy.Request(link,callback=self.parse_chapters)

        nextpage = response.xpath()
        if nextpage:
            yield scrapy.Request(nextpage)

    def parse_chapters(self,response):
        pass
