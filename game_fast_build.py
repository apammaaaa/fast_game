from gameobj import GameObject

def walk_r(meta):
    action_controller = meta['self']
    action_controller['walk_r']['action_value'] = meta['action_value']

def walk_l(meta):
    action_controller = meta['self']
    action_controller['walk_l']['action_value'] = meta['action_value']

def walk_t(meta):
    action_controller = meta['self']
    action_controller['walk_t']['action_value'] = meta['action_value']

def walk_d(meta):
    action_controller = meta['self']
    action_controller['walk_d']['action_value'] = meta['action_value']

def obj_move(scene,x=0,y=0):
    for gobj_key in scene.game_object_dict:
        if not hasattr(scene[gobj_key], 'camera'):
            scene[gobj_key].rect.x += x
            scene[gobj_key].rect.y += y
def move_r(meta):
    g_obj = meta['gobj']
    scene = meta['scene']
    if hasattr(g_obj, 'can_move_right'):
        if g_obj.can_move_right:
            if hasattr(g_obj, 'camera'):
                obj_move(scene, x=-3)
            else:
                g_obj.rect.x += 3
    else:
        g_obj.rect.x += 3

def move_l(meta):
    g_obj = meta['gobj']
    scene = meta['scene']
    if hasattr(g_obj, 'can_move_left'):
        if g_obj.can_move_left:
            if hasattr(g_obj, 'camera'):
                obj_move(scene, x=3)
            else:
                g_obj.rect.x += -3
    else:
        g_obj.rect.x += -3

def move_t(meta):
    g_obj = meta['gobj']
    scene = meta['scene']
    if hasattr(g_obj, 'can_move_top'):
        if g_obj.can_move_top:
            if hasattr(g_obj, 'camera'):
                obj_move(scene, y=3)
            else:
                g_obj.rect.y += -3
    else:
        g_obj.rect.y += -3

def move_d(meta):
    g_obj = meta['gobj']
    scene = meta['scene']
    if hasattr(g_obj, 'can_move_bottom'):
        if g_obj.can_move_bottom:
            if hasattr(g_obj, 'camera'):
                obj_move(scene, y=-3)
            else:
                g_obj.rect.y += 3
    else:
        g_obj.rect.y += 3

def addMove(g_obj, obj_name, r, l, t, d):
    g_obj.action_controller.create_action('walk_r', 0,walk_r)
    g_obj.action_controller.bind_action('walk_r', 'KEYDOWN', 'd', 1)
    g_obj.action_controller.bind_action('walk_r', 'KEYUP', 'd', 0)
    g_obj.character_controller.bind_event('walk_r', [('walk_r', 1), ('walk_l', 0), ('walk_d', 0), ('walk_t', 0)], move_r)

    g_obj.action_controller.create_action('walk_l', 0,walk_l)
    g_obj.action_controller.bind_action('walk_l', 'KEYDOWN', 'a', 1)
    g_obj.action_controller.bind_action('walk_l', 'KEYUP', 'a', 0)
    g_obj.character_controller.bind_event('walk_l', [('walk_l', 1), ('walk_r', 0), ('walk_d', 0), ('walk_t', 0)], move_l)

    g_obj.action_controller.create_action('walk_t', 0,walk_t)
    g_obj.action_controller.bind_action('walk_t', 'KEYDOWN', 'w', 1)
    g_obj.action_controller.bind_action('walk_t', 'KEYUP', 'w', 0)
    g_obj.character_controller.bind_event('walk_t', [('walk_t', 1), ('walk_l', 0), ('walk_r', 0), ('walk_d', 0)], move_t)

    g_obj.action_controller.create_action('walk_d', 0,walk_d)
    g_obj.action_controller.bind_action('walk_d', 'KEYDOWN', 's', 1)
    g_obj.action_controller.bind_action('walk_d', 'KEYUP', 's', 0)
    g_obj.character_controller.bind_event('walk_d', [('walk_d', 1), ('walk_l', 0), ('walk_r', 0), ('walk_t', 0)], move_d)


    g_obj.action_controller.create_action('walk_d', 0, walk_d)
    g_obj.action_controller.bind_action('walk_d', 'KEYDOWN', 's', 1)
    g_obj.action_controller.bind_action('walk_d', 'KEYUP', 's', 0)
    g_obj.character_controller.bind_event('walk_d', [('walk_d', 1), ('walk_l', 0), ('walk_r', 0), ('walk_t', 0)],
                                          move_d)
    g_obj.animation_controller.create_animation(obj_name, 'male_move_right',
                                                [('walk_r', 1), ('walk_l', 0), ('walk_d', 0), ('walk_t', 0)], r[0],
                                                r[1])
    g_obj.animation_controller.play_anime(obj_name, 'male_move_right')
    g_obj.animation_controller.create_animation(obj_name, 'male_move_left',
                                                [('walk_l', 1), ('walk_r', 0), ('walk_d', 0), ('walk_t', 0)], l[0],
                                                l[1])
    g_obj.animation_controller.play_anime(obj_name, 'male_move_left')
    g_obj.animation_controller.create_animation(obj_name, 'male_move_top',
                                                [('walk_t', 1), ('walk_l', 0), ('walk_r', 0), ('walk_d', 0)], t[0],
                                                t[1])
    g_obj.animation_controller.play_anime(obj_name, 'male_move_top')
    g_obj.animation_controller.create_animation(obj_name, 'male_move_down',
                                                [('walk_d', 1), ('walk_l', 0), ('walk_r', 0), ('walk_t', 0)], d[0],
                                                d[1])
    g_obj.animation_controller.play_anime(obj_name, 'male_move_down')


def CameraBuild(camera_obj:GameObject):
    if hasattr(camera_obj, 'camera'):
        camera_obj.addActionController()
        camera_obj.addCharacterController()
        camera_obj.action_controller.create_action('walk_r', 0,walk_r)

class Dfunc:

    def __init__(self, camera_obj, original_x, target_x, speed):
        self.scene = camera_obj.scene
        self.original_x = original_x
        self.target_x = target_x
        self.speed = speed
        self.is_invalid = False
        self.is_active = False

    def bind(self, func):
        self.func = func
    def run(self, delay_event):
        self.func(self, self.scene)

    def __str__(self):
        return str(self.speed)
def c_r(dfunc, scene):
    if dfunc.original_x < dfunc.target_x:
        obj_move(scene, x=-1 * dfunc.speed)
    else:
        dfunc.is_active = False
        dfunc.is_invalid = True
    dfunc.original_x += dfunc.speed
def CameraMove(delay_event_name, camera_obj:GameObject, direction, distance, speed):


    if direction == 'right':
        original_x = camera_obj.original_x
        target_x = original_x + distance
        camera_obj.original_x = target_x
        print('初始',original_x, target_x)
        f = Dfunc(camera_obj, original_x, target_x, speed)
        f.bind(c_r)
        delay_ls = camera_obj.delay_dict.get(delay_event_name, [])
        delay_ls.append(f)
        camera_obj.delay_dict[delay_event_name] = delay_ls

def CameraBindMove(camera_obj:GameObject):
    for vls in camera_obj.delay_dict.values():
        camera_obj.update_controller.bind_u('delay_event', func_obj_ls=vls)

