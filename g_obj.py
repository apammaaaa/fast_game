from gametools import GameFun
from gameeventloop import EventController, UpdateController
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

    def __init__(self,
                 text: str,
                 font_size: int,
                 color: tuple[int, int, int],
                 position_for_obj: tuple[int, int],
                 bg_color: tuple[int, int, int],
                 event_controller: EventController,
                 update_controller: UpdateController,
                 hover_color: tuple[int, int, int],
                 hover_bg_color: tuple[int, int, int],
                 font_style: str):
        """
        文本对象
        :param text: 文本内容
        :param color: 文本颜色
        :param font_size: 文字大小
        """
        self.type = 'button'
        self.font_size = font_size
        self.txt = text
        self.color = color
        self.position_for_obj = position_for_obj
        self.bg_color = bg_color
        self.f = pygame.font.Font(font_style, self.font_size)
        self.text = self.f.render(self.txt, True, self.color, self.bg_color)
        self.rect = self.text.get_rect()

        self.event_controller = event_controller
        self.update_controller = update_controller

        self.hover_color = hover_color
        self.hover_bg_color = hover_bg_color

        self.event_controller.bind('MOUSEMOTION', self.mouse_hover, None, {'gobj':self, 'is_hover':0})

    def mouse_hover(self, meta):
        if meta['is_hover'] == 1:
            self.text = self.f.render(self.txt, True, self.hover_color, self.hover_bg_color)
        else:
            self.text = self.f.render(self.txt, True, self.color, self.bg_color)

    def bind(self, func):
        self.event_controller.bind('MOUSEBUTTONDOWN', func, meta={'gobj':self}, hot_key=None)