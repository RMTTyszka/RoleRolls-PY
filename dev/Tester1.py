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
attackers_list = ['heavy_weapon', 'medium_weapon', 'light_weapon']
defenders = []
attackers = []
class Tester(Ch.Char):
    '''
    A class used for testing vars for combat
    balancing every kind of armor and weapon
    '''
    def __init__(self,**kwargs):
        super(Tester,self).__init__(**kwargs)
        damage_done = []
        damage_taken = []
        self.equip(self.equipment.armor,slot='armor')
        for attr in  At.attributes_list:
            setattr(self.attributes,'_'+attr,self.lvl*5)
        for skill in Sk.skills_list:
            setattr(self.skills,'_'+skill,self.lvl*5)
        for bon_type in self.bonuses.keys():
            for bon_name, bon in self.bonuses[bon_type].items():
                self.bonuses[bon_type][bon_name] = bon*self.lvl
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
            char = Tester(name=defender,lvl=x+1, attributes=attributes, skills=skills,
                        defenses=defenses, resists=resists, equipment=equipment)
            defenders.append(char)
        for attacker,wep_cat in zip(attackers_list,arg_list):
            weapon = I.Equipable.Weapon(base=random.choice(II.weapons['cutting'][wep_cat].keys()))
            char = Tester(name=attacker,lvl=x+1, attributes=attributes, skills=skills,
                        defenses=defenses, resists=resists, equipment=equipment)
            attackers.append(char)
        for z in range(3):
            for y in range(3):
                dam = attackers[z].main_attack(defenders[y])
                attackers[z].damage_done.append(dam)
                defenders[y].damage_taken.append(dam)

    #for d in defenders:
        #print d.name
