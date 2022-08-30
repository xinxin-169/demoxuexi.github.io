


class Student():
    tizhong = 100
    shengao = 1000
    def __init__(self,high,wigh):
        self.high=high
        self.wigh=wigh


s1 = Student(100,1000)
print(s1.__init__(100,1000))



'''
class  Student():
    company = "SXT"
    count = 0
    def __init__(self,name,score):
        self.name=name
        self.score=score
        Student.count += 1

    def say_score(self):
        print("我的学校是：",self.company)
        print(self.name,'的分数是：',self.score)

s1 = Student("张三",80)
s1.say_score()
print('一共创建{0}个对象',format(Student.count))
'''

