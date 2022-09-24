import pygame
from collections import defaultdict
from gameobj import *

class Scene:

    def __init__(self, scene_name: str, size: tuple[int, int], bg: tuple[int, int, int] = (255, 255, 255)):
        self.bg = bg
        self.name = scene_name
        self.screen = pygame.display.set_mode(size)
        self.screen_rect = self.screen.get_rect()
        self.game_object_dict = defaultdict()

    def create_game_object(self, object_name, position: tuple[int, int] = (0, 0)):
        game_object = GameObject(position)
        self.game_object_dict[object_name] = game_object

    def fill(self):
        self.screen.fill(self.bg)
        for object_name, game_object in self.game_object_dict.items():
            self.load_game_object(game_object)

    def load_game_object(self, game_object):
        for gobj in game_object.values():

            gobj.rect.x = game_object.rect.x + gobj.position_for_obj[0]
            gobj.rect.y = game_object.rect.y + gobj.position_for_obj[1]
            if gobj.type == 'rect':
                self.screen.blit(gobj.image, gobj.rect)
            elif gobj.type == 'font':
                self.screen.blit(gobj.text, gobj.rect)

    def __getitem__(self, game_object_name) -> GameObject:
        return self.game_object_dict[game_object_name]

