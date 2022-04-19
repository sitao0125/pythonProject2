# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 21:18
'''
列表的排序 操作
调用sort（）方法  列表中的所有元素按 从小到大的顺序排序 可以指定 reverse=true ，进行降序排序
调用内置函数 sorted（） 可以指定 reverse=True 进行降序排列 原列表不发生改变
'''
lst=[20,40,10,98,54]
print('开始前的列表',lst,id(lst))
lst.sort()
print('排序后的列表',lst,id(lst))

# 通过指定关键数参数 对列表中参数 进行 降序排列
lst.sort(reverse=True)
print(lst)

lst.sort(reverse=False)
print(lst)  #不指定 reverse 默认 升序

#使用内置函数 sorted 进行排序 会产生一个新的列表对象
lst=[20,40,10,98,54]
print('原列表',lst)
new_list=sorted(lst)
print(lst,id(lst))
print(new_list,id(new_list))

#指定关键字 参数  实现降序排列
desc_list=sorted(lst,reverse=True)
print(desc_list)

# 区别 sort 是对原列表的一个操作  而 sorted 是产生一个新列表 对原列表不产生影响

#列表生成公式

