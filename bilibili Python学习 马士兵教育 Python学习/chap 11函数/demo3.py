# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 23:42
# 函数返回值
'''当函数返回多个值时  结果为元组'''
print(bool(0))
print(bool(8))


def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.qppend(i)
        else:
            even.append(i)
    return odd,even



lst=[10,29,34,23,44,53,55]
#print(fun[10,29,34,23,44,53,55])
print(fun(lst))


# 函数的返回值
#1. 如果没有返回值  不需要提供数据 return 可以不写
#2. 函数的返回值 如果是1个 直接返回类型
#03 多个  返回元组类型

