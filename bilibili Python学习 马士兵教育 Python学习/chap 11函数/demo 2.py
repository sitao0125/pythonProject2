# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 23:02
#函数参数传递
def calc(a,b): # a b 为形式参数
    c=a+b
    return c

result=calc(10,20) #10 20 为实际参数
print(result)

#传递参数的方式
'''
位置对应
关键字实际参数
'''


res=calc(b=10,a=20)
print(res)

def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    return


n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)

''' 
在函数调用过程中 进行参数传递
若果是不可变对象 在函数体的修改不会影响实参的值 
如果是可变对象 则会影响'''
