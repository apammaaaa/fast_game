import pygame
from collections import defaultdict

class GameObject:

    def __init__(self, position):
        self.type = 'game_object'
        self.rect = pygame.Rect(*position, 0, 0)
        self.object_dict = defaultdict()
        self.count = 0

    def create_rect(self, object_name: str, img_path: str, size: tuple[int, int] = None,
                    position: tuple[int, int] = (0, 0)):

        self.object_dict[object_name] = Rect(img_path, size, position)

    def crreate_font(self, object_name: str, text: str, font_size: int = 50,
                     color: tuple[int, int, int] = (0, 0, 0), position: tuple[int, int] = (0, 0)):
        self.object_dict[object_name] = Font(text, font_size, color, position)

    def delete_object(self, object_name: str):
        self.object_dict.pop(object_name)

    def values(self):
        return self.object_dict.values()

    def __getitem__(self, object_name):
        return self.object_dict[object_name]


class Rect:

    def __init__(self, img_path: str, size: tuple[int, int], position_for_obj: tuple[int, int]):
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


class Font:

    def __init__(self, text: str, font_size: int, color: tuple[int, int, int], position_for_obj: tuple[int, int]):
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
        print(self.text)
        self.text = f.render(self.text, True, self.color)
        self.rect = self.text.get_rect()
