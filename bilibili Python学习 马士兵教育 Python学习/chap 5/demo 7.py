# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 22:40
''' while'''
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

    a+=1

    for i in range(1, 51):
        if i % 5 == 0:
            print(i)

    #continue 语句


print('_____continue______')
for item in range(1,51):
    if item%5!=0:
        continue
        print(item)

