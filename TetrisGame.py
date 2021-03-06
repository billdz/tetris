# coding : utf-8

#: pip install pygame
import random
import sys
from turtle import screensize
import pygame
from color import *
from layout import Layout
from panel import Panel


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    #: 初始化
    while True:
        layout = Layout()
        layout.create_new_building()
        panelsize = (100, 528)
        screensize = (layout.size[0]+panelsize[0], 528)
        pygame.init()
        pygame.display.set_caption('俄罗斯方块')
        screen = pygame.display.set_mode(screensize, 0, 32)
        panel = Panel(layout.size[0], 0, *panelsize)
        is_over = False
        #: 单局游戏循环开始 [结束后直接重新开始]
        while not is_over:
            #: 处理游戏消息
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                #: 处理按键
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        layout.convert_building()
                    if e.key == pygame.K_DOWN:
                        layout.direct_down()
                    if e.key == pygame.K_LEFT:
                        layout.move_left_right(-1)
                    if e.key == pygame.K_RIGHT:
                        layout.move_left_right(1)
            #: 是否碰触底部地面了，是 -> 融合背景 否 -> 继续下落
            if layout.test_building_touch_wall(y_offset=1):
                layout.put_building_to_layout()
                is_over = layout.create_new_building()
            else:
                layout.down_build()
            #: 绘制
            layout.draw(screen)
            layout.draw_building(screen)
            score = '{:0>3d}'.format(layout.get_score())
            panel.score_text.set_text(score)
            panel.draw(screen)
            pygame.display.update()
            #: 速度
            pygame.time.Clock().tick(layout.speed)


if __name__ == '__main__':
    main()
