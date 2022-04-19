# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/6 20:34
# 字符串 的驻留 机制
a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
# 三个 字符串的 地址 都相同

# 字符串在编译时 驻留 而非运行时
# 字符串· 常用操作
'''
查询 index()
rindex()
find() -1
rfind() -1
'''

s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))
print(s.rfind('k'))

# 字符转换
'''upper 小转大
lower 大转小
swapcase（） 小转大 大转小
capitalize()把第一个字符转化为大写 其他小写
title（） 单词的第一个字符转大写  每个单词 剩余字符 转化为小写
'''


