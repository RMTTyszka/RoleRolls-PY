#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import random

def def_targets(targets,numtar):
    newlist = []
    newlist = sorted([[tar.risk_lv,tar] for tar in targets if tar.ALIVE],reverse=True)[:numtar]
    newlist = [tar[1] for tar in newlist]

    return newlist

class Power:
    def __init__(self,atr,skill,caster):
        self.AE = caster.AE(atr,skill)
        self.CT = 1
    def use(self):
        pass

    @classmethod
    def Dual_Heal(cls,caster,targets):
        heal = cls('wis','magery',caster)
        heal.CT = 15.0
        heal.spiritpower = 22
        def use():
            targets = def_targets(targets,2)
            for target in targets:
                if caster.SP - heal.spiritpower*len(targets) < 0:
                    print 'not enough spiritpower'
                    caster.useskill = 'Wait'
                    return heal
                print caster.life_percent
                target.SP -= heal.spiritpower*len(targets)
                heallife = (random.randint(1,100) + heal.AE)/10 * 6
                target.life += heallife
                if target.life >= target.main['status']['MAXlife']:
                    target.life = target.main['status']['MAXlife']
            print caster.name, 'healed', heallife, 'lifes', target.name , 'has', target.life
        heal.use = use
        return heal
    @classmethod
    def Heal(cls,caster,targets):
        heal = cls('wis','magery',caster)
        heal.CT = 10.0
        heal.spiritpower = 15
        def use():
            heal.targets = def_targets(targets,1)
            if len(heal.targets) == 0:
                print 'target not avaiable'
                caster.usekill = "Wait"
                return heal
            if caster.SP - heal.spiritpower*len(heal.targets) < 0:
                print 'not enough spiritpower'
                caster.useskill = 'Wait'
                return heal
            for target in heal.targets:
                print target.name, 'has',target.LIFE_PERCENT,'%'
                caster.SP -= heal.spiritpower
                heallife = (random.randint(1,100) + heal.AE)/10 * 6
                target.LIFE += heallife
            print caster.name, 'healed', heallife, 'lifes', target.name , 'has', target.LIFE,'\n'
        heal.use = use
        return heal

    @classmethod
    def Power_Attack(cls,caster,targets):
        poweratk = cls('str',caster.equipament['mainhand'].wep_skills['atkskill'],caster)
        poweratk.CT = 10.0
        poweratk.spiritpower = 15
        def use():
            poweratk.targets = def_targets(targets,1)
            if caster.SP - poweratk.spiritpower*len(poweratk.targets) < 0:
                    print 'not enough spiritpower'
                    caster.useskill = 'Wait'
                    return poweratk
            for target in poweratk.targets:
                poweratkatk = (random.randint(1,100) + poweratk.AE) - target.EVD
                if poweratkatk >= 50:
                    dam = 15+ caster.mod('str')*5 - target.FORTITUDE
                    dam /= 5
                    target.LIFE -= dam
                    print 'Power Attack',caster.name, 'caused',dam,'of phisical damage on ', target.name,'\n'
        poweratk.use = use
        return poweratk
    @classmethod
    def Wait(cls,caster,targets):
        wait = cls('none','none',caster)
        wait.CT = 0.0
        wait.spiritpower = 0
        def use():
            print wait.caster.name, 'Waited'
        return wait
    @classmethod
    def Meditation(cls,caster,targets):
        medit = cls('int','meditating',caster)
        medit.CT = 10.0
        def use():
            mana = 5 + (random.randint(1,100)+ (caster.mod('int')+caster.mod('meditating')))/10
            caster.SP += mana
            print caster.name,'recovered', mana,'of mana'
        medit.use = use
        return medit
