from gametools import GameFun
import pygame

class Rect:

    def __init__(self, img_path: str, size: tuple[int, int], position_for_obj: tuple[int, int], event_controller, update_controller):
        """
        方块对象
        :param img_path: 图片路径
        """
        self.type = 'rect'
        self.img_path = img_path
        self.size = size
        self.position_for_obj = position_for_obj
        self.image = pygame.image.load(self.img_path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller


class Font:

    def __init__(self, text: str, font_size: int,  color: tuple[int, int, int], position_for_obj: tuple[int, int], event_controller, update_controller):
        """
        文本对象
        :param text: 文本内容
        :param color: 文本颜色
        :param font_size: 文字大小
        """
        self.type = 'font'
        self.font_size = font_size
        self.text = text
        self.color = color
        self.position_for_obj = position_for_obj
        f = pygame.font.Font('C:/Windows/Fonts/RAVIE.TTF', self.font_size)
        self.text = f.render(self.text, True, self.color)
        self.rect = self.text.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller

class Button:

    def __init__(self, text: str, font_size: int, color: tuple[int, int, int], position_for_obj: tuple[int, int], bg_color: tuple[int, int, int], event_controller, update_controller):
        """
        文本对象
        :param text: 文本内容
        :param color: 文本颜色
        :param font_size: 文字大小
        """
        self.type = 'button'
        self.font_size = font_size
        self.text = text
        self.color = color
        self.position_for_obj = position_for_obj
        self.bg_color = bg_color
        f = pygame.font.Font('C:/Windows/Fonts/RAVIE.TTF', self.font_size)
        self.text = f.render(self.text, True, self.color, self.bg_color)
        self.rect = self.text.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller