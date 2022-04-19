# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/11 17:10
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄：{1}'.format(self.name,self.age))

#定义子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

#测试
stu=Student('jack',20,'1001')
stu.info()