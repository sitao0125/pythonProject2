# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 20:19
def fun():
    a=int(input("请输入任意整数："))
    b=int(input("请输入任意整数："))
    c=int(input("请输入任意整数："))
    d=int(input("请输入任意整数："))
    my_list=[a,b,c,d]
    for i in range(0,4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                list_result=[my_list[i],my_list[j],my_list[k]]
                list_result.sort()
                print(list_result)

fun()
