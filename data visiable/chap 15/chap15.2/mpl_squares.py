# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/15 10:33
import matplotlib.pyplot as plt

squares =[1,4,9,16,25]

plt.plot(squares,linewidth=5) #决定了plot（）绘制线条的粗细

#设置图表标签，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)  #fontisize指定了图表中文字的大小
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both',labelsize=14)

#1.   plt.plot(squares)
plt.show()

