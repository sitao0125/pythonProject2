# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/15 9:31
filename= '../text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines= file_object.readlines()

pi_string=''
for line in lines:
    pi_string +=line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))
