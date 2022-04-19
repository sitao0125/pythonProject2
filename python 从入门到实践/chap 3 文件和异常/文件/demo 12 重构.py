# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/27 13:36
# 将代码分为一系列完成具体工作的函数。这样的过程称为重构
'''import json
def greet_user():
    '''问候用户并且指出名字'''
    filename='username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
except FileNotFoundError:
    username =input("what is your name?")
    with open(filenmae,'w') as f_obj:
        json.dump(username,f_obj)
        print("we'll remember you when you come back, "+ username + "!")
else:
print("welcome back,"+ username + "!")

greet_user()'''      #greet_user 函数


import json

def get_stored_username():
    '''如果存储了用户名，就获取他'''
    filename ='username.json'
    try:
        with open(filename) as f_boj:
            username = json.load(f_boj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    '''问候用户并且指出名字'''
    username = get_stored_username()
    if username:
        print("welcome back,"+ username + "!")
    else:
        username =input("what is your name?")
        filename='username.json'

        with open(filenmae,'w') as f_obj:
            json.dump(username,f_obj)
            print("we'll remember you when you come back, "+ username + "!")

greet_user()




