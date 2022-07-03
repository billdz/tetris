#: 颜色定义
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 97, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_CYAN = (0, 255, 255)
COLOR_PURPLE = (160, 32, 240)

COLORS = [color for name, color in globals().items() 
                if not name.startswith('__') 
                and color not in (COLOR_BLACK, COLOR_WHITE)
            ]


if __name__ == "__main__":
    print(COLORS)