# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 22:06
#字典元素的获取  []
scores={'张三':100,'李四':98,'王五': 45}
''' 第一种方式使用 []'''
print(scores['张三'])
#print(scores['陈六'])  # 会报错
''' 第二种方式 使用get()fangfa'''
print(scores.get('张三'))
print(scores.get('陈六'))  #会显示 none
print(scores.get('麻七',99))#99是查询 麻7 不存在的默认值
