class dd:
    def __init__(self,name,char):
        self.name = name
        self.char = char
        print(self.name,self.char)

    def qqq(self,w,e):
        self.w = w
        self.e = e
        print(self.w,self.e,'woshi')

qwq = dd('','')#可以不赋值
qwq.qqq('会','不会')#非init可以不用self,有也可以运行


# class dd:
#     def __init__(self,name,char):
#         self.name = name
#         self.char = char
#         print(self.name,self.char)
#
# qaq = dd()
# qaq.__init__('艾希','欧亚')#init里边需要self