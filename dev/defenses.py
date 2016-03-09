#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
defenses file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import defenses as C

class Defenses(object):
    ''' Base Defenses for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the defenses.
            "cutting", cutting,
            "smashing", smashing,
            "piercing", piercing,
            "magic", magic
        '''
        for defense in C.defenses_list:
            if defense in kwargs:
                setattr(self, defense, kwargs[skill])
            else:
                setattr(self, defense, 0)

        # fazer properties

if __name__ == '__main__':
    Defense1 = Defenses()
    assert type(Defense1.cutting) is int
