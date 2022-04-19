# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 21:52
# for-in 循环
# for 自定义变量 in 可迭代对象：循环体
for item in'python':
    print(item)

#range 也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用自定义变量，可将自定义变量写为"_"
for _ in range(5):
    print('ren sheng ku duan wo yong python ')

print('使用 for 循环 ，计算1 到 100 偶数和')
sum=0
for item in range(1,101):
    if item% 2==0:
        sum+=item

print('1dao 100 偶数和 为：',sum)
