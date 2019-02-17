from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features="lxml")

# findAll()方法可以发现所有特定标签
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    # get_text()方法可以取出标签
    print(name.get_text())