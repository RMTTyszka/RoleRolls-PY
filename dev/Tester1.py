#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

import auxiliary
import char as Ch
import items as I
from constants import items as II
from constants import attributes as At
from constants import skills as Sk
import random
arg_list = ['heavy','medium','light']
defenders_list = ['heavy_armor', 'medium_armor','light_armor']
attackers_list = ['heavy_weapon', 'medium_weapon', 'light_weapon', 'two_medium_weapon', 'two_light_weapon']
defenders = []
attackers = []
class Tester(Ch.Char):
    def __init__(self,name, **kwargs):
        super(Tester,self).__init__(name,**kwargs)
        damage_done = []
        damage_taken = []
        for attr in  At.attributes_list:
            attr

    def update_lvl():
        pass
tst = 'rush'
if tst == 'combat':
    pass
else:
    attributes = auxiliary.Attributes()
    skills = auxiliary.Skills()
    defenses = auxiliary.Defenses()
    resists = auxiliary.Resists()
    equipment = auxiliary.Equipment()
    for x in range(20):
        for defender,armor_cat in zip(defenders_list,arg_list):
            armor = I.Equipable.Armor(base=random.choice(II.armors_dict[armor_cat].keys()))
            char = Tester(defender,lvl=1, attributes=attributes, skills=skills, defenses=defenses, resists=resists, equipment=equipment)
            defenders.append(char)
        print x
