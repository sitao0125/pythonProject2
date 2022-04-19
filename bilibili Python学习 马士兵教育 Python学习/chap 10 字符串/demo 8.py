# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 21:10
# 格式化 字符串

#  % 作为占位符
name='张三'
age=20
print('我叫%s，今年%d岁' % (name,age))

#2 花括号 {}

print('我叫{0},今年{1}岁'.format(name,age))

#3  f-string
print(f'我叫{name},今年{age}岁')

print('%10d % 99')
