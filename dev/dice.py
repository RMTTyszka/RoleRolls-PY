#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
dice file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import random

def roll_01(maximum):
    return sum(random.randint(0, 1) for i in range(maximum))

if __name__ == '__main__':
    print roll_01(10)
