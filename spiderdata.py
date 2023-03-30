import pandas as pd
from lxml import etree
import requests
import os
import csv
from bs4 import BeautifulSoup
import re

# 小区名称、参考均价、90天成交数、当前出租数、建成年份、地址

#           }
commentcounts = []
districts = []
nintyresults = []
nowhires = []
addresss = []
tureaddresss = []
whenbulids = []
urldata=['yuhua','kaifu','furong','changshaxian','yuelu','tianxin']      #  'wangcheng','liuyang','ningxiang']
for i in urldata:
    print(i)
    for j in range(1,11):
        if j<=1:
            url = 'https://cs.lianjia.com/xiaoqu/'+i+'/pcro21/'
        else:
            url = 'https://cs.lianjia.com/xiaoqu/'+i+'/pg'+str(j)+'cro21/'


        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
        page_text = requests.get(url = url,headers = headers,timeout=1000)          # 请求发送
        page_text.encoding = page_text.apparent_encoding

        tree = etree.HTML(page_text.text)                                   #数据解析
        page = page_text.text
        commentcount = tree.xpath("//div[@class='title']/a/text()")     #小区名称

        # print('小区名称')
        # print(commentcounts)

        for s in commentcount:
            commentcounts.append(s)

        # district = tree.xpath("//div[@class='totalPrice']/span//text()")   # 参考均价
        # for l in district:
        #      districts.append(l)

        regex1 = '<div class="totalPrice"><span>(.*?)</span>(.*?)<sup>2</sup></div>'
        district = re.findall(regex1, page)
        for l in district:
                districts.append(l)
        # print(districts)
        print(j)
        print(len(districts))

        housestate = tree.xpath("//div[@class='houseInfo']/a/text()")
        nintyresult = housestate[::2]
        for j in nintyresult:
            nintyresults.append(j)
        nowhire = housestate[1::2]
        for k in nowhire:
            nowhires.append(k)
        # print('九十天成交数')
        # print(nintyresults)
        # print('当前出租数')
        # print(nowhires)

        whenbuild = tree.xpath("//div[@class='positionInfo']/text()")
        whenbuild = [x.strip() for x in whenbuild]

        whenbuild = whenbuild[3::4]
        for a in whenbuild:
            whenbulids.append(a)
        # print(len(whenbuild))
        # print('建成年份')
        # print(whenbuild)

        address = tree.xpath("//div[@class='positionInfo']/a[@class='district']/text()")  # 小区地址
        for m in address:
            addresss.append(m)
        regex = '<a href=.*? class="bizcircle" title=".*?">(.*?)</a>'
        tureaddress = re.findall(regex, page)   # 详细地址
        for s in tureaddress:
            tureaddresss.append(s)

        # print('小区所在地')

        # print('详细地址')
        # print(len(tureaddress))

whenbulids1 = [i.split('/\xa0'[1]) for i in whenbulids]
# print(whenbulids1)

whenbulids2 =[]
whenbulids2 = [x[1] for x in whenbulids1]
print(whenbulids2)
# 小区名称、参考均价、90天成交数、当前出租数、建成年份、地址

if not os.path.exists('./spiderdata.csv'):
        os.mkdir('./spiderdata.csv')
print(len(addresss))
print(len(tureaddresss))
print(len(commentcounts))
print(len(districts))
print(len(nintyresults))
print(len(nowhires))
print(len(whenbulids2))
Data = pd.DataFrame(
        { '小区名称': commentcounts, '小区参考均价': districts, '90天成交数': nintyresults, '当前出租数': nowhires, '所在地区': addresss,'详细地址':tureaddresss,'建成年份':whenbulids2})

Data.to_csv('spiderdata.csv', index=None,encoding='gbk')
