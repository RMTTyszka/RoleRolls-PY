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
def attack(attacker, target=None, weapon=None,fulltest=True):
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
    roll = random.randint(100,100)+ attk - evade
    correct = attk+50 - evade
    #print 'attk: {0}, evade: {1}, roll: {2} == {3}'.format(attk,evade,roll+evade-attk,roll)
    if roll >= 0:
        hit = True
        critical = True if random.randint(1,100) <= attacker.critical else False
        d = damage(attacker,target,weapon,critical,fulltest)
        return d*(1+correct/100.00)
    else:
        counter = True if random.randint(1,100) <= attacker.counter else False
        d = damage(attacker,target,weapon,critical,fulltest) if counter == True else 0
        return 0
def damage(attacker, target, weapon=None, critical=False, fulltest=True):
    '''
    Get damage multiplicated by Attribute and skill, and reduced from
    protection of the target
    Multiply by critical-damage if critical is True
    '''
    #run code if weapon == None
    enchant_damage = 0
    for cat,bonuses in weapon.bonuses.items():
        for bonus_name,bonus_value in bonuses.items():
            enchant_damage += bonus_value if bonus_name == 'damage' else 0
    roll_01 = random.randint(weapon.min_damage,weapon.max_damage)+enchant_damage
    roll_01 = (weapon.min_damage+weapon.max_damage)/2 + enchant_damage
    roll_01 *= weapon.mult_damage
    #print 'min',weapon.min_damage,'max',weapon.max_damage, roll_01
    damage_mod = getattr(attacker.skills,weapon.attk_skill+'_mod')()+attacker.at_damage_mod - target.fortitude
    #print damage_mod, 'is mod'
    #print weapon.mult_damage

    damage_mod *= weapon.mult_damage
    attr_damage = getattr(attacker.attributes,weapon.damage_attr+'_mod')()*2
    attr_damage *= weapon.mult_attr
    prot = target.protection - attacker.armor_penetration(weapon)
    if prot < 0: prot = 0
    total_damage = roll_01 + damage_mod + attr_damage - prot
    total_damage *= attacker.critical_damage if critical == True else 1
    if total_damage <= 0:
        take_damage(target,0)
    else:
        take_damage(target,total_damage)
    if fulltest == False:
        print attacker.lvl
        print '{0},/// {1}'.format(attacker.name,target.name)
        print 'base damage :{0}'.format(roll_01)
        #print 'skill_mod :{0}, skill_mod * weapon_multiplicator: {1}'.format(
        #getattr(attacker.skills,weapon.attk_skill+'_mod')(), damage_mod)
        #print 'attr_modx2 :{0}, total attr damage {1}'.format(attr_damage/ weapon.mult_attr,attr_damage)
        #print 'fortitude :{0}'.format(target.fortitude)
        print 'protection - armor pen :{0}'.format(prot)
        print '{0}+{1}+{2}-{3} = {4}\n'.format(roll_01,damage_mod,attr_damage,prot,total_damage)
    return total_damage
def take_damage(target,damage):
    target.life -= damage
arg_list1 = ['heavy','medium','light']
arg_list2 = ['heavy','medium','light','2medium', '2light']
defenders_list = ['heavy_armor', 'medium_armor','light_armor']
attackers_list = ['heavy_weapon', 'medium_weapon', 'light_weapon','2medium_weapon', '2light_weapon']
defenders = []
attackers = []
total_W = {'heavy_weapon':[],'medium_weapon':[],'light_weapon':[],'2medium_weapon':[],'2light_weapon': []}
total_A = {'heavy_armor':[],'medium_armor':[],'light_armor':[]}
total_B = {'heavy_weapon':483.998,'medium_weapon':480.626,'light_weapon':490.897,'2medium_weapon':480.725,'2light_weapon': 490.138}
for x in range(20):
    y = (x+1)*5
    Attributes = dev.Attributes(**{attr: y for attr in dev.constants.attributes.attributes_list})
    Skills = dev.Skills(**{skill: y for skill in dev.constants.skills.skills_list})
    Defenses = dev.Defenses()
    Resists = dev.Resists()
    Bonuses = {'innate': {'critical_damage': 0}}
    for defender,armor_cat in zip(defenders_list,arg_list1):
        Equipment = dev.Equipment(armor=dev.Equipable.Armor(base=random.choice(it.armors_dict[armor_cat].keys()),lvl=x+1, ))
        char = dev.char.Char(name=defender,lvl=x+1, attributes=Attributes, skills=Skills,
                    defenses=Defenses, resists=Resists, equipment=Equipment, bonuses=Bonuses)
        char.damage_done = []
        char.damage_taken = []
        defenders.append(char)
    for attacker,wep_cat in zip(attackers_list,arg_list2):
        #wep_cat = wep_cat.lstrip('2')
        Equipment = dev.Equipment(mainhand=dev.Equipable.Weapon(base=random.choice(it.weapons['cutting'][wep_cat].keys()),lvl=x+1,bonuses={'innate':{'damage': 10*(x+1)},'magic':{},'moral':{}}))

        char = dev.char.Char(name=attacker,lvl=x+1, attributes=Attributes, skills=Skills,
                    defenses=Defenses, resists=Resists, equipment=Equipment, bonuses=Bonuses)
        char.damage_done = []
        char.damage_taken = []
        char.damage_std = []
        attackers.append(char)
    for z in range(5):
        for y in range(3):
            dam = []
            for trys in range(int(600/attackers[x*5+z].equipment.mainhand.AS_base)):
                dam.append(attack(attackers[x*5+z],defenders[x*3+y],attackers[x*5+z].equipment.mainhand))
            attackers[x*5+z].damage_std.append(np.std(dam))
            dam = sum(dam)
            dam /= 600
            dam = round(dam,3)
            attackers[x*5+z].damage_done.append(dam)
            defenders[x*3+y].damage_taken.append(dam)
for de in defenders:
    break
    if de.name == 'heavy_armor':
        print de.lvl
for lvl in range(20):
    break
    for size in arg_list:
        for at in attackers:
            if at.name == size+'_weapon':
                for de in defenders:
                    if at.lvl == de.lvl:
                        attack(at,de,at.equipment.mainhand,fulltest=False)
for at in attackers:
    total_W[at.name].append(sum(at.damage_done))
for de in defenders:
    total_A[de.name].append(sum(de.damage_taken))
for wep in total_W:
    print wep, sum(total_W[wep])
    #/total_B[wep]*100-100
print '\n'
for arm in total_A:
    print arm, sum(total_A[arm])
for wep in attackers_list:
    plt.plot(total_W[wep],label=wep)
    plt.legend(loc="upper center")
    #plt.xticks([x+1 for x in range(20)])
plt.show()
for lvl in range(20):
    break
    for at in attackers:
        print str(at.lvl) + ' is ', lvl+1,'?'
        if at.lvl == lvl+1:
            print 'yes'
            for de in defenders:
                print str(de.lvl) + ' is ', lvl+1,'?'
                if de.lvl == lvl+1:
                    print 'yes'
                    attack(at,de,at.equipment.mainhand,fulltest=False)
                print 'no'
                if lvl+1 == 3:
                    quit()
        print 'no'
