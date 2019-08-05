#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Crawer_main.py    
@Contact :   icsh98@163.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-08-04 20:07   Authorcai      1.0    baidu_spider
'''

import html_dowload
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    """
    初始化url管理器 网页下载器 网页解析器 数据处理器
    """
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_dowload.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 从跟url开始,循环判断是否有新的url
        """
        若存在新的url,则
        1.获取 new_url
        2.通过 new_url 下载 html_content
        3.通过 html_content 提取出的 new_urls, new_data
        4.添加 new_urls, 处理new_data
        """
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s' %(count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                self.outputer.oouput_html()
                if count== 1000:
                    break

                count = count+1
            except:
                print('craw error')
        print("ok")

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
