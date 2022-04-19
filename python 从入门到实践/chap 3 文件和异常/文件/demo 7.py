# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/26 21:32
import json
filename='numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

    print(numbers)