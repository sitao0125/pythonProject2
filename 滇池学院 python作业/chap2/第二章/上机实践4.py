# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/15 11:43
import random
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0,9))  		# 0~9之间的数字
        ran2 = chr(random.randint(65,90)) 		# a~z的字母
        ran3 = chr(random.randint(97,122))   	# A~Z的字母

        r = random.choice([ran1,ran2,ran3]) 	#从a~z、A~Z、0-9中选出一个字符
        code += r   							# 循环取出4个
    return code
code = func()
print(code)
