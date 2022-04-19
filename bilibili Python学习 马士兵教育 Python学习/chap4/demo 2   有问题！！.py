# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/1 22:22
#分支结构
money=1000
s=int(input('请输入取款金额'))
if money>=s:
    money=money-s
    print('取款成功 余额为：',money)
#双分支结构
'''' 从键盘录入一个整数 让计算机判断是奇数还是偶数'''
num=int(input('请输入一个整数'))
if num%2==0:     #为啥这里这个 if 往后去一格就报错 顶着头 就正确
     print(num,'是ou数')
else:
     print(num,'是ji数')


