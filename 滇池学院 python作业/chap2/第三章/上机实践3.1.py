# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 16:14
import turtle as t
for i in range(4):
    t.seth(90*(i+1))
    t.circle(200, 90)
    t.seth(-90+i*90)
    t.circle(200, 90)
t.done()