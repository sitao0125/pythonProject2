# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 9:58


# 获取列表中的多个元素
# 列表名[start : stop : :step]
lst=[10,20,30,40,50,60,70,80]
#start =1,stop=6,step=1
print(lst[1:6:1])
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段：',id(lst2))
# 切出来的片段 是独立的一个
print(lst[1:6:])
print(lst[1:6:2])

print(lst[:6:2])

#start 1  step 2 stop
print(lst[1::2])

'''step 为 负数 默认是从最后开始的'''
print('步长为负数')
print('原列表：',lst)
print(lst[::-1])
# start 7 stop   step -1
print(lst[7::-1])
print(lst[6:0:-2])
