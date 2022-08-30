import requests
url = "https://www.baidu.com/"
headers = {"useragent": "Mozilla/5.0 (Windows NT 10.0: Win64: x64) AppleWebKit/537.36 'KHTML, like Gecko' Chrome/103.0.0.0 Mobile Safari/537.36"}
resp = requests.get(url,headers=headers)
resp.encoding="utf-8"
with open("baidu.html","w",encoding="utf-8")as f:
    f.write(resp.text)




    