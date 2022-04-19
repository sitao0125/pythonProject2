# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/18 11:31
filename = '../text_files/pi_million_digits.txt'

with open (filename) as file_object:
    lines= file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string+= line.rstrip()

    birthday =input("enter your birthday, in the form mmddyy:")
    if birthday in pi_string:
        print("your birthday appears in the first million digits of pil")
    else:
        print("your birthday does not appear in the first million digits of pi")
