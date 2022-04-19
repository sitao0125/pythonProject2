# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/15 8:51
filename= '../text_files/pi_digits'

with open(filename) as file_object:
    lines=file_object.readlines()


for line in lines:
    print(line.rstrip())

pi_string=''      #创建一个空白的字符串
for line in lines:
    pi_string+=line.strip()  # strip 用于消除左边的空格  rstrip 用于消除右边的空格

print(pi_string)
print(len(pi_string))
# 在读取文本文件 python 将 其中所有的文本都解读为字符串  若读取的是数字 并且要当作数值使用 必须使用 函数int()将其换成整数


