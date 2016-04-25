#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import effects as C

class Effects(object):
    ''' Base Effect for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the effects.
        '''

    @staticmethod
    def poisoned(char):
        '''
        Poisoned effect
        '''
        print 'coisas a fazer quando o char está poisoned'
        char.life -= 10


# if __name__ == '__main__':
#     Effect1 = Effects.poisoned()
#     Effect1.run()
#     assert type(Effect1.weakness) is int
