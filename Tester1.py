#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

import random
import dev
it = dev.constants.items
at = dev.constants.attributes
sk = dev.constants.skills

arg_list = ['heavy','medium','light']
defenders_list = ['heavy_armor', 'medium_armor','light_armor']
attackers_list = ['heavy_weapon', 'medium_weapon', 'light_weapon']
defenders = []
attackers = []
class Tester(dev.Char):
    '''
    A class used for testing vars for combat
    balancing every kind of armor and weapon
    '''
    def __init__(self,**kwargs):
        super(Tester,self).__init__(**kwargs)
        damage_done = []
        damage_taken = []
        self.equip(self.equipment.armor,slot='armor')
        for attr in  at.attributes_list:
            setattr(self.attributes,'_'+attr,self.lvl*5)
        for skill in sk.skills_list:
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

    attributes = dev.Attributes()
    skills = dev.Skills()
    defenses = dev.Defenses()
    resists = dev.Resists()
    equipment = dev.Equipment()
    for x in range(20):
        for defender,armor_cat in zip(defenders_list,arg_list):
            armor = dev.Equipable.Armor(base=random.choice(it.armors_dict[armor_cat].keys()))
            char = Tester(name=defender,lvl=x+1, attributes=attributes, skills=skills,
                        defenses=defenses, resists=resists, equipment=equipment)
            defenders.append(char)
        for attacker,wep_cat in zip(attackers_list,arg_list):
            weapon = dev.Equipable.Weapon(base=random.choice(it.weapons['cutting'][wep_cat].keys()))
            char = Tester(name=attacker,lvl=x+1, attributes=attributes, skills=skills,
                        defenses=defenses, resists=resists, equipment=equipment)
            attackers.append(char)
        # for z in range(3):
        #     for y in range(3):
        #         attacker[x]
    #for d in defenders:
        #print d.name
