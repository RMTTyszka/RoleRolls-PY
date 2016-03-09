#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
attributes file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import attributes as C

class Attributes(object):
    ''' Base Atributes for any item in the game '''

    def __init__(self, strength=10, agility=10, vitality=10, wisdom=10, inteligence=10,
        charisma=10):
        '''
        Initializes the attributes.
            "strength": char strength,
            "agility": char agility,
            "vitality": char vitality,
            "wisdom": char wisdom,
            "inteligence": char inteligence}
            # "charisma": char charisma} - not implemented so far
        '''
        self.str = strength
        self.agi = agility
        self.vit = vitality
        self.wis = wisdom
        self.int = inteligence
        self.cha = charisma

    @property
    def str_mod(self):
        return self.str/2 - 5

    @property
    def agi_mod(self):
        return self.agi/2 - 5

    @property
    def vit_mod(self):
        return self.vit/2 - 5

    @property
    def wis_mod(self):
        return self.wis/2 - 5

    @property
    def int_mod(self):
        return self.int/2 - 5

    @property
    def cha_mod(self):
        return self.cha/2 - 5


if __name__ == '__main__':
    Attr1 = Attributes()
    assert type(Attr1.str) is int
    assert type(Attr1.str_mod) is int

    assert type(Attr1.agi) is int
    assert type(Attr1.agi_mod) is int

    assert type(Attr1.vit) is int
    assert type(Attr1.vit_mod) is int

    assert type(Attr1.wis) is int
    assert type(Attr1.wis_mod) is int

    assert type(Attr1.int) is int
    assert type(Attr1.int_mod) is int

    assert type(Attr1.cha) is int
    assert type(Attr1.cha_mod) is int
    print 'All tests ok!'
