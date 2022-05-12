# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 16:31
n=input("请输入若干个数字且用逗号隔开：")
nums=n.split(",")
s=0
for i in nums:
    s+=eval(i)
print(s)