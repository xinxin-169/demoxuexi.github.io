
def search_info():
    """查询学员"""
    # 1. 输入要查找的学员姓名：
    global list_data
    list_data = [{'name':'小明'}]
    search_name = input('请输入要查找的学员姓名：')


    # 2. 判断学员是否存在：如果输入的姓名存在则显示这位学员信息，否则报错提示
    for i in list_data:
        if  i['name']==search_name:
            print(search_name,'已存在')
            break
    else:
        print('该学员不存在')
    b = int(input('是否再次寻找  1.y/2.n \n'))
    if b == 2:
        print('结束使用')
    elif b ==1:
        return search_info()












if __name__ == '__main__':

    search_info()