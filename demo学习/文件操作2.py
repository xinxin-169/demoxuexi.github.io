porty = '朝辞白帝彩云间，千里江陵一日还，两岸猿声啼不住，轻舟已过万重山'
line = porty.split()
print(line)
list_data =[]
for data in line:
    list_data.append(str(data))
    with open('kkk.txt','a',encoding='utf-8') as z:
        z.write(data)

print(list_data)