# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/6 21:40
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))

print(s.lower(),id(s.lower()))
print(s,id(s))
b=s.lower()
print(b,id(b))
print(s,id(s))
print(b==s)
print(b is s)

s2='hello,python'
print(s2.swapcase())

print(s,id(s))