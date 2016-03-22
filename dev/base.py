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

        # handles positional
        self.name = name
        self.alive = True

        # handles kwargs
        for arg_name in C.args_list:
            if arg_name in kwargs:
                if arg_name in C.properties:
                    setattr(self, 'max'+arg_name, kwargs[arg_name])
                    setattr(self, '_'+arg_name, kwargs[arg_name])
                else:
                    setattr(self, arg_name, kwargs[arg_name])
            else:
                if arg_name in C.properties:
                    setattr(self, 'max'+arg_name, None)
                    setattr(self, '_'+arg_name, None)
                else:
                    setattr(self, arg_name, None)
        self.lvl = self.lvl or 0

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
    @property
    def HP(self):
        '''
        base HP
        '''
        return self._HP
    @HP.setter
    def HP(self, value):
        value = self.maxHP if value > self.maxHP else value
        self._HP = value
        self._alive = True if self._HP > 0 else False
    @property
    def HP_percent(self):
        '''
        base HP in percentage
        interval: 0 - 1
        '''
        return self._HP/self.maxHP if self.maxHP > 0 else 0
    @HP_percent.setter
    def HP_percent(self, value):
        self.HP = int(round(value*self.maxHP))

    # SP property
    @property
    def SP(self):
        '''
        base SP
        '''
        return self._SP
    @SP.setter
    def SP(self, value):
        value = self.maxSP if value > self.maxSP else value
        self._SP = value
    @property
    def SP_percent(self):
        '''
        base SP in percentage
        interval: 0 - 1
        '''
        return self._SP/self.maxSP if self.maxSP > 0 else 0
    @SP_percent.setter
    def SP_percent(self, value):
        self.SP = int(round(value*self.maxSP))

    # ST property
    @property
    def ST(self):
        '''
        base ST
        '''
        return self._ST
    @ST.setter
    def ST(self, value):
        value = self.maxST if value > self.maxST else value
        self._ST = value
    @property
    def ST_percent(self):
        '''
        base ST in percentage
        interval: 0 - 1
        '''
        return self._ST/self.maxST if self.maxST > 0 else 0
    @ST_percent.setter
    def ST_percent(self, value):
        self.ST = int(round(value*self.maxST))


if __name__ == '__main__':
    assert Base('test')
    assert Base('test').HP_percent is 0
    assert Base('test', HP=10).HP is 10
    assert Base('test', HP=10).HP_percent is 1
    print 'All tests ok!'
