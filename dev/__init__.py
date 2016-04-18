#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
__init__ file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

from auxiliary import *
from char_creator import *
from char import *
from dice import *
from effects import *
from items import *
from powers import *
from spells import *
import constants as C

if __name__ == '__main__':
    char = Char.blank('boi')
    armor1 = items.Equipable.Armor(name='gato', base='cloth')
    armor1.evade = 10
    char.equip(armor1, 'armor')
    char.attributes.strength = 20
    print char.attributes.strength
    print char.attributes.str_mod
    print char.attributes.roll('vitality')
    print char.equipment.armor.evade
    print char.EVD
    char.run_effects()
