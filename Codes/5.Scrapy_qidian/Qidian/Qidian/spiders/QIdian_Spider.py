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
from items import QidianItem
from items import DocumentItem


class QIdianSpider(scrapy.spiders.Spider):
    name = 'Qidian'
    start_urls = [
        'http://www.23us.com/class/1_1.html',
        'http://www.23wx.com/class/2_1.html',
        'http://www.23wx.com/class/3_1.html',
        'http://www.23wx.com/class/4_1.html',
        'http://www.23wx.com/class/5_1.html',
        'http://www.23wx.com/class/6_1.html',
        'http://www.23wx.com/class/7_1.html',
        'http://www.23wx.com/class/8_1.html',
        'http://www.23wx.com/class/9_1.html',
        'http://www.23wx.com/class/10_1.html'
    ]

    def parse(self, response):
        books = response.xpath('//tr[@bgcolor="#FFFFFF"]')
        i = 0
        for book in books:
            id = str(i + 1)
            i = i+1
            name = book.xpath(". //td[1]//a[2]/text()").extract()
            link = book.xpath(". //td[1]//a[2]/@href").extract()
            new_para = book.xpath(". //td[2]//a/text()").extract()
            author = book.xpath(". //td[3]/text()").extract()
            words = book.xpath(". //td[4]/text()").extract()
            date = book.xpath(". //td[5]/text()").extract()
            status = book.xpath(". //td[6]/text()").extract()
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
            yield scrapy.Request(str(link), callback=self.parse_chapters)

        nextpage = response.xpath("//div[@id='pagelink']//a[@class='next']/@href").extract()
        if nextpage:
            yield scrapy.Request(str(nextpage))

    def parse_chapters(self, response):
        chapters = response.xpath("//tbody//td[@class='L']/a")
        i = 0
        for chapter in chapters:
            id = i+1
            name = chapter.xpath(". /text()").extract()
            base_link = str(response.url)
            link = base_link + chapter.xpath(". /@href").extract()

            yield scrapy.Request(link, callback=self.parse_chapters_contents, meta={
                'name':name,
                'id':id,
                'link':link
            })

    def parse_chapters_contents(self,response):
        item = DocumentItem()
        id = response.meta['id']
        name = response.meta['name']
        link = response.meta['link']
        content = response.xpath("//dd[@id ='contents']/text()").extract()

        item['id'] = id
        item['name'] = name
        item['link'] = link
        item['content'] = content

        return item