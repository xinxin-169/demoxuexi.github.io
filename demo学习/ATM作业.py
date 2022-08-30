def ATM(money):
    sca = int(money)
    print('您的余额为'+str(sca))
    shuru = int(input('请选择操作 \n1.存款 2.取款\n请输入'))
    # intake  = int(input('请输入存款金额'))

    if shuru==1:
        intake = int(input('请输入存款金额'))
        yue = sca + intake
        print('您的余额为',str(yue))
    elif shuru==2:
        take = int(input('请输入取款金额'))
        yue = sca -take
        print('您的余额为',str(yue))
    else:
        print('请重新选择操作')
        return  ATM(money)
ATM(100)