import time
import requests
class A(object):
    def __init__(self ):
        self.url =  'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&logid' \
        '=10247125497873696470&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7' \
        '%89%87&z=0&ic=0&hd=undefined&latest=undefined&copyright=undefined&s=undefined&se=&tab=0&width=&height=&face' \
        '=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=2468503377%2C3588140890' \
        '&catename=&nojc=undefined&album_id=&album_tab=&cardserver=&tabname=&pn=0&rn=30&gsm=2&1655103061695= '
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39 '
        }

    def get_html(self):
        respense = requests.get(self.url, headers=self.headers)
        return respense

    def get_json(self, respense):
        start = time.time()
        list_url = respense.json()['data']
        print(f"获取到的数据：{list_url}", )
        for i in list_url[:-1]:
            name = i['fromPageTitleEnc']
            name1 = i['thumbURL']
            print(f'{name}:{name1}')
            get_name = requests.get(url=name1,headers=self.headers)
            with open(f'img\\{name[:9]}'+'.jpg',mode='wb')as f:
                f.write(get_name.content)
        print('数据下载完成')
        end = time.time()
        print(f'下载时间：{end-start}')
    def go(self):
        xl = self.get_html()
        self.get_json(xl)
    def zhangmian(self):
        aa.get_html()
        aa.go()
if __name__ == '__main__':
    aa = A()
    aa.zhangmian()