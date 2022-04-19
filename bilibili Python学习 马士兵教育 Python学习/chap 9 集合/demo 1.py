# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 23:39
# 集合
'''与列表 字典一样都属于可变类型的序列
集合是没有value 的字典
'''

# 创建 集合
'''
1.使用花括号
'''
s={2,3,4,5,5,6,7,7}# 集合中元素不允许重复
print(s)

'''2. 使用内置函数set（）'''
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,4,5,6])
print(s2,type(s2))

s3=set((1,2,4,4,5,65))  #集合特点是 无序的
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))

s5=set({12,4,34,55,66,44,4})
print(s5,type(s5))


#定义一个空集合
s6={}  #dict 字典类型
print(type(s6))

s7=set()
print(type(s7))
