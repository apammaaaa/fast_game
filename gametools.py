from g_functions import *

class GameFun:

    def __init__(self):
        pass

    def addAnimationController(self) -> AnimationController:
        print('添加动画控制器')
        self.animation_controller = AnimationController(self, self.action_controller, self.event_controller, self.update_controller)

    def addActionController(self) -> ActionController:
        print('添加动作控制器')
        self.action_controller = ActionController(self.event_controller, self.update_controller)

    def addCharacterController(self) -> CharacterController:
        self.character_controller = CharacterController(self, self.action_controller, self.event_controller, self.update_controller)

