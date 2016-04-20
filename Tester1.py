#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

import random
import dev
it = dev.constants.items
at = dev.constants.attributes
sk = dev.constants.skills

def attack(attacker, target=None, weapon=None):
    '''
    Attacks the enemy, returning the damage and any other penalty
    '''
    #create checkers
    critical = False
    counter = False
    hit = False
    #cod if target == None

    #get vars
    attk = attacker.attack(weapon)

    #get target vars
    evade = target.evade
    roll = random.randint(1,100)+ attk - evade - 50
    if roll >= 0:
        hit = True
        critical = True if random.randint(1,100) <= attacker.critical else False
        d = damage(attacker,target,weapon,critical)
        return d
    else:
        counter = True if random.randint(1,100) <= target.counter else False
        damage(attacker,target) if counter == True else None
        return 0
def damage(attacker, target, weapon=None, critical=False):
    '''
    Get damage multiplicated by Attribute and skill, and reduced from
    protection of the target
    Multiply by critical-damage if critical is True
    '''
    #run code if weapon == None
    #print attacker.attributes
    roll_01 = random.randint(weapon.min_damage,weapon.max_damage)
    #print getattr(attacker.skills,weapon.attk_skill+'_mod')(), 'skill_mod',getattr(attacker.skills,weapon.attk_skill)()
    #print attacker.at_damage_mod, 'damage_mod'
    print target.fortitude, 'fortitude'

    #print 'min',weapon.min_damage,'max',weapon.max_damage, roll_01
    damage_mod = getattr(attacker.skills,weapon.attk_skill+'_mod')()+attacker.at_damage_mod - target.fortitude
    #print damage_mod, 'is mod'
    #print weapon.mult_damage
    damage_mod *= weapon.mult_damage
    attr_damage = getattr(attacker.attributes,weapon.damage_attr+'_mod')()*2
    attr_damage *= weapon.mult_attr
    prot = target.prot - attacker.armor_penetration(weapon)
    if prot < 0: prot = 0
    total_damage = roll_01 + damage_mod + attr_damage - prot
    total_damage *= attacker.critical_damage if critical == True else 1
    if total_damage <= 0:
        take_damage(target,0)
    else:
        take_damage(target,total_damage)
    return total_damage
def take_damage(target,damage):
    target.life -= damage
arg_list = ['heavy','medium','light']
defenders_list = ['heavy_armor', 'medium_armor','light_armor']
attackers_list = ['heavy_weapon', 'medium_weapon', 'light_weapon']
defenders = []
attackers = []

tst = 'rush'
if tst == 'combat':
    pass
else:
    for x in range(20):
        y = (x+1)*5
        Attributes = dev.Attributes(**{attr: y for attr in dev.constants.attributes.attributes_list})
        Skills = dev.Skills(**{skill: y for skill in dev.constants.skills.skills_list})
        Defenses = dev.Defenses()
        Resists = dev.Resists()
        for defender,armor_cat in zip(defenders_list,arg_list):
            Equipment = dev.Equipment(armor=dev.Equipable.Armor(base=random.choice(it.armors_dict[armor_cat].keys())))

            char = dev.char.Char(name=defender,lvl=x+1, attributes=Attributes, skills=Skills,
                        defenses=Defenses, resists=Resists, equipment=Equipment)
            char.damage_done = []
            char.damage_taken = []
            defenders.append(char)
        for attacker,wep_cat in zip(attackers_list,arg_list):
            Equipment = dev.Equipment(mainhand=dev.Equipable.Weapon(base=random.choice(it.weapons['cutting'][wep_cat].keys())))

            char = dev.char.Char(name=attacker,lvl=x+1, attributes=Attributes, skills=Skills,
                        defenses=Defenses, resists=Resists, equipment=Equipment)
            char.damage_done = []
            char.damage_taken = []
            attackers.append(char)
        for z in range(3):
            for y in range(3):
                dam = attack(attackers[x*3+z],defenders[x*3+y],attackers[x*3+z].equipment.mainhand)
                #print dam
                attackers[x*3+z].damage_done.append(dam)
                defenders[x*3+y].damage_taken.append(dam)
    for at in attackers:

        print at.skills.fencing_mod(), at.at_damage_mod
