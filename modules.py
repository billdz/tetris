import random
from color import COLORS


class Building:
    """积木"""

    def __init__(self):
        """
        方块的7种基本形状
        每次初始化随机选择一个形状
        @:return True / False
        """
        self.color = random.choice(COLORS)
        self.form = random.choice([
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            [
                [0, 0, 0, 0, 0], 
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0], 
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
                ],
            ])

    def change_to(self, box):
        self.form = box

    def __getitem__(self, pos):
        return self.form[pos]

    def __setitem__(self, key, value):
        self.form[key] = value
    
    def get_color(self):
        return self.color
