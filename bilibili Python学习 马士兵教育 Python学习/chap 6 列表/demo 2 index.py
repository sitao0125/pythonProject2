# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 9:39
lst=['hello','world',98,'hello']
print(lst.index('hello'))
# 列表中有相同元素 只返回列表中相同元素第一个元素
#print(lst.index('python'))
#可以在 指定的范围内 查找
print(lst.index('hello',1,3))
#换成 1，4 可以查找到 说明 查找是左闭右开的
'''获取列表中的单个元素'''
#正向索引 0 -N-1    逆向索引 -N ------ -1 指定索引不存在 抛出 indexerror

lst=['hello','world',98,'hello','world',234]
print(lst[2])
