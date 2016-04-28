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
def create_armor(lvl,category = None,base = None, material = None, enchantment = None):
    '''
    create a random armor of a determined category if
    it's given, else it will create a armor of any category.
    a base, the material and an enchant can be passed as arg too
    '''
    #run code if base is none
    if base == None:
        base = 'fullplate'
    else:
        base = 'fullplate'
    #run code if category is none
    if category == None:
        category = 'heavy'
    else:
        category = 'heavy'
    #run code if material is none
    
    #run code if enchantment is none

    #create armor
    armor = items.Equipable.Armor(category=category,base=base )
    #get positionals
    armor.lvl = lvl
    return armor
def random(name, **kwargs):
    '''

    Generates a new randomized char
    Passing kwargs will fix it's stats
    '''
    random_char = char.Char.blank(name)
    # setar random coisas (attr, skills, items ...)
    return random_char

def from_file(name, filename, lvl=1, ):
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
            armor = create_armor(value0)

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
    file_char = from_file('dudu', 'goblin_warrior.json')
    #for var in vars(file_char):
        #print var,getattr(file_char,var)
    print file_char.equipment.armor.category
