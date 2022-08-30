
lst=[1,2,3,4,5,6,7,8,9,10]
def func(lst):
    jishu=[]#保存寄数
    oushu=[]#保存偶数
    for i in lst:
        if i%2==0:
            oushu.append(i)
        else:
            jishu.append(i)
    return jishu,oushu

print(func(lst))