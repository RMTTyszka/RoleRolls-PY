#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
base file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

from constants import base as C
C.args_list.remove('name')

class Base(object):
    ''' Base class for anything in the game '''

    def __init__(self, name, **kwargs):
        '''
        Initializes the class.
        arguments - all are optional, except the name:
            name: base name (positional)

            lvl: base level

            attributes: base attributes ('Attribute' object)

            defenses: base defenses ('Defense' object)

            resists: base resists ('Resist' object)

            inventory: base inventory ('inventory' object)

            effects: base effects (list, values are 'Effects' objects)

            powers: base powers (list, values are 'Power' objects)

            spells: base spells (list, values are 'Spells' objects)

            bonuses: base bonuses (list, values are 'Bonus' objects)

            HP: base HP - if not specified it's set with base's attributes

            SP: base SP - if not specified it's set with base's attributes

            ST: base ST - if not specified it's set with base's attributes
        '''



    def __repr__(self):
        string = 'base\nname: {} lvl: {}\nHP: {} MP: {}'.format(self.name, self.lvl,
            self.HP, self.SP)
        if self.effects:
            string += '\neffects: {}'.format(self.effects.keys())
        return string

    def run_effects(self):
        '''
        Runs the effects in the effects dict
        '''
        for effect_name, effect in self.effects.items():
            effect(self)

    def calculate_bonus(self):
        '''
        Calculates all the bonuses and add them to it's corresponding object
        '''

    # HP property


if __name__ == '__main__':
    assert Base('test')
    assert Base('test').HP_percent is 0
    assert Base('test', HP=10).HP is 10
    assert Base('test', HP=10).HP_percent is 1
    b = Base("test")
    b.maxHP = 50
    print b.HP
    b.HP += 10
    print b
    print 'All tests ok!'
