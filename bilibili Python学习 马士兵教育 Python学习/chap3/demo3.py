# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/1 21:13
#比较运算符
a,b=10,20
print('a>b?\n',a>b)
print('a<b\n',a<b)
print('a<=b',a<=b)
print('a>=b?',a>=b)
#还有 == ！=
''' 一个 = 称为赋值运算符 两个= 称为比较运算符
一个变量由三部分组成,标识 类型 值 
== 比较的是值
比较对象的标识使用的是 is
'''
a=10
b=10
print(a==b)
print(a is b)
''' 说明 a 与b 的 value 和 id 都相等'''
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)
print(lst1 is lst2)
print(id(lst1),id(lst2))
print(a is not b)
''' 前面的链式赋值 a 和 b 的地址是一样的'''
print(lst1 is not lst2)
#bool运算符
# and or not in not in
a,b=1,2
print(a==1 and b==2)
print(a==1 or b==2)

print('----------对bool类型的操作数取反----------')
f=True
f2=False
print(not f)
print(not f2)

print('=======in 与 not in=========')
s='hello world'
print('w' in s)
print('k' in s)