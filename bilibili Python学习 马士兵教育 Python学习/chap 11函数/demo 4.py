# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/8 19:22
# 函数参数的 定义
'''个数可变的位置参数
使用* 定义个数可变的 位置形参
结果为一个元组

个数可变的关键字形参
定义函数 无法实现确定传递关键字实参个数 使用可变的关键字形参
使用 **定义 个数可变的关键字形参
结果为一个字典
'''

def fun(*args):
    print(args)



fun(10)
fun(10,.30)
fun(30,405,50)

def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)

print('hello','world','javA')

'''def fun2(args,*a):
pass
以上代码 程序会报错 可变的位置参数之恩那个是一个'''
#def fun2(**args,*a):
 #   pass
 # 个数可变的关键字参数也只能有一个

# def fun3(**args1,*args2):
 #    pass