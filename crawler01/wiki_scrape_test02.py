from urllib.request import urlopen
from bs4 import BeautifulSoup

# 正则表达式
import re

import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, features="lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

# 循环获取页面中的url
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)