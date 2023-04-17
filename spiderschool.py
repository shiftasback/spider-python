import pandas as pd
from lxml import etree
import requests
import re
import os
import csv
from bs4 import BeautifulSoup
def requestUrltext():
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
    page_text = requests.get(url=url, headers=headers, timeout=1000)
    page_text.encoding = page_text.apparent_encoding
    html_text = page_text
    tree = etree.HTML(html_text.text)
    return tree


def list_get(tree):
    paiming = tree.xpath('//td/div/text()')
    paiming = [x.strip() for x in paiming]
    paiming =paiming[::2]
    xuexiaomc = tree.xpath('//div/a[@class="name-cn"]/text()')
    shengshi = tree.xpath('//td[@data-v-3fe7d390=""]/text()')
    shengshi1 = [x.strip() for x in shengshi]
    diqu = shengshi1[::4]
    leixing = shengshi1[1::4]
    zongfen = shengshi1[2::4]
    banxuechengc = shengshi1[3::4]
    print(len(shengshi))
    return paiming,xuexiaomc,diqu,leixing,zongfen,banxuechengc


def csv_return(paiming,xuexiaomc, diqu, leixing,zongfen,banxuechengc):
    Data = pd.DataFrame(
            { '排名':paiming,'学校名称':xuexiaomc,'地区': diqu, '类型': leixing, '总分': zongfen, '办学层次': banxuechengc})

    Data.to_csv('spiderdata.csv', index=None,encoding='gbk')
    return ("xieru")

a = requestUrltext()
paiming,xuexiaomc,diqu,leixing,zongfen,banxuechengc = list_get(a)
csv_return(paiming,xuexiaomc,diqu,leixing,zongfen,banxuechengc)