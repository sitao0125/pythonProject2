# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/18 11:42
filename= '../text_files/learning_python.txt'

with open(filename) as file_object:
    lines=file_object.readlines()
    line1=''
    for line in lines:
        line1+=line.rstrip()
    print(line1)
