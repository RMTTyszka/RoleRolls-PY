#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import config
import random
class Test:
    def __init__(self,caster,stat,cond,value,target,numtar,skill): 
        self.value = value
        self.cond = cond
        self.target = {}
        if target == 'allies':
            self.target = config.players
        elif target == 'monsters':
            self.target = config.monsters
        elif target == 'self':
            self.target = [caster]
        self.numtar = numtar
        self.caster = caster
    @classmethod
    def random_tar(cls,caster,stat,cond,value,target,numtar,skill):
        random_tar = cls(caster,stat,cond,value,target,numtar,skill)
        true_target = [random.choice(random_tar.target)]
        return True, true_target
        
    @classmethod
    def life(cls,caster,stat,cond,value,target,numtar,skill):
        life = cls(caster,stat,cond,value,target,numtar,skill)
        true_target = []
        sum = 0
        
        if life.cond == '<=':
            
            for x in life.target:
                if x.LIFE_PERCENT <= life.value and x.ALIVE:
                    sum +=1
                    true_target.append(x)
            if sum >= numtar:
                return True, true_target
            else:
                return False
                
        if life.cond == '>=':
            
            for x in life.target:
                if x.LIFE_PERCENT >= life.value and x.ALIVE:
                    sum +=1
                    true_target.append(x)
            if sum >= numtar:
                return True, true_target
            else:
                return False
    @classmethod
    def SP(cls,caster,stat,cond,value,target,numtar,skill):
        SP = cls(caster,stat,cond,value,target,numtar,skill)
        true_target = []
        sum = 0
        
        if SP.cond == '<=':
            for x in SP.target:
                if x.SP_PERCENT <= SP.value:
                    sum +=1
                    true_target.append(x)
            if sum >= numtar:
                return True, true_target
            else:
                return False
                
        if life.cond == '>=':
            
            for x in SP.target:
                if x.SP_PERCENT >= SP.value:
                    sum +=1
                    true_target.append(x)
            if sum >= numtar:
                return True, true_target
            else:
                return False
    @classmethod
    def armor(cls,caster,stat,cond,value,target,numtar,skill):
        armor = cls(caster,stat,cond,value,target,numtar,skill)
        true_target = []
        sum = 0
        
        for x in armor.target:
            if x.equipament['armor'].type == armor.value and x.ALIVE:
                sum +=1
                true_target.append(x)
        if sum >= numtar:
            return True, true_target
        else:
            return False

    @classmethod
    def effect(cls,caster,stat,cond,value,target,numtar,skill):
        effect = cls(caster,stat,cond,value,target,numtar,skill)
        sum = 0
        
        for x in effect.target:
            for cat in effect.target.effects.keys():
                if x.effects[cat].has_key(effect.value)and x.ALIVE:
                    sum +=1
                    true_target.append(x)
        if sum >= numtar:
            return True, true_target
        else:
            return False    
    @classmethod
    def stamina(cls,caster,cond,comparer,target,numtar):
        stamina = cls(caster,cond,comparer,target,numtar)
        sum = 0
        if cond == '<=':
            
            for x in stamina.target:
                if x.life_percent < percent and x.ALIVE:
                    sum +=1
            if sum >= numtar:
                return True, true_target
            else:
                return False
        if cond == '>=':
            if target == 'allies':
                targets = 'party'
            else:
                targets = 'monsters'
            for x in stamina.target:
                if x.life_percent < percent and x.ALIVE:
                    sum +=1
                    true_target.append(x)
            if sum >= numtar:
                return True, true_target
            else:
                return False 