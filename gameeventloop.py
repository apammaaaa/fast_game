import pygame
import sys
from collections import defaultdict


def hotkey_bind(e, event, func):
    # print(e['hot_key'])
    if e['hot_key']:
        if e['hot_key'] == 'a':
            if event.key == pygame.K_a:
                func(e['meta'])
        elif e['hot_key'] == 'b':
            if event.key == pygame.K_b:
                func(e['meta'])
        elif e['hot_key'] == 'c':
            if event.key == pygame.K_c:
                func(e['meta'])
        elif e['hot_key'] == 'd':
            if event.key == pygame.K_d:
                func(e['meta'])
        elif e['hot_key'] == 'e':
            if event.key == pygame.K_e:
                func(e['meta'])
        elif e['hot_key'] == 'f':
            if event.key == pygame.K_f:
                func(e['meta'])


class EventController:

    def __init__(self):
        self.event_ls = []

    def listen(self, event):
        # print(self.event_ls)
        if event.type == pygame.QUIT:
            sys.exit()
        for e in self.event_ls:
            event_type, func, hot_key = e['event_type'], e['func'], e['hot_key']
            if event_type == 'KEYDOWN':
                if event.type == pygame.KEYDOWN:
                    hotkey_bind(e, event, func)
            elif event_type == 'KEYUP':
                if event.type == pygame.KEYUP:
                    hotkey_bind(e, event, func)

            elif event_type == 'MOUSEBUTTONDOWN':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if e['meta'].get('gobj', None):
                        if e['meta']['gobj'].type == 'button':
                            if e['meta']['gobj'].rect.collidepoint(event.pos):
                                func(e['meta'])
                    else:
                        func(e['meta'])
            elif event_type == 'MOUSEMOTION':

                if event.type == pygame.MOUSEMOTION:
                    if e['meta'].get('gobj', None):
                        if e['meta']['gobj'].type == 'button':
                            if e['meta']['gobj'].rect.collidepoint(event.pos):
                                e['meta'].update({'is_hover': 1})
                            else:
                                e['meta'].update({'is_hover': 0})
                            func(e['meta'])

    def bind(self, event_type, func, hot_key, meta):
        self.event_ls.append({'event_type':event_type, 'func': func, 'hot_key': hot_key, 'meta': meta})


def update_anime(gobj, anime_name):
    anime_img_ls = gobj.anime_dict[anime_name]['anime_img_ls']
    gobj.image = pygame.image.load(anime_img_ls[gobj.anime_dict[anime_name]['anime_number']])

    if gobj.anime_dict[anime_name]['anime_number'] < gobj.anime_dict[anime_name]['anime_length'] - 1:

        gobj.anime_dict[anime_name]['anime_number'] += 1
    else:
        gobj.anime_dict[anime_name]['anime_number'] = 0


class UpdateController:

    def __init__(self):
        self.anime_ls = []
        self.character_ls = []

    def update(self):
        for c in self.character_ls:
            func = c['func']
            action_name = c['action_name']
            action_value = c['action_value']
            gobj = c['gobj']
            if gobj.action_controller[action_name]['action_value'] == action_value:
                func(c)
        for u in self.anime_ls:
            gobj = u['self']
            anime_name = u['anime_name']
            action_switch_kvls = gobj.anime_dict[anime_name]['action_switch_kvls']
            switch_type = u['switch_type']
            switch_ls = []
            for action_kv in action_switch_kvls:
                action_name = action_kv[0]
                action_value = action_kv[1]
                if gobj.action_controller[action_name]['action_value'] == action_value and gobj.anime_dict[anime_name]['is_active']:
                    switch_ls.append(True)
                else:
                    switch_ls.append(False)
            if switch_type == "&&":
                if False not in switch_ls:
                    update_anime(gobj, anime_name)
            elif switch_type == "||":
                if True in switch_ls:
                    update_anime(gobj, anime_name)



    def bind_u(self, update_type, **meta):
        if update_type == 'anime_play':
            item = {
                'self': meta['obj'],
                'anime_name_path': meta['anime_name_path'],
                'anime_number_range' : meta['anime_number_range'],
                'action_switch_kvls': meta['action_switch_kvls'],
                'switch_type': meta['switch_type'],
                'anime_name': meta['anime_name'],
                'type': 'anime_play',
            }
            self.anime_ls.append(item)
        elif update_type == 'character_event':
            item = {
                'func': meta['func'],
                'action_name': meta['action_name'],
                'action_value': meta['action_value'],
                'gobj': meta['gobj']
            }
            self.character_ls.append(item)