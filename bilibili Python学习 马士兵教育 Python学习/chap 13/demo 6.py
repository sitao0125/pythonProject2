# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/2/10 19:32
# 面向对象 的三大特征  封装 继承 多态  与 语言本身没有关系
class Car:  # 封装
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')


car=Car('宝马x5')
car.start()
print(car.brand)



