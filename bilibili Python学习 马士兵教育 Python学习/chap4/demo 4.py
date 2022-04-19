# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/2 19:47
'''
会员 >=200 八折
    >=100 九折
    非会员
    >=200 9.5折
    其余不打折


'''
answer=input('are you member? y/n ')
money=int(input('please input your spend'))
if answer=='y': # member
    print('you are the member')
    if money>=200:
        print('the money is:',money*0.8)
    elif money>=100:
        print('money is:',money*0.9)
    else:
        print('money is:',money)

else :
    print('sorry you aren\' the member,')
    if money >=200:
        print('money is:',money*0.95)
    else:print('money is:',money)

