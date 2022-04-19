# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/8 20:19
def fun(a,b=10):  # b 称为 默认值 形式参数
    print('a=',a)
    print('b=',b)

def fun2(*args):
    print(args)

def fun3(**args2):
    print(args2)

fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)

def fun4(a,b,*,c,d):
    print('a',a)
    print('b', b)
    print('c', c)
    print('d', d)

    #fun4(10,20,,30,40)  #位置实参传递
    fun4(a=10,b=20,c=30,d=40)  # 关键字实参传递
    fun4(10,20,c=30,d=40)  #前两个位置实参传递 后两个关键字实参传递

