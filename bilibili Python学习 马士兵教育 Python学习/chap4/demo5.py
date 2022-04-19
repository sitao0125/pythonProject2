# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 20:04
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第一个整数'))
if num_a>=num_b:
    print(num_a,'>=',num_b)
else:
    print(num_a,'<=',num_b)
print('使用条件表达式进行表达')

print(num_a, '>=', num_b)if num_a>=num_b else  print(num_a,'<=',num_b)
print(' 字符串链接方式')
print(str(num_a)+'大于等于'+str(num_b))if num_a>=num_b else  print(str(num_a)+'小于等于'+str(num_b))
