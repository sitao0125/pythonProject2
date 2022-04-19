# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/26 22:47
import json
filename='username.json'
try:
    with open(filename) as f_obj:  #尝试打开文件 username,json
        username =json.load(f_obj)  #若存在 则 将内容读取到用户名
except FileNotFoundError:
    username =input("what is your name ?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("we'll remember you when you come back ,"+ username+ "!")
else:
    print("welcome back" +username+"!")
