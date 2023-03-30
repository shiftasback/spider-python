import requests
from bs4 import BeautifulSoup as btf
url = "https://movie.douban.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47"}
r = requests.get(url, headers=headers, timeout=100)
r.encoding = r.apparent_encoding
soup = btf(r.text,'lxml')
result = soup.find_all(name='img')
for i in result:
    print(i)
print(soup)