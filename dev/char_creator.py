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
from constants import items as Ci
from constants import equipment as Ce
import json
import operator as op
import random
from os.path import dirname, abspath

ROOT_FOLDER = dirname(abspath(__file__))+'/'

ops = {
        '+' : op.add,
        '-' : op.sub,
        '*' : op.mul,
        '/' : op.div,
        '%' : op.mod,
        '^' : op.xor
        }
def create_armor(lvl, base = None, name=None, category = None, material = None, power = None, effect=None, bonuses = None):
    '''
    create a dict to pass as argument to an item.equipable.armor class
    a_dict = {'base':
              'category':
              'material':
              'enchant'}
    '''
    #create a_dict
    a_dict = {}
    #run code if base is none
    a_dict['lvl'] = lvl
    if base != None:
        a_dict['base'] = base
        a_dict['category'] = [cat for cat, base
                          in Ci.armors_dict.items()
                          if a_dict['base']
                          in base.keys()][0]
    else:
        a_dict['category'] = category
        a_dict['base'] = random.choice(Ci.armors_dict[a_dict['category']].keys())
    a_dict['name'] = str(name)+' '+str(a_dict['base']) if name != None else a_dict['base']
    a_dict['material'] = material if material != None else 'common'
    a_dict['power'] = [power]
    a_dict['effect'] = effect
    a_dict['bonuses'] = bonuses if bonuses != None else {'magic':{},
                                                         'innate':{},
                                                         'moral':{}}


    #create armor
    print a_dict
    armor = items.Equipable.Armor(**a_dict)
    #get positionals
    return armor
#def random(name, **kwargs):
#    '''
#
#    Generates a new randomized char
#    Passing kwargs will fix it's stats
#    '''
#    random_char = char.Char.blank(name)
#    # setar random coisas (attr, skills, items ...)
#    return random_char

def from_file(name, filename, lvl=1 ):
    '''
    Creates a char from a json file the configuration
    '''
    # get character info, bonus, powers and drops
    with open(ROOT_FOLDER+'chars/'+filename, 'r') as char_file:
        char_data = json.loads(char_file.read())

    char_bonus = {}
    #get info and drop
    char_role = char_data['role']
    char_race = char_data['race']
    char_drop = char_data['drop']
    #get bonus
    for key0, value0 in char_data.items():
        if (key0 == 'skills' or
            key0 == 'attributes' or
            key0 == 'defenses' or
            key0 == 'resists' or
            key0 == 'status'):
            for key1, value1 in value0.items():
                char_bonus[key1] = char_bonus.get(key1,0) + int(value1)

    # get race bonus, powers and drops
    with open(ROOT_FOLDER+'races/'+char_race+'.json','r') as char_file3:
        char_data3 = json.loads(char_file3.read())
    # get bonus
    for key0, value0 in char_data3.items():
        if (key0 == 'skills' or
            key0 == 'attributes' or
            key0 == 'defenses' or
            key0 == 'resists' or
            key0 == 'status'):
            for key1, value1 in value0.items():
                char_bonus[key1] = char_bonus.get(key1,0) + int(value1)
    # get powers

    # get drops

    #get role bonus and equips
    with open(ROOT_FOLDER+'roles/'+char_role+'.json', 'r') as char_file2:
        char_data2 = json.loads(char_file2.read())
    #get bonus
    for key0, value0 in char_data2.items():
        if (key0 == 'skills' or
            key0 == 'attributes' or
            key0 == 'defenses' or
            key0 == 'resists' or
            key0 == 'status'):
            for key1, value1 in value0.items():
                char_bonus[key1] = char_bonus.get(key1,0) + int(value1)
    # get equips
        if key0 == 'equipment':
            armor = create_armor(lvl, category=value0['armor'])

    # fill char
    file_char = char.Char.blank(name, lvl=lvl)
    #equip char
    # fill bonus and update
    file_char.bonuses['innate'] = char_bonus
    file_char.equip(armor,'armor')
    file_char._update_bonus()
    print file_char.bonuses
    # fill the rest here

    return file_char

if __name__ == '__main__':
    #random_char = random('boris')
    #print random_char
    file_char = from_file('dudu', 'goblin_warrior.json', lvl=12)
    
    #for var in vars(file_char):
        #print var,getattr(file_char,var)
    for var in vars(file_char.attributes):
        print var, getattr(file_char.attributes,var)
