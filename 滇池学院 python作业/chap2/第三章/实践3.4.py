# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 16:47
m=int(input("请输入一个数："))
n=int(input("请输入另一个数："))
c=''
if m>n:
    min=n
else:
    min=m
for i in range(1,min+1):
    if(m%i==0)and(n%i==0):
        c=i
print('这两个数的最大公约数是：',c)