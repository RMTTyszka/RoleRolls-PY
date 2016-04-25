#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import matplotlib.pyplot as plt
import numpy as np
import random
import dev

it = dev.constants.items
at = dev.constants.attributes
sk = dev.constants.skills
def create_char(name,classmoethod):
    char = dev.Char()
monster_list = [['goblin warrior','soldier'],['goblin barbarian','brute'],
                ['goblin thief','assassin'],['goblin mage','caster'],
                ['goblin shaman','caster']]
party_list = [['human warrior','soldier'],['human barbarian','brute'],
                ['human thief','assassin'],['human mage','caster'],
                ['human shaman','caster']]
party = []
monsters = []

combat = True
while combat:
    quit()
