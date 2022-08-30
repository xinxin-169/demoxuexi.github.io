list = []
def add_date():
    # global  list
    # while d:
    id  = input('请输入学生姓名')
    dict_date = {}
    dict_date['name'] = id
    if id in dict_date:
        print('已存在')
    else:
        list.append(dict_date)
        print(list)



    # if id in dict_date:
    #     print('已存在')
    #
    # print(list)

    #     if id in dict_date:
    #         print('已存在,请重新添加')
    #     else:
    #         list.append(id)
    #         print('添加成功')
    # c = input('请选择接下来的操作 1：添加 2：返回系统界面')
    # if c == 2:
    #     print(list)
    # d = False






add_date()






