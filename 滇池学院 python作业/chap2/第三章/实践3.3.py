# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 16:47
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                print(i*100+j*10+k,end=' ')