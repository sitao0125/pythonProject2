# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/9 19:00
# python 的异常处理机制
'''try except else 结构
没有抛出异常 执行 else 抛出异常
 执行except
'''

try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result =a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)

    '''try except else finally 结构'''
#finally 块 无论是否发生异常都会被执行 能常用来释放try块中 申请的资源
