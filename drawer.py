
import pygame


class Block:
    """小块"""
    width = 24
    height = 24

    @staticmethod
    def draw(s, left, top, color, bg_color):
        pygame.draw.rect(s, bg_color,
                         pygame.Rect(left, top, Block.width, Block.height)
            )
        pygame.draw.rect(s, color, 
                        pygame.Rect(left, top, 
                            Block.width - 1,
                            Block.height - 1)
            )