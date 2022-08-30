# 存放学员信息的列表
list_data = []


# 增加数据
def add_data():
    a = True
    while a:

        new_name = input("请输入学员姓名：")

        global list_data
        dict_data = {}

        # dict_data["name"] = new_name
        #
        # list_data.append(dict_data)
        # print(new_name, "---同学的信息插入成功")
        for data in list_data:
            print(data['name'])
            if data['name'] == new_name:
                print('存在')
                list_data.remove(data)
                print('请重新添加')

            else:
                break
        dict_data["name"] = new_name

        list_data.append(dict_data)
        print(new_name, "---同学的信息插入成功")






        b = int(input("是否继续添加学员信息（1:添加   2:返回系统页面）："))
        if b == 2:
            print(list_data)
            a = False

add_data()
