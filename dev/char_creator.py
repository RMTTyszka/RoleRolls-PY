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
    with open(ROOT_FOLDER+'chars/'+filename, 'r') as char_file:
        char_data = json.loads(char_file.read())
        char_bonus = {'innate': {}}
        char_role = char_data['role']
    # update dict with real values
    for key0, value0 in char_data.items():
        if (key0 == 'skills' or
            key0 == 'attributes' or
            key0 == 'defenses' or
            key0 == 'resists' or
            key0 == 'status'):
            for key1, value1 in value0.items():
                char_bonus['innate'][key1] = char_bonus['innate'].get(key1,0)+ int(value1)
        try:
            for key1, value1 in value0.items():
                if 'lvl' in value1:
                    operator = value1.strip('lvl')[0]
                    operand = value1.strip('lvl')[1:]
                    #char_data[key0][key1] = eval(str(lvl)+operator+operand)
                    char_data[key0][key1] = ops[operator](lvl,int(operand))
        except:
            continue
    with open(ROOT_FOLDER+'roles/'+char_role, 'r') as char_file:
        char_data = json.loads(char_file.read())
    # fill char
    file_char = char.Char.blank(name, lvl=lvl)
    if 'attributes' in char_data:
        for attr, value in char_data['attributes'].items():
            setattr(file_char.attributes, '_'+attr, value)
    if 'skills' in char_data:
        for skill, value in char_data['skills'].items():
            setattr(file_char.skills, '_'+skill, value)
    # fill the rest here

    return file_char

if __name__ == '__main__':
    #random_char = random('boris')
    #print random_char
    file_char = from_file('dudu', 'goblin_peasant.json')
    #for var in vars(file_char):
        #print var,getattr(file_char,var)
    print 'agility',file_char.attributes.agility()
