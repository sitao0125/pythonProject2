# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 20:09
print('p'in 'python')
print('k'not in 'python')



lst=[10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

print('----------------')
for item in lst:
    print(item)

#列表元素的 增删 改
#向列表末尾添加一个元素
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
#标识对象没有改变


''' 
增加操作  append（）
        extend()
        insert()
        切片
'''
lst2=['hello','world']
#lst.append(lst2)
print(lst) # 将 lst2 作为一个整体 赋给 lst
lst.extend(lst2)  # 列表末尾 添加多个元素
print(lst)

#在任意位置添加元素
lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
#在任意位置上添加N多个元素
lst[1:]=lst3
print(lst)  #1 是起始位置 起始位置之后的内容被切掉