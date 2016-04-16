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

    def __init__(self,**kwargs):
        #super(Item, self).__init__(name, **kwargs)
        for arg in Ci.items_args:
            if arg in kwargs:
                setattr(self,arg,kwargs[arg])
            else:
                setattr(self,arg,None)
        self.lvl = kwargs['lvl'] if 'lvl' in kwargs else 1
        self.condition = Ci.item_condition[self.lvl-1]
        self.value = Ci.item_value[self.lvl-1]
        self.color = kwargs['color'] if 'color' in kwargs else Ci.default_color

    @classmethod
    def blank(cls, name, *args, **kwargs):
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
        return cls(name, *args, **blank)

class Equipable(Item):
    ''' Base class for any equipable in the game '''

    def __init__(self, slot, **kwargs):
        super(Equipable, self).__init__(slot = slot, **kwargs)
        self.bonuses = kwargs['bonuses'] if 'bonuses' in kwargs else {'magic':{},'innate':{},'moral':{}}
        def Equip():
            pass


    @classmethod
    def Armor(cls,**kwargs):
        '''
        Create an item that can be equipped
        and implement armor attributes:
        - category
        - strong
        - weak
        - bonuses [protection and evasion]
        '''
        armor = cls(['armor'],**kwargs)
        if 'category' in kwargs:
            armor.category = kwargs['category']
        else:
            armor.category = [cat for cat, base
                              in Ci.armors_dict.items()
                              if armor.base
                              in base.keys()][0]
        if 'strong' in kwargs:
            armor.strong = kwargs['strong']
        else:
            armor.strong = Ci.armors_dict[armor.category][armor.base]['strong']
        if 'weak' in kwargs:
            armor.weak = kwargs['weak']
        else:
            armor.weak = Ci.armors_dict[armor.category][armor.base]['weak']


        armor.bonuses['innate']['protection'] = armor.bonuses['innate'].get('protection',0) \
                                + Ci.armor_info[armor.category]['protection'] \
                                * armor.lvl
        armor.bonuses['innate']['evasion'] = armor.bonuses['innate'].get('evasion',0) \
                                 + Ci.armor_info[armor.category]['evasion']
        return armor
    @classmethod
    def Weapon(cls,**kwargs):
        '''
        Create an item, that can be equipped
        and implement weapon attributes:
        - category
        - size
        - and attributes and skills used for attack
        '''
        weapon = cls(['maindhand','offhand'], **kwargs)

        if 'category' in kwargs:
            weapon.category = kwargs['category']
        else:
            weapon.category = [cat for cat
                               in Ci.weapons.keys()
                               if True in [weapon.size.has_key(weapon.base) for weapon.size
                                            in Ci.weapons[cat].values() ]][0]
        weapon.size = kwargs['size'] if 'size' in kwargs else [size for size
                        in Ci.weapons[weapon.category].keys()
                        if Ci.weapons[weapon.category][size].has_key(weapon.base)][0]
        for arg in Ci.get_weapon_attr:
            setattr(weapon,arg,Ci.weapon_type[weapon.category][arg])
        return weapon

    @classmethod
    def Ring(cls, base, **kwargs):
        return 0
if __name__ == '__main__':
    item1 = Item(base = 'candle')
    print item1.condition
    print item1.value
    print isinstance(item1, Item)
    print isinstance(item1, Equipable)
    item2 = Equipable.Armor(base = 'splintmail',lvl=12)
    print isinstance(item2, Equipable)
    print item2.category
    print item2.strong
    print item2.weak
    print item2.bonuses
    #print item2.slots
    item3 = Equipable.Weapon(base = 'longsword',name = 'fire')
    print item3.name + ' ' + item3.base
