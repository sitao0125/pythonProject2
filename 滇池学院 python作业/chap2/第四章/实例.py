# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 16:58
import random


def FaHongBao(total,num):
    eachone = ''
    already=0
    for i in range(1,num):
        hb = round(random.uniform(0.01,(total-already)-(num-i)*0.01),2)
        eachone=eachone+str(hb)+','
        already =already+hb

    eachnoe = eachone +str(round((total-already),2))

    return eachnoe

total = 20
num =5
for i in range(10):
    eachone =FaHongBao(total,num)
    print(eachone)