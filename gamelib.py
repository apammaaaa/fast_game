import sys

from gamescene import *


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
        self.main_scene = Scene('default_scene', size)
        self.scene_dict = defaultdict()
        pygame.display.set_caption(title)
        if icon_path:
            img = pygame.image.load(icon_path)
            pygame.display.set_icon(img)

    def create_scene(self, scene_name):
        self.scene_dict[scene_name] = Scene(scene_name, self.size)

    def load_scene(self, scene_name):
        self.main_scene = self.scene_dict[scene_name]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.main_scene.fill()
            pygame.display.update()

    def __getitem__(self, key) -> Scene:
        return self.scene_dict[key]


