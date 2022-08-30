#元组只有三部分
t = ('james',[20,30],'开玩笑的')
print(t[0],t[1],t[2])
print(type(t[0]),id(t[1]))
k = t[1].insert(1,100)
k = t
print(k)

#元组里边的元素用【】
#遍历

s = {1,2,3,}
print(type(s))