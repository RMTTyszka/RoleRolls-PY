#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import skills as C

class Skills(object):
    ''' Base Atributes for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the skills.
            "alchemy": alchemy,
            "anatomy": anatomy,
            "animaltaming": animaltaming,
            "archery": archery,
            "armorcrafting": armorcrafting,
            "armslore": armslore,
            "awareness": awareness,
            "bowcrafting": bowcrafting,
            "carpentery": carpentery,
            "fencing": fencing,
            "gathering": gathering,
            "healing": healing,
            "heavyweaponship": heavyweaponship,
            "jewelcrafting": jewelcrafting,
            "leatherworking": leatherworking,
            "lore": lore,
            "lumberjacking": lumberjacking,
            "magery": magery,
            "meditating": meditating,
            "mercantilism": mercantilism,
            "military": military,
            "parry": parry,
            "reflex": reflex,
            "resistspells": resistspells,
            "skinning": skinning,
            "stealth": stealth,
            "swordmanship": swordmanship,
            "tactics": tactics,
            "tailoring": tailoring,
            "wrestling": wrestling
        '''
        for skill in C.skills_list:
            if skill in kwargs:
                setattr(self, skill, kwargs[skill])
            else:
                setattr(self, skill, 0)
            # prop = property(lambda x: getattr(self, skill))
            # setattr(self, skill+'_mod', prop)


        # fazer properties

if __name__ == '__main__':
    Skill1 = Skills()
    assert type(Skill1.meditating) is int
