# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/1/31 20:25
#整数类型 可以表示 正数负数 0
n1=90
n2=-96
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数表示为二进制 八进制 十进制
print('十进制',118)
print('二进制',0b10101111)
#八进制 0o 十六进制 0x 二进制 0b
#浮点值
a=3.14159
print('a',type(a))
#浮点数存储不精确 可以通过导入模块 decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))