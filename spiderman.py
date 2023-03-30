import requests
import re
import os
from lxml import etree

def spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
    r = requests.get(url, headers=headers, timeout=100)
    content = r.content.decode("utf-8")

    res = re.compile(r'src="(https.+?.jpg)"')  # 运用正则表达式过滤出图片路径地址

    page = r.text
    print(r.status_code)  # 状态码
    print(r.raise_for_status())

    reg = re.findall(res, page)  # 匹配网页进行搜索出图片地址数组
    if not os.path.exists('./img'):
        os.mkdir('./img')

    # 循环遍历下载图片
    print(reg)
    num = 0
    for i in reg:
        a = requests.get(i)
        f = open("img/%s.jpg" % num, 'wb')  # 以二进制格式写入img文件夹中
        f.write(a.content)  # 下载链接是否成功状态码
        # print(a)
        f.close()
        print("第%s张图片下载完毕" % num)
        num = num + 1
spider("https://movie.douban.com/")