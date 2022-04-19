# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 19:34
# 多分支结构
''' if  条件表达式 1：
条件执行体1
    elif  条件表达式2：
条件执行体2
 [else:]'''
''' 从键盘录入一个整数成绩
90-100  A
80-89   B
70-79   C
60-69   D 
0-59    E
小于 0或 大于 100为非法数据
'''
score=int(input('请输入一个成绩'))
if score>=90 and score<=100:
    print('A')
elif score>=80 and score<=89:
    print('B')
elif score>=70 and score<=79:
    print('C')
elif score>=60 and score <= 69:
    print('D')
elif score>=0 and score <=59:
    print('E')
elif score<0 or score>100:
    print('非法数据')


