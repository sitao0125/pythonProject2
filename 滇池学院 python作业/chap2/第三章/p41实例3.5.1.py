# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/28 15:35
#根据身高体重，输出BMI指标

heigth,weight =eval(input("请输入身高（m）和题中（kg）[逗号分开]："))
bmi=weight/pow(heigth,2)
str=""
if bmi<18.5:
    str="偏瘦，请注意饮食！"
elif 18.5<=bmi<24:
    str="正常，请保持！"
elif 24<=bmi<28:
    str="偏胖，请注意饮食！"
else:
    str="肥胖，请引起重视！"
print("您的体重"+str)