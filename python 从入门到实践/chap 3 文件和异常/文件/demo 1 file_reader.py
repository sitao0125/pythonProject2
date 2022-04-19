# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/11 14:19
with open('../text_files/pi_digits') as file_object:  #open 为打开函数  with 在不需要访问文件时将他关闭 object可以视作一个新的名称
    contents=file_object.read()
    print(contents.rstrip())  #经过检验read 确实返回了一个空行
    print('hello world')

with open('../text_files/filename', encoding=conding='utf-8') as file_objecti:
    contenti=file_objecti.read()
    print(contenti)


'''with open('E:\\pythonProject2\\python 从入门到实践\\chap 3 文件和异常\\text_files.txt',encoding=conding='utf-8') as file_objecti:
    contenti=file_objecti.read()
    print(contenti)'''

'''f = open('E:\\pythonProject2\\python 从入门到实践\\chap 3 文件和异常\\text_files.txt',encoding=conding='utf-8')
ls = f.readline()
print(ls)'''


