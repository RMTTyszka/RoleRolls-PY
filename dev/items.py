#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import auxiliary
from constants import items as Ci
from constants import equipment as Ce
class Item(object):
    ''' Base class for any item in the game '''

    def __init__(self, lvl, base, name, material, power, effect):
        #super(Item, self).__init__(name, **kwargs)
        self.base = base
        self.name = name
        self.lvl = lvl
        self.condition = Ci.item_condition[self.lvl-1]
        self.value = Ci.item_value[self.lvl-1]

    @classmethod
    def blank(cls,*args, **kwargs):
        '''
        Creates a blank char with 0 in all stats
        '''
        blank = {
            'lvl': 0,
            'effects': {},
            'powers': {},
            'spells': {},
            'bonuses': {},
                }
        for key, value in kwargs.items():
            if key in blank:
                blank[key] = value
        return cls(*args, **blank)

class Equipable(Item):
    ''' Base class for any equipable in the game '''

    def __init__(self, slot, lvl, base,name, material, power, effect, bonuses):
        super(Equipable, self).__init__(lvl, base, name, material, power, effect)

        self.slot = slot
        self.bonuses = bonuses if bonuses != None else {'magic':{},'innate':{},'moral':{}}

        def Equip(self):
            pass
        def _update_bonus(self,newlvl):
            pass

    @classmethod
    def Armor(cls, lvl, base, name, category, material, power, effect, bonuses):
        '''
        Create an item that can be equipped
        and implement armor attributes:
        - pass bonuses to equipable class
        - category
        - strong
        - weak
        - protection and evasion
        '''

        armor = cls(['armor'], lvl, base ,name, material, power, effect, bonuses)
        if category == None:
            armor.category = [cat for cat, base
                              in Ci.armors_dict.items()
                              if armor.base
                              in base.keys()][0]
        else:
            armor.category = category

        for arg in Ci.armor_args:
            setattr(armor,arg,Ci.armors_dict[armor.category][armor.base][arg])
        #get protection and evasion
        armor.protection = armor.bonuses['innate'].get('protection',0) \
                                + Ci.armor_info[armor.category]['protection'] \
                                * armor.lvl
        armor.evasion = armor.bonuses['innate'].get('evasion',0) \
                                 + Ci.armor_info[armor.category]['evasion']
        return armor
    @classmethod
    def Weapon(cls, base, name=None, category=None, size=None, bonuses=None, lvl=1 ):
        '''
        Create an item, that can be equipped
        and implement weapon attributes:
        - category
        - size
        - AS_base // min_damage // max_damage // attk_bonus // mult_damage //
          mult_attr // counter // armor_penetration
        '''
        #create basic weapon
        weapon = cls(['mainhand','offhand'], base, name, lvl, bonuses=bonuses)
        #get category
        if category == None:
            weapon.category = [cat for cat
                               in Ci.weapons.keys()
                               if True in [weapon.size.has_key(weapon.base) for weapon.size
                                            in Ci.weapons[cat].values() ]][0]
        else:
            weapon.category = category
        #get size
        if size == None:
            weapon.size = [size for size
                    in Ci.weapons[weapon.category].keys()
                    if Ci.weapons[weapon.category][size].has_key(weapon.base)][0]
        else:
            weapon.size = size
        print weapon.base, weapon.name,weapon.category,weapon.size
        #get attributes and skills used for attack and damage and base status
        for arg in Ci.get_weapon_attr:
            setattr(weapon,arg,Ci.weapon_type[weapon.category][arg])
        for arg in Ci.wep_size_info[weapon.size]:
            fix = weapon.lvl if arg == 'armor_penetration' else 1
            setattr(weapon,arg,Ci.wep_size_info[weapon.size][arg]*fix)

        return weapon

    @classmethod
    def Ring(cls, base, **kwargs):
        return 0
if __name__ == '__main__':
    #item1 = Item(base = 'candle')
    #print item1.condition
    #print item1.value
    #print isinstance(item1, Item)
    #print isinstance(item1, Equipable)
    item2 = Equipable.Armor(base = 'splintmail',lvl=12)
    print isinstance(item2, Equipable)
    print item2.category
    print item2.strong
    print item2.weak
    print item2.bonuses
    #print item2.slots
    print
    print
    print
    item3 = Equipable.Weapon(base='longsword',name='fire')
    print item3.name + ' ' + item3.base
    for var in vars(item3):
        print var, getattr(item3,var)
    item4 = Equipable.Armor(base='fullplate',name ='gosma',lvl=5)
    print item4.bonuses
