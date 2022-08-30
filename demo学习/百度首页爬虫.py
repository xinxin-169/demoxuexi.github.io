

import requests
url = "http://www.baidu.com/"
resp = requests.get(url)
with open('baidu.html') as f:
    f.write('html')







