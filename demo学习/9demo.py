
#查询3次密码不正确后else在for下的使用
for ii in range(3):
    pwd = input('请输入密码')
    if pwd == '666':
        print('输入密码正确')
        break
    else:
        print('输入密码正确')
else:
    print("duibuqiyijinsanci")

x = 0
while x <3:
    pwd = input('请输入密码')
    if pwd == '666':
        print('输入密码正确')
        break
    else:
        print('输入密码正确')
        x +=1
else:
    print("duibuqiyijinsanci")