# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/3/27 18:15
import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
    #初始化pygame 设置和屏幕对象
    pygame.init()
    ai_settings=Settings()
    scree = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height,))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship =Ship(ai_settings,screen)




    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,scree,ship)


        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()