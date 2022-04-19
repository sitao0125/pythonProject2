# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 22:24
#break 语句
'''从键盘录入密码 最多三次 正确就结束'''
for item in range(3):
    pwd=input('请输入密码')
    if pwd =='8888':
        print('密码正确')
    break
   else:
         print('密码不正确')
#要注意 格式 例如break 一定要与if 在同一个体 内