from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features="lxml")

# 获取子代标签内容
print("******** 子代标签内容 ********")
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

# 获取后代标签内容
print("******** 后代标签内容 ********")
for child in bsObj.find("table", {"id":"giftList"}).descendants:
    print(child)

# 处理兄弟标签
# previous_siblings、next_siblings--获取多个
# previous_sibling、next_sibling
print("******** 处理兄弟标签 ********")
for child in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(child)

# 使用正则表达式
print("******** 使用正则表达式 ********")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
