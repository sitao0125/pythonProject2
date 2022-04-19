# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 20:47
#字典元素 遍历
scores={'张三':100,'李四':98,'王五': 45}

for item in scores:
    print(item,scores[item],scores.get(item))

# 字典的特点
'''
字典所有元素都是一个key—value对  key不允许重复 value 可以重复
字典中元素是无序的
字典中的key必须是不可变对象
字典也可以根据需要动态的伸缩
字典会浪费较大的内存 是一种使用空间换时间的数据结构
'''
d={'name':'张三','name':'李四'}
print(d)

d={'name':'张三','nikename':'张三'}
print(d)

lst=[10,20,30]
lst.insert(1,100)
print(lst)

#字典的 键 必须是一个不可变对象 如果用列表去作为对象是不可以的
#d={lst:100}
#print(d)

