# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 20:34
#range ()函数
'''
用于生成一个整数序列
创建range对象
range(stop)
'''
#range（stop) 小括号只给了一个数
r=range(10)#默认从 0 开始 相差 1  1为默认 步长
print(r)
# 返回值是一个迭代器对象
print(list(r))#用于查看range对象中的整数序列
a=range(3,10)
print(a)
print(list(a))
b=range(2,88,5)  # 三个数分别为 起始数 步长 末位数
print(list(b))
#in not in 判断整数序列中是否存在 （不存在  指定的整数
'''' 判断指定整数 是否在序列中存在'''
print(10 in b)
print(84 not in b)
print