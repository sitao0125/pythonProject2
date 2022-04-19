# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/4 9:05
# break continue use in two 8
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()