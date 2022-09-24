import sys
import pygame
from collections import defaultdict
from gamescene import Scene
import pickle



class Game:

    def __init__(self, title: str, size: tuple[int, int], icon_path: str = None):
        """
        初始化
        :param size: 窗口大小
        :param title: 窗口标题
        :param icon_path: 窗口图标路径
        """
        pygame.init()
        self.size = size
        self.main_scene = Scene('default_scene', size, (255, 255, 255))
        self.scene_dict = defaultdict()
        pygame.display.set_caption(title)
        if icon_path:
            img = pygame.image.load(icon_path)
            pygame.display.set_icon(img)

    def create_scene(self, scene_name, bg_color: tuple[int, int, int] = (255, 255, 255)):
        self.scene_dict[scene_name] = Scene(scene_name, self.size, bg_color)

    def load_scene(self, scene_name):
        self.main_scene = self.scene_dict[scene_name]

    def run(self):
        while True:
            self.main_scene.fill()
            pygame.display.update()

    def __getitem__(self, key) -> Scene:
        return self.scene_dict[key]

    def save_scene(self, scene_name):
        with open('scene/game_object_name', 'wb') as fp:
            pickle.dump(self.scene_dict[scene_name], fp)


