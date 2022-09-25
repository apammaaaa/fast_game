import pygame
from collections import defaultdict
from gameobj import GameObject
from gameeventloop import EventController, UpdateController


class Scene:

    def __init__(self, scene_name: str, size: tuple[int, int], bg_color):
        self.bg = bg_color
        self.name = scene_name
        self.screen = pygame.display.set_mode(size)
        self.screen_rect = self.screen.get_rect()
        self.game_object_dict = defaultdict()

        self.event_controller = EventController()
        self.update_controller = UpdateController()

    def create_game_object(self, object_name, position: tuple[int, int] = (0, 0)):
        game_object = GameObject(position, self.event_controller, self.update_controller)
        self.game_object_dict[object_name] = game_object

    def fill(self):
        for event in pygame.event.get():
            self.event_controller.listen(event)
        self.screen.fill(self.bg)

        self.update_controller.update()
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
            elif gobj.type == 'button':
                self.screen.blit(gobj.text, gobj.rect)

    def __getitem__(self, game_object_name) -> GameObject:
        return self.game_object_dict[game_object_name]

    def bind(self, event_type, func, hot_key=None, meta={}):
        self.event_controller.bind(event_type, func, hot_key, meta)
