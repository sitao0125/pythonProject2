# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/26 22:13
import json

username=input("what is your name")
filename='username.json'

with open(filename,'w') as f_boj:
    json.dump(username,f_boj)
    print("we'll remember you when you come back,"+ username +"!")



