name = "诗是一种最集中地反映社会生活的文学样式，它饱含着丰富的想象和感情，常常以直接抒情的方式来表现，而且在精炼与和谐的程度上，特别是在节奏的鲜明上，它的语言有别于散文的语言又有音乐之美。"
print(name)
a = name.split('，')
b = '\n'
c = []
for i in a:
    c.append(i+b)
aa = c[:1]
bb = c[2:]
cc = aa+bb
for data in cc:
    print(data)
    with open('ttt.txt','a',encoding='utf-8') as k:
        k.write(data)