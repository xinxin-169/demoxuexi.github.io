
import lxml
from lxml import etree
import requests
url = "https://user.qzone.qq.com/1459244936/main"
resp = requests.get(url)
a = resp.text
b = etree.HTML(a)

with open("baidu.html","w",encoding="utf-8")as f:
    f.write(resp.text)































