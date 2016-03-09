#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
resists file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import resists as C

class Resists(object):
    ''' Base Resists for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the resists.
            "weakness": weakness,
            "slow": slow,
            "stun": stun,
            "blind": blind,
            "curse": curse
        '''
        for resist in C.resists_list:
            if resist in kwargs:
                setattr(self, resist, kwargs[skill])
            else:
                setattr(self, resist, 0)

        # fazer properties

if __name__ == '__main__':
    Resist1 = Resists()
    assert type(Resist1.weakness) is int
