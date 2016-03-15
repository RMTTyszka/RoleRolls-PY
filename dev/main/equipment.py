#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import equipment as C

class Equipment(object):
    ''' Base Equipment for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the equipment.
            "mainhand": mainhand,
            "offhand": offhand,
            "helmet": helmet,
            "neck": neck,
            "armor": armor
            "wrist": wrist
            "gauntlet": gauntlet
            "ring1": ring1
            "ring2": ring2
            "belt": belt
            "boots": boots
            "extra": extra
        '''
        for equipment in C.equipment_list:
            if equipment in kwargs:
                setattr(self, equipment, kwargs[equipment])
            else:
                setattr(self, equipment, None)

    def __iter__(self):
        for equipment in C.equipment_list:
            yield equipment, getattr(self, equipment)

    @property
    def evade(self):
        return sum(equipment.evade for name, equipment in self if hasattr(equipment, 'evade'))

    def put(self, item,  slot):
        '''
        Puts the item in the slot.
        Returns the item if the slot doesn't exists or the old item if the slot is
        occupied
        '''
        if item in C.equipment_list:
            old_item = getattr(self, slot) if hasattr(self, slot) else False
            setattr(self, slot, item)
            return old_item
        return item

if __name__ == '__main__':
    Equi1 = Equipment()
    print dir(Equi1)
    # pass
    for i in Equi1:
        print i
