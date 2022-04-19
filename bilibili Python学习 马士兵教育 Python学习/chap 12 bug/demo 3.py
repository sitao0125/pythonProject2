# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/9 19:15
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result =a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)
finally:
    print('谢谢您的使用')
