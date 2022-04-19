# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/9 20:51
# 动态绑定属性和方法

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
print('---------为 stu2 动态绑定 性别属性-------------')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)


#动态绑定方法

print('''''''''''''''''''''''''''''')

stu1.eat()
stu1.eat()

def show():
    print('定义类之外 的 称为 函数')
stu1.show=show
stu1.show()

#stu2.show() 因stu2 没有绑定 方法
