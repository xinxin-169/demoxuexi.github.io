
class Student:
    def eat(self):
        print('chishiwanfan')
    @staticmethod
    def method():
        print('23')
    @classmethod()
    def classmathod(cls):
        print("这个是什么方法")



a =  Student()
print(a.eat)
Student.method(a.eat())

