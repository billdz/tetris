from elements import ButtonText, Text
from color import *
from drawer import PanelDrawer


class Panel:
    """面板, 用于控制游戏以及显示分数"""
    def __init__(self, x, y=0, width=240, height=528):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.start_btn = ButtonText('Start', COLOR_ORANGE, 40)
        self.score_text = Text('000', COLOR_BLUE, 40)
        self.pause_btn = ButtonText('Pause', COLOR_RED, 40)

    def set_start_handler(self, command):
        self.start_btn.handle_event(command)
    
    def set_pause_handler(self, command):
        self.pause_btn.handle_event(command)

    def draw(self, s):
        PanelDrawer.draw(s, self.x, self.y, self.width, self.height, COLOR_WHITE, COLOR_BLACK)
        center_x = self.x+self.width//2
        self.score_text.draw(s, center_x, self.y+(self.height//6)*1)
        self.start_btn.draw(s, center_x, self.y+(self.height//6)*3)
        self.pause_btn.draw(s, center_x, self.y+(self.height//6)*5)
