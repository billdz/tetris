import pygame
from drawer import Block


class Text:
    def __init__(self, text: str, text_color, font_size: int):
        """
        text: 文本内容,如'大学生模拟器',注意是字符串形式
        text_color: 字体颜色, 使用RGB
        font_size: 字体大小,如20、10
        """
        self.text = text
        self.text_color = text_color
        self.font_size = font_size

        font = pygame.font.Font(None, self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()

        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()
    
    def get_size(self):
        return (self.text_width, self.text_height)
    
    def set_text(self, text):
        self.text = text
        font = pygame.font.Font(None, self.font_size)
        self.text_image = font.render(self.text, True, self.text_color).convert_alpha()
        self.text_width = self.text_image.get_width()
        self.text_height = self.text_image.get_height()

    def draw(self, surface: pygame.Surface, center_x, center_y, bg_color=(0, 255, 255)):
        """
        surface: 文本放置的表面
        center_x, center_y: 文本放置在表面的<中心坐标>
        bg_color: RGB值, 表示文本框的底色
        """
        upperleft_x = center_x - self.text_width / 2
        upperleft_y = center_y - self.text_height / 2
        Block.draw(surface, upperleft_x-1, upperleft_y-1, bg_color, (0, 0, 0), 
            self.text_width+2, self.text_height+2)
        surface.blit(self.text_image, (upperleft_x, upperleft_y))

class ButtonText(Text):
    def __init__(self, text: str, text_color, font_size: int):
        super().__init__(text, text_color, font_size)
        self.rect = self.text_image.get_rect()

    def draw(self, surface: pygame.Surface, center_x, center_y):
        super().draw(surface, center_x, center_y)
        self.rect.center = center_x, center_y

    def handle_event(self, command):
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.hovered:
            command()