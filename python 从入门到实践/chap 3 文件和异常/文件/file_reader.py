# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/11 14:59
filename = '../text_files/pi_digits'  #使用文件的一种常用做法

with open(filename) as file_object:
    for line in file_object:
        print(line)
