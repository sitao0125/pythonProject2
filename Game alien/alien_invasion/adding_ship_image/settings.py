# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/29 9:00
class Settings():
    '''存储《外星人入侵》的所有设置类'''
    def _init_(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_spreed_factor=1.5