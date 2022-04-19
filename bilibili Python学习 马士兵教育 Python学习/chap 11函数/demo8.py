# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/8 21:04
def fun(a,b):
    c=a+b
    print(c)

    # pirnt(c)
#print(a)   # ac 超出了作用域

name='yanglao shi'
print(name)
def fun2():
    print(name)

    fun2()

def fun3():
    global age  # 局部变量使用global 声明  是全局变量
    age=20
    print(age)

fun3()
print(age)