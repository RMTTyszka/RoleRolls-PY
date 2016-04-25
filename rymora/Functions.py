#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import random

def randATR(nv):
    b = 0
    for j in range(15):
        b += random.randint(1,1) #(0,1)
    return b

def randatr(nv):
    b = 0
    for j in range(5):
        b += random.randint(1,1)  #(-1,1)
    return b

def randSKILL(nv):
    b = 0
    for j in range(15):
        b += random.randint(1,1)
    return b

def randskill(nv):
    b = 0
    for j in range(10):
        b += random.randint(1,1)
    return b

def rand_bonus_equip(nv, x):
    b = 0
    for j in range(nv/2*x):
        b += random.randint(-1,1)
    return b


def autoattack(attacker, target=None):
    if target == None:
        comparare = [[char, char.risk_lv] for char in attacker.AT_target]
        compare =  max(comparare, key=lambda x:x[1])

        defender = compare[0]
    else:
        defender = target
    crit = False
    hit = False
    counter = False
    z = random.randint(1,100)
    a = attacker.AT(attacker.equipament['mainhand'])
    b = defender.EVD
    if z + a - b >= 100 - (attacker.CRIT-defender.RESILIENCE):
        crit = True
    if z + a - b >= 20:
        hit = True
    if z + a - b <= defender.mod('counterrating'):
        counter = True
    if counter:
        d = defender.main_damage(attacker)
        print 'Counter attack!!!---', attacker.name , 'received', d,'damage'
        attacker.LIFE -= d
        print attacker.name, 'has', attacker.LIFE, 'of life'
    if hit:
        d = attacker.main_damage(defender)
        str = 'Hit!!!----'
        if crit:
            str =  'Crit!!!----'
            d *= 2
        defender.LIFE -= d
        print str, attacker.name, 'caused', d, 'damage to', defender.name, defender.LIFE_PERCENT
        print defender.name, 'has', defender.LIFE, 'of life', defender.LIFE_PERCENT,'%'
    if hit == False:
        print attacker.name, 'Missed'
    attacker.AT_target = None
    #{'AT':,'evade':,'AE':,'resist':,'AS':,'crit':,'resil':,'defense':,'atr':,'status':,'stagen':,'damage':,'fortitude':,'prot':,'skills':}

def t_autoattack(AT,DEF):
    a = random.randint(1,100)
    t = a + AT.AT(AT.equipament['mainhand']) - DEF.EVD
    print a+AT.AT(AT.equipament['mainhand']), DEF.EVD
    if t >= 50:
        return AT.main_damage(DEF)
    else:
        return 0



if __name__ == '__main__':
    # stress test random to check if they're in range
    for i in range(100):
        assert 0 <= randATR(0) <= 15
        assert -5 <= randatr(0) <= 5
        assert 0 <= randSKILL(0) <= 15
        assert 0 <= randskill(0) <= 10
        assert -10 <= rand_bonus_equip(10, 2) <= 10
    # ... add all the tests
    print 'All tests ok!'
