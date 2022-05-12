# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 20:21
import math
def yuan(r):

    d=math.pi*2*r
    s=math.pi*(r**2)
    print("圆的周长是：",'%.2f'%d)
    print("圆的面积是：",'%.2f'%s)

r=float(input("please enter the r of the circle"))

yuan(r)