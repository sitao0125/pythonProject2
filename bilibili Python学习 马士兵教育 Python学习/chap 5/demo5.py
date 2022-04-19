# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 22:06
print('输出100-999之间的水仙花数')
# 例如 153=3*3*3+5*5*5+1*1*1
for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    if ge**3+shi**3++bai**3==item:
        print(item)
