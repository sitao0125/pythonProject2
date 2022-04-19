# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 20:31
'''
获取字典视图的三个方法
1.keys（） 获取字典中所有key
2.values（） 获取字典中所有value
3.items（） 获取字典中所有key，value 对
'''
scores={'张三':100,'李四':98,'王五': 45}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))# 将所有 键组成的视图 转化成列表

#获取所有的值
values=scores.values()
print(values)
print(type(values))
print(list(values))

items=scores.items()
print(items)
print(list(items)) # 转换后的列表元素 是由元素组成的


