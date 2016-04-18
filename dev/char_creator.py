#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

import char
import items
import auxiliary
import effects
import items
import powers
import spells
import dice

def create_random_char(name, **kwargs):
    '''
    Generates a new randomized char
    Passing kwargs will fix it's stats
    '''
    random_char = char.Char.blank(name)
    # setar random coisas (attr, skills, items ...)
    return random_char

if __name__ == '__main__':
    create_random_char('boris')
