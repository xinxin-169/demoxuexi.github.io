# 写入创建文件：写好里面的东西
def Write_Create_File(a):
    # name = "诗是一种最集中地反映社会生活的文学样式，它饱含着丰富的想象和感情，常常以直接抒情的方式来表现，而且在精炼与和谐的程度上，特别是在节奏的鲜明上，它的语言有别于散文的语言又有音乐之美。"
    print(a)
    name_1 = a.split('，')
    name_1_1 = '\n'
    name_list = []
    for i in name_1:
        name_list.append(i + name_1_1)
    lists1,lists2 = name_list[:1], name_list[2:]
    cc = lists1 + lists2
    return cc
# 打开文件写入:删除第二据话
def Open_File(cc,a):
    for data in cc:
        with open(a, 'a', encoding='utf-8') as k:
            k.write(data)

#  整体
def xiao():
    b = input('请输入你的诗词：')
    c = input('请输入文件名：')
    a = Write_Create_File(b)
    Open_File(a,c)

aa = xiao()