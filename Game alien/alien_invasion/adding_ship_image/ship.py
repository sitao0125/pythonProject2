# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/29 9:39
import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """初始化飞船，并设置其位置"""
        self.screen=screen
        self.ai_settings =ai_settings

        #加载飞船图像并获取其外接矩形
        self.image =pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx =self.screen_rect.centerx
        """rect 对象 属性 center centerx centery"""
        self.rect.bottom =self.screen_ract.bottom

        #在飞船的属性center中存储小数值
        self.center=float(self.rect.centerx)
        #移动标志
        self.moving_right =False
    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值 而不是rect
        if self.moving_right and self.ract.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_spreed_factor
        if self.moving_left and self.rect.left>0:
            self.center -=self.ai_settings.ship_spreed_factor

        #根据self.center更新rect 对象
        self.rect.centerx=self.center



    def blitem(self):
        """ 在指定位置绘制飞船"""
        self.screen.bolit(self.image,self.rect)


