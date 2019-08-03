"""
通过Selenium模拟浏览器

Version 0.1
Author: Authorcai
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.santostang.com/2018/07/04/hello-world/")