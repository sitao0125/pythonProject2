# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/11 15:40
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # 年龄不希望在类 的外 被使用 所以加了两个_
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外使用name 与 age
print(stu.name)
#print(stu.__age)
print(dir(stu))
print(stu._Student__age) #在 类的外部 可以通过 _Student__age 进行访问

#继承



