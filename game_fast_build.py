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

def move_r(meta):
    g_obj = meta['gobj']
    g_obj.rect.x += 3

def move_l(meta):
    g_obj = meta['gobj']
    g_obj.rect.x += -3

def move_t(meta):
    g_obj = meta['gobj']
    g_obj.rect.y += -3

def move_d(meta):
    g_obj = meta['gobj']
    g_obj.rect.y += 3

def addMove(g_obj, obj_name):
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

    g_obj.animation_controller.create_animation('male', 'male_move_right', [('walk_r', 1), ('walk_l', 0), ('walk_d', 0), ('walk_t', 0)], 'walk/BODY_male', (28, 36))
    g_obj.animation_controller.play_anime(obj_name, 'male_move_right')
    g_obj.animation_controller.create_animation('male', 'male_move_left', [('walk_l', 1), ('walk_r', 0), ('walk_d', 0), ('walk_t', 0)], 'walk/BODY_male', (10, 18))
    g_obj.animation_controller.play_anime(obj_name, 'male_move_left')
    g_obj.animation_controller.create_animation('male', 'male_move_top', [('walk_t', 1), ('walk_l', 0), ('walk_r', 0), ('walk_d', 0)], 'walk/BODY_male', (1, 9))
    g_obj.animation_controller.play_anime(obj_name, 'male_move_top')
    g_obj.animation_controller.create_animation('male', 'male_move_down', [('walk_d', 1), ('walk_l', 0), ('walk_r', 0), ('walk_t', 0)], 'walk/BODY_male', (20, 27))
    g_obj.animation_controller.play_anime(obj_name, 'male_move_down')