# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/26 22:33
import json

filename = 'username.json'
with open(filename) as f_obj:
    username=json.load(f_obj)
    print("welcome back,"+ username +"!")
