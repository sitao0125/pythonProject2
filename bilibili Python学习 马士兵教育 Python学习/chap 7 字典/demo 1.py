# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 21:46
#字典
'''列表使用[] 定义  而 字典 使用{}定义'''
# 字典当中 是以 一对的形式出来的 ’张三‘ ： 100，  冒号之前叫 键 之后叫 值

#python 中 字典 是根据key 来查找 value所在位置

#创建 字典 常用方式
# 使用花括号
scores={'张三':100,'李四':98,'王五': 45}
print(scores)
print(type(scores))
#使用内置函数dict（）
student=dict(name='jack',age=20)
print(student)
#创建空 字典
d={}
print(d)