# input 输入
password = input("请输入你的密码")

# for循环3次
for ii in range(3):
    if password == "111": # True
        print('正确')
        break # 退出
    # 多条件判断
    # 一个正确条件不够用时，再加入elif条件多加一个正确条件判断
    elif password == "666":
        print("666正确")
        break

    elif password=="888":
        print("888正确")
        break

    else:

        print("cuowu")
#jiuge亲授




"""
if 判断正确的结果 True

else 是执行不正确结果 False


"""











