# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/3 20:54
print('_____continue______')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)   #又是一个 格式产生的问题 如果print 和continue 对齐了 就不会打印结果了



    #else 和 while for 搭配  循环中没有 碰到break 就不会执行 else

for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
          print('密码不正确')
else:
    print('对不起 三次密码输入错误')