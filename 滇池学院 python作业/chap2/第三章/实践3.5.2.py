# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 15:43
#猜数字游戏

import random

x=random.randint(1,10)

for i in range(1,4):
    m=eval(input("请输入一个整数："))
    if x ==m:
        print("恭喜，猜对了，一共猜了{}次".format(i))
        break
    elif m<x:
        print("猜小了")
    else:
        print("猜大了")
    if i == 3:
        print("游戏结束")