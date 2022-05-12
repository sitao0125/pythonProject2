# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 21:34
def numb():
    num = input('输入一个不超过5位的正整数:')
    l = len(num)    #长度,就是几位数
    print('这个数是',l ,'位数')
    n = num[::-1]   #通过索引切片,逆序打印出数字
    for i in n:
        print(i)

numb()