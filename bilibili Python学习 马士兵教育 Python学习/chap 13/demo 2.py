# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/9 19:52
class Student: # student 是类名 要求 首字母 大写 其余字母小写  由一个或者多个单词组成
    native_pace='吉林' # 直接写在类里面的变量 称为类属性

    def __init__(self,name,age):
       self.name=name
       self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭...')

        # 静态方法
        @staticmethod
        def method():
            pirnt('我使用了 statticmethod进行修饰，所以我是静态方法')

      # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了 classmethod 方法 进行修饰')
    #在类 之外定义的 成为函数 在类 之内定义的称为方法
def drink():
    print('喝水')


#创建 Student 类的对象
stu1=Student('张三',20)  #????????????????????
print(id(stu1))
print(type(stu1))

stu1.eat() #对象名的方法名
Student.eat(stu1) # 与34 行 代码 意思相同 都是调用 Student 中的 eat 方法



