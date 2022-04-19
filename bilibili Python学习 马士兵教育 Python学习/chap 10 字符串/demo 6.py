# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/7 20:38
# 字符串 替换 replace（）  字符串合并 join()
s='hello,python'
print(s.replace('python','java'))

s1='hello,python,python,python'
print(s1.replace('python','java',2))
# 不加数字 默认是全部替换 加了 数字 从右到左 依次替换

# join 列表或元组 的字符串 合并成一个新的字符串
lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))
print('*'.join('python')) # lianjie 字符串

# 字符串的 比较


print('apple'>'app')
print('apple'>'banaan')

print(ord('a'),ord('b'))  # 原始值 ascⅡ 表

print(ord('陈'))
print(chr(38472))

'''==与 is 的区别
==  比较的是value
is  比较的是地址

'''



