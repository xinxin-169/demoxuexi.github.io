def shuru():
    u = input('first:')
    i = input('second:')
    o = input('third:')
    h = '\n'
    with open('poety','a',encoding='utf-8') as a:
        a.write(u+h +i+h+ o+h )
def zhixing():
    f  = open('poety','r',encoding='utf-8')
    g = f.readlines()
    list  = []
    for data in g:
        print(data)
        list.append(data)
    print(list)
    del list[1]
    print(list)

    for i in list:
        print(i)
        with open('poety.txt','a',encoding='utf-8') as k:
            k.write((i))
def zong():
    shuru()
    zhixing()
zong()
#
#
# porty = '朝辞白帝彩云间，千里江陵一日还，两岸猿声啼不住，轻舟已过万重山'
# line = porty.split()
# print(line)
# list_data =[]
# for data in line:
#     list_data.append(str(data)+'\n')
# print(list_data)







# for i in g:
#     b = list(i)
# print(b)
# c = list.remove()



