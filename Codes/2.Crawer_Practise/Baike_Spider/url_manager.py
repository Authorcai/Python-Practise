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

    def add_new_url(self, root_url):
        pass

    def add_new_urls(self, new_urls):
        pass

    def has_new_url(self):
        pass

    def get_new_url(self):
        pass

