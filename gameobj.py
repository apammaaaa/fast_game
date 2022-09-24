import pygame
from collections import defaultdict
from g_obj import *

class GameObject:

    def __init__(self, position, event_controller):
        self.type = 'game_object'
        self.rect = pygame.Rect(*position, 0, 0)
        self.object_dict = defaultdict()
        self.count = 0

        self.event_controller = event_controller

    def create_rect(self, object_name: str, img_path: str, size: tuple[int, int] = None,
                    position: tuple[int, int] = (0, 0)):

        self.object_dict[object_name] = Rect(img_path, size, position, self.event_controller)

    def crreate_font(self, object_name: str, text: str, font_size: int = 50,
                     color: tuple[int, int, int] = (0, 0, 0), position: tuple[int, int] = (0, 0)):
        self.object_dict[object_name] = Font(text, font_size, color, position, self.event_controller)

    def crreate_button(self, object_name: str, text: str, font_size: int = 50,
                     color: tuple[int, int, int] = (255, 255, 255), position: tuple[int, int] = (0, 0), bg_color: tuple[int, int, int] = (0, 0, 0)):
        self.object_dict[object_name] = Button(text, font_size, color, position, bg_color, self.event_controller)

    def delete_object(self, object_name: str):
        self.object_dict.pop(object_name)

    def values(self):
        return self.object_dict.values()

    def __getitem__(self, object_name) -> Rect:
        return self.object_dict[object_name]


