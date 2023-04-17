from lxml import etree
import requests
import re
from lxml import etree

url = "https://www.bbiquge.net/book/59265/57967084.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
page_text = requests.get(url=url, headers=headers, timeout=2000)
page_text.encoding = page_text.apparent_encoding
tree = etree.HTML(page_text.text)
titlename = tree.xpath('//div[@class="border"]/h1/text()')
listtext = tree.xpath('//div[@id="content"]/text()')
listtext = [x.strip() for x in listtext]
strtext = listtext
print(titlename)
print(strtext)

f = open("sywz.txt", "a",encoding='utf-8')
f.write(str(titlename)+"\n")
for i in strtext:
    f.write(str(i)+"\n")
f.close()


