import requests
import re
from lxml import etree

def gettext(tree):
    titlename = tree.xpath('//div[@class="border"]/h1/text()')
    listtext = tree.xpath('//div[@id="content"]/text()')
    listtext = [x.strip() for x in listtext]
    return titlename, listtext


def forrange(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
    page_text = requests.get(url=url, headers=headers, timeout=2000)
    page_text.encoding = page_text.apparent_encoding
    tree = etree.HTML(page_text.text)
    return tree

def listnumget(urllist):
    # /// 章节序号获取 ///
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
    page_text = requests.get(url=urllist, headers=headers, timeout=2000)
    page_text.encoding = page_text.apparent_encoding
    treenum = etree.HTML(page_text.text)
    # regex = r'<dd><a href="(.*?).html"></a>.*?</dd>'
    # resultnum = re.findall(regex, page_text.text)
    numlist = treenum.xpath('//div[@class="zjbox"]/dl/dd/a/@href')
    # numlist = [x.strip('.html') for x in numlist]
    # numlist1 = [x.replace('.html','') for x in numlist]
    return numlist
    """,numlist1"""

f = open("sywz.txt", "a",encoding='utf-8')

for j in("https://www.bbiquge.net/book/59265/","https://www.bbiquge.net/book/59265/index_2.html"):

    numlist = listnumget(j)
    print(listnumget(j))
    for i in numlist:
        urlzji = "https://www.bbiquge.net/book/59265/"+str(i)
        print(urlzji)
        tree = forrange(url=urlzji)
        titlename, listtext = gettext(tree)
        for j in titlename:
            f.write(str(j) + "\n")
        for i in listtext:
            f.write(str(i) + "\n")
f.close()

