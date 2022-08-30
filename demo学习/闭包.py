
def func1(myprint):
    def func2():
        print('打开外挂')
        myprint()
        print('关闭外挂')
    return func2
#mypr就是第二行里的myprint，不一样是因为传参只要设置参数在那里就行了
@func1
def mypr():
    print('欢迎来到王者荣耀')

mypr()

# def func():
#     print('这是闭包')
#     def func1():
#         print('这是func1')
#     return func1
# a=func()
# a()
def funcl(func):#外部闭包函数的参数是被装饰的函菱
    def func2():
        print('aaabbb')
        return func()#返回了外部函数接收的被装的
    return func2
#funcl（）takes 0 positional arguments but 1
#return func#返回了函数对象
#return func（）#返回的是一个函数调用
#funcl(myprint)（）#接收被装饰的函数作为参数，

#func2（）->
#
#
@funcl
def myprint():
    print('你好，我是print')

myprint()