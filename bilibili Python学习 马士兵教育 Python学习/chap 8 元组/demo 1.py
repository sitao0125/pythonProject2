# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 22:03
# 元组
'''是 排 还是 散'''
'''元组  集合'''
'''元组 是不可变序列 是内置的数据结构
不可变序列没有增删改操作
（字符串元组
可变序列
（列表 字典
'''



'''可变序列
    列表 字典
    '''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列 字符串 元组'''
s='hello'
print(id(s))
s=s+'world'
print(id(s)) #内存地址发生了更改
print(s)

# 元组
# 列表使用[]定义 而元组 使用（） 定义
