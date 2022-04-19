# 2020级人工智能一班
# 陈思韬
# 开发时间: 2022/4/5 8:39
import sys

import pygame

def check_events(ship):
    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type ==pygame.KEYUP:
            if event.key== pygame.K_RIGHT:
                ship.moving_right =False
