# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/15 11:06
import math
P=float(input('请输入本金:'))
R=float(input('请输入年利率:'))
T=float(input('请输入年数:'))
F=P*(1+R/100)**T-P
print('本金利率和为:','%.2f'%F)