# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 15:49
#求1~100的素数
import math
for i in range(2,101):
    n=int(math.sqrt(i))+1
    for j in range(2,n):
        if i % j == 0:
            break
    else:
        print(i,end=" ")