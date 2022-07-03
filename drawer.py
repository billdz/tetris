
from tkinter import N
from tkinter.messagebox import NO
import pygame


class Block:
    """小块"""
    width = 24
    height = 24

    @staticmethod
    def draw(s, left, top, color, bg_color, width=None, height=None):
        if width is None:
            width = Block.width
        if height is None:
            height = Block.height
        pygame.draw.rect(s, bg_color,
                         pygame.Rect(left, top, width, height)
            )
        pygame.draw.rect(s, color, 
                        pygame.Rect(left, top, 
                            width - 1,
                            height - 1)
            )

class PanelDrawer:
    @staticmethod
    def draw(s, x, y, width, height, color, bg_color):
        pygame.draw.rect(s, bg_color,
                         pygame.Rect(x, y, width, height)
            )
        pygame.draw.rect(s, color, 
                        pygame.Rect(x, y, 
                            width - 1,
                            height - 1)
            )