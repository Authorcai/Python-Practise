"""
练习 : 使用Python爬虫访问静态页面获取英文

"""
import requests
from bs4 import BeautifulSoup

# 定制URL参数


# 定制headers,需要设置的key有 'user-agent' 'Host'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Host': 'movie.douban.com'
}


# 获取电影排名的函数
def get_movie(headers):
    link_base = 'https://movie.douban.com/top250?start='
    # 定义movie_list列表用于储存电影名
    movie_list = []
    for i in range(0, 10):
        # 1.link 和 headers
        link = link_base + str(i * 25)
        r = requests.post(link, headers=headers, timeout=10)
        # print(str(i + 1), "页响应状态码:", r.status_code)

        # 2.获取soup对象并解析
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')

        # print(div_list)
        # 3.依次将电影信息存入
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list


movie_list = get_movie(headers)
print(movie_list)
