import urllib.request
"""
由于百度百科的页面下载较为简单,只使用了一种urrllib.request 这一个第三方库
遇到其他复杂的页面或者站点,需要更为复杂的操作实现对页面的下载
"""

class HtmlDownloader(object):

    def download(self, url):
        if url == None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()