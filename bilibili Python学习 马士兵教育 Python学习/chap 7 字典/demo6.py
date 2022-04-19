# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 21:20
# 字典生成式
# 内置函数 zip（） 生成 字典

items=['Fruits','Books','Others']
prices=[96,78,85]

d={item.upper():price  for item,price in zip(items,prices)}
print(d)

#列表元素 个数不相同


