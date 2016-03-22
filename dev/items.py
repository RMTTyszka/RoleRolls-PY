#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import base
import auxiliary
from constants import items as C

class Item(base.Base):
    ''' Base class for any item in the game '''

    def __init__(self, name, **kwargs):
        super(Item, self).__init__(name, **kwargs)
        self.category = C.item_cat[self.lvl]
        self.value = C.item_value[self.lvl]

    @classmethod
    def blank(cls, name, *args, **kwargs):
        '''
        Creates a blank char with 0 in all stats
        '''
        blank = {
            'lvl': 0,
            'attributes': auxiliary.Attributes(),
            'defenses': auxiliary.Defenses(),
            'resists': auxiliary.Resists(),
            'inventory': auxiliary.Inventory(0),
            'effects': {},
            'powers': {},
            'spells': {},
            'bonuses': {},
            'HP': 0,
            'SP': 0,
            'ST': 0}
        for key, value in kwargs.items():
            if key in blank:
                blank[key] = value
        return cls(name, *args, **blank)

class Equipable(Item):
    ''' Base class for any equipable in the game '''

    def __init__(self, name, slots, **kwargs):
        super(Equipable, self).__init__(name, **kwargs)
        self.slots = slots

    @classmethod
    def Armor(cls, name, **kwargs):
        return cls.blank(name, ['armor'], **kwargs)

    @classmethod
    def Weapon(cls, name, **kwargs):
        return cls.blank(name, ['weapon'], **kwargs)

    @classmethod
    def Ring(cls, name, **kwargs):
        return cls.blank(name, ['ring'], **kwargs)

if __name__ == '__main__':
    item1 = Item('candle')
    print item1.category
    print item1.value
    print isinstance(item1, Item)
    print isinstance(item1, Equipable)
    item2 = Equipable.Armor('red chainmail')
    print isinstance(item2, Equipable)
    print item2.slots
