# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/8 21:26
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))