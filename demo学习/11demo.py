
#break与continue的区别
for i in range(1,5):
    for j in range(1,11):
#如果if里边是错的则打印一次print,如果是对的话就不打印，继续执行小循环体，如果为false则就打印一个j
#break错了的话直接就打印一个值，再进行下一判定循环
        if j%2 == 0:
            continue
        print(j,end='\t')

