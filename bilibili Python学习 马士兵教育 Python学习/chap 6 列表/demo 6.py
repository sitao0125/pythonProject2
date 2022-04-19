# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 20:46

#列表的移除
lst=[10,20,30,40,50,60,30]
lst.remove(30) #从列表中移除元素 如果有重复元素 只移除第一个
print(lst)

#lst.remove(100)
'''
删除操作 
remove（） 一次只删除一个元素   重复元素只删除第一个 元素不存在抛出valueerror
pop（）    删除一个指定索引位置上的元素   指定索引不存在抛出indexerror  不指定索引，删除列表中最后一个元素
切片       一次至少删除一个元素 
clear（）  清空列表
del（）    删除列表
'''
#pop 根据索引 移除元素
lst.pop(1)
print(lst)
#lst.pop(5)  # 如果指定索引位置 不存在 报错
# 如果不指定参数  索引将删除最后一个元素
lst.pop()
print(lst)

print('-------切片操作-删除至少一个元素-产生一个新的列表对象------------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)
#是产生了 一个新的 列表对象

#正儿八经 删除 源列表
lst[1:3]=[]
print(lst)   #所谓删除 使用空的去替代

# qing chu
lst.clear()
print(lst)
del lst
#print(lst)   #报错 没有定义 因为del 操作 将此列表删除了
