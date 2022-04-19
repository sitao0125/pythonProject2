# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/up2/6 19:20
# 集合的关系
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)
print(s!=s2)#fales

#一个集合是否为另一个集合的子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s1))

# 一个集合是否为另一个集合的超集
print(s1.issuperset(s2))
print(s1.issuperset(s3))
# 两个集合 是否no有 交集  isdisjoint

print(s2.isdisjoint(s3))
s4={100,200,300}

print(s2.isdisjoint(s4))