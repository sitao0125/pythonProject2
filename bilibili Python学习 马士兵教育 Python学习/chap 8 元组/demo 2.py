# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 22:24
'''元组的创建
1.直接小括号
2.使用内置函数tuple（）
3.只包含一个元组的元素需要使用逗号和小括号
'''
#1
t=('python','world',98)
print(t)
print(type(t))
t2='python','world',98
print(t2)
print(type(t2))

t3=('python',)
print(t3)
print(id(t3))
#2 内置函数 tuple（）
t1=tuple(('python','world',98))
print(t1)
print(type(t1))


# 空 元组
lst=[]
lst1=dict()
#空元组
d={}
d2=dict()
t4=()
t5=tuple()
print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)