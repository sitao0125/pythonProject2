# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/6 19:41

'''集合 的 数学操作'''
# 交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)   #& 与 intersection 等价

#并集操作
print(s1.union(s2))
print(s1| s2)  # deng jia
print(s1)
print(s2)

# 差集操作
print(s1.difference(s2))

print(s1-s2)

# 对称 差集
print(s1.symmetric_difference(s2))
print(s1 ^s2)




