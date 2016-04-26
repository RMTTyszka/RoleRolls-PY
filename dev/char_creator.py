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
    print char_data,'\n'
    # update dict with real values
    for value in char_data.values():
        print type(value)
        print type(value) == 'dict'
        if type(value) == 'dict':
            for key0, value0 in value.items():
                for key1, value1 in value0.items():
                    if 'lvl' in value1:
                        operator = value1.strip('lvl')[0]
                        operand = value1.strip('lvl')[1:]
                        #char_data[key0][key1] = eval(str(lvl)+operator+operand)
                        char_data[key0][key1] = ops[operator](lvl,int(operand))

    print char_data,'\n'

    # fill char
    if 'role' in char_data:
        file_char = getattr(char.Char,'blank')(name, lvl=lvl)
    else:
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
