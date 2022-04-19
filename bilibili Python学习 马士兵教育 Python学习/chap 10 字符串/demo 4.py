# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/6 22:21
 # 字符串劈分 操作
'''
split()
rsplit()
'''
s='hello world python'
lst=s.split()
print(lst)

s1='hello|world|python'
print(s1.split(sep='|'))

print(s1.split(sep='|',maxsplit=1))
print(s1.rsplit(sep='|',maxsplit=1))



