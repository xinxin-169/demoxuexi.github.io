class dd:
    def __init__(self,canshu):
        self.canshu = canshu
        print(canshu,'这个是参数')

    def no__init__(self,diaoyong):
        self.diaoyong = diaoyong
        print(self.diaoyong,'这个不是类的属性调用')


qaq = dd('参数')
qdq = dd('为什么这里还要填类的参数')
qdq.no__init__('这个是实例对象的调用')
