import pandas as pd
from lxml import etree
import requests
import re
import os
import csv
from bs4 import BeautifulSoup
url = 'https://cs.lianjia.com/xiaoqu/tianxin/cro21/'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
page_text = requests.get(url = url,headers = headers,timeout=1000)
html = page_text.text
page = page_text.text
soup = BeautifulSoup(html,'lxml')
tree = etree.HTML(page_text.text)
# tureaddress = tree.xpath("//div[@class='positionInfo']/a/text()")   # 详细地址
# print(len(tureaddress))
# print(tureaddress)
a = (soup.find_all('a',class_='bizcircle'))
b = (soup.find_all('div',class_='totalPrice'))
print(b)
regex = '<a href=.*? class="bizcircle" title=".*?">(.*?)</a>'
tureaddress = re.findall(regex, page)
regex1 = '<div class="totalPrice"><span>(.*?)</span>(.*?)<sup>2</sup></div>'
district = re.findall(regex1, page)
print(district)
print(len(district))

