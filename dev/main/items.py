#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import base
from constants import items as C

class Item(base.Base):
    ''' Base class for any item in the game '''

    def __init__(self, name, **kwargs):
        super(Item, self).__init__(name, **kwargs)
        self.category = C.item_cat[self.lvl]
        self.value = C.item_value[self.lvl]

class Equipable(Item):
    ''' Base class for any equipable in the game '''

    def __init__(self, name, **kwargs):
        super(Equipable, self).__init__(name, **kwargs)

    @classmethod
    def Armor(cls, name, **kwargs):
        instance = cls(name, **kwargs)
        return instance

    @classmethod
    def Weapon(cls, name, **kwargs):
        instance = cls(name, **kwargs)
        return instance

    @classmethod
    def Ring(cls, name, **kwargs):
        instance = cls(name, **kwargs)
        return instance

if __name__ == '__main__':
    item1 = Item('candle')
    print item1.category
    print item1.value
    print item1.equipable
