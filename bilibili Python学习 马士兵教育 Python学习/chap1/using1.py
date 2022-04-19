# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/1/28 21:00
#可以输出数字
print(520)
print(985)

#可以输出字符串
print('hello world');
#字符串不加引号 会报错
#含有运算符的表达式
print(3+1)
#输出到文件
fp=open('E:/text.txt','a+')
#a+ 如果文件不存在就创建，存在就在文件内容后面继续
print('hello world',file=fp)
fp.close()

不进行换行输出（输出内容在一行中）
printf('hello','world','python')
