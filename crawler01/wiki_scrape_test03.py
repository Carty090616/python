from urllib.request import urlopen
from bs4 import BeautifulSoup

# 正则表达式
import re

# 从主页开始寻找，并实现链路去重
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org")
    bsObj = BeautifulSoup(html, features="lxml")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到新页面
                newPages = link.attrs['href']
                print(newPages)
                pages.add(newPages)
                getLinks(newPages)

getLinks("")