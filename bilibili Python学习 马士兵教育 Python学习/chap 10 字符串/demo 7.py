# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 21:00
#字符串 的切片操作
# 字符串是不可变类型 不可以执行 增删改 操作  切片都将 产生 新的对象

s='hello,python'
s1=s[:5] # 由于没有指定起始位置 从0 开始

s2=s[6:]  # 由于没有指定结束位置 所以指向字符串结束
print(s1)
print(s2)
s3='!'
newstr=s1+s2+s3
print(newstr)
print('------------------------')
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))


print('------------切片---------------')
print(s[1:5:1])
print(s[::2])

print(s[::-1])

print(s[-6::1])