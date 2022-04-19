# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/5 20:22
# 字典的常用操作
'''key 的判断'''
scores={'张三':100,'李四':98,'王五': 45}
print('张三' in scores)
print('张三' not in scores)
del scores['张三']

#scores.clear()
print(scores)
scores['陈六']=98#新增元素
scores['陈六']=188 #新增元素
print(scores)