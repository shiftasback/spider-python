import pandas as pd
from lxml import etree
import requests
import re
import os
import csv
from bs4 import BeautifulSoup
url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
page_text = requests.get(url = url,headers = headers,timeout=1000)
page_text.encoding = page_text.apparent_encoding
html = page_text.text
page = page_text.text
# print(page)
soup = BeautifulSoup(html,'lxml')

tree = etree.HTML(page_text.text)


paiming = tree.xpath('//td/div/text()')
paiming = [x.strip() for x in paiming]
paiming = paiming[::2]
# paiming = '<div class="ranking top1" data-v-3fe7d390>(.*?)</div>'
# paiminglist = re.findall(paiming,html)
# <td data-v-3fe7d390><div class="ranking top2" data-v-3fe7d390>               2             </div></td>


# paiming = tree.xpath('//div[@class="ranking"]/text()')
# paiming = [x.strip() for x in paiming]
# for i in range(1,4):
#         paiming.insert(i-1,str(i))




print('排名',paiming)
# print(paiming)
xuexiaomc = tree.xpath('//a[@class="name-cn"]/text()')
print((xuexiaomc))
shengshi = tree.xpath('//td[@data-v-3fe7d390=""]/text()')

shengshi1 = [x.strip() for x in shengshi]
# print(len(shengshi1))
# print(shengshi1)
diqu = shengshi1[::4]
leixing = shengshi1[1::4]
zongfen = shengshi1[2::4]
banxuechengc = shengshi1[3::4]
# print(diqu)
# print(leixing)
# print(zongfen)
print(banxuechengc)
print(len(diqu))
print(len(leixing))
print(len(zongfen))
print(len(banxuechengc))
Data = pd.DataFrame(
        { '排名':paiming,'学校名称':xuexiaomc,'地区': diqu, '类型': leixing, '总分': zongfen, '办学层次': banxuechengc})

Data.to_csv('spiderdata.school.csv', index=None,encoding='gbk')