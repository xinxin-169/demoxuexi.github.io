


#
# x = ['dsakldh','dasiod','dsjald']
# # print(x.index())
# print('james'in 'j')
# list = [1,2,3]
# list2 = list[1:2：1]
# print()
import xml.dom

lst = [1,23,33]
lst.pop(0)
print(lst)
print(lst.index(23))
lst2 = [10,45,23,78,12]
print("未排序的元数据",lst2)
lst2.sort(reverse=True)
print(lst2,id(lst2))
new_lst = sorted(lst2)
print(new_lst)