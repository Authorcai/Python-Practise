"""
Url管理器需要维护两个集合:
    已爬取URL集合: old_urls
    未爬取url集合: new_urls
Url管理器需要实现的功能:
    1.(批量)添加新的url
    2.判断有无新的url
    3.(批量)返回新的url
"""
class UrlManager(object):
    def __init__(self):
        # 设置已爬取和未爬取的URL集合
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url == '':
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        tag = len(self.new_urls) != 0
        return tag

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

