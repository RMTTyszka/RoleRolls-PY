#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import const as C
import Powers as P
from Powers import Power
import Functions as F                                                                                                                                                                                                                                      
import random                                                                                                                                                                                                                        
import itens as I
from test import Test
import time

class Char(object):                                                                                                                                                                                                                                
    def __init__(self,nv):    
        self.nv = nv                                                                                                                                                                                                                       
        self.main = {}
        #main atributes 
        for atr in C.atr_list:
            setattr(self,atr,0)                                                                                                                                                                                                 

        #Skills                                                                                                                                                                                                                   
        for skill in C.skills_list:
            setattr(self,skill,0)
        self.at_e = 0
        self.at = 0
        #about defense                                                                                                                                                                                                                          
        self.defenses = {}                                                                                                                                                                                                                  
        self.resists = {}                                                                                                                                                                                                                   
        self.equipament = {}
        self.equipament['offhand'] = 'empty'
        self.weaponpower = 'x'
        for defe in C.defenses_list:
            self.defenses[defe] = self.defenses.get(defe,0)
        for res in C.resist_list:
            self.resists[res] = self.resists.get(res,0)
        self.bonus_E = {} 
        self.bonus_T = {} 
        self._life = None
        self._lifeMAX = 0
        self._sp = None
        self.effects = {}
        self.effects['harmfull'] = {}
        self.effects['helpfull'] = {}
        #atributes used for powers and targets
        self.useskill = 'Wait'
        self.target = None
        self.AE_target = None
        self.AT_target = None
        self._live = True
    @property
    def LIFEMAX(self):
        a = 50
        b = self.mod('vit')*10
        c = self.mod('life')
        self._lifeMAX = a + b + c
        if self._life == None:
            self._life = self._lifeMAX
        return self._lifeMAX
    @property
    def LIFE(self):
        return self._life
    @LIFE.setter
    def LIFE(self,value):
        self._life = value
        if self._life >= self.LIFEMAX:
            self._life = self.LIFEMAX
        if self._life <= 0:
            self._life = 0
            self._live = False
        if self._life >0: self._live = True
    @property
    def ALIVE(self):
        if self._live:
            return True
        else:
            return False
    @property    
    def LIFE_PERCENT(self):
        return round(self.LIFE/self.LIFEMAX*100,2)
    @LIFE_PERCENT.setter
    def LIFE_PERCENT(self,value):
        self._life = self.LIFEMAX*value/100
        
    @property
    def SPMAX(self):
        a = 50
        b = self.mod('int')*2
        self._spMAX = a+b
        if self._sp == None:
            self._sp = self._spMAX
        return self._spMAX
    @property
    def SP(self):
        return self._sp
    @SP.setter
    def SP(self,value):
        self._sp = value
        if self._sp > self.SPMAX:
            self._sp = self.SPMAX
    @property    
    def SP_PERCENT(self):
        return round(self.SP/self.SPMAX*100,2)
    @SP_PERCENT.setter
    def SP_PERCENT(self,value):
        self._sp = self.SPMAX*value/100
        
    @property
    def STAMINMAX(self):
        self._stamax = 25+ self.mod('vit')/2+self.mod('meditating')/2
        return self._stamax
        
        
    def AS(self,weaponhand):
        a = self.equipament[weaponhand].wep_atr['ASbase']
        b = self.mod('as')
        return round(a * (100-b)/100,2)
    @property
    def EVD(self):                                                                                                                                                                                                                   
        a = self.mod('reflex')
        b = self.mod('agi')
        c = self.mod('evade')
        d = a + b + c
        return d
    def AT(self,weapon):
        a = self.mod('at') + weapon.wep_atr['modataque']
        b = self.mod(weapon.wep_skills['atkskill'])
        c = self.mod(weapon.wep_skills['atkatr'])/5
        d = 0
        if self.equipament['offhand'] == 'heavyweapon' or self.equipament['offhand'] == 'empty':
            d = 8
        return a + b + c + d
    def AE(self,atr,skill):
        a = self.mod(atr)/5
        b = self.mod(skill)
        c = self.mod('ae')
        d = 0
        if self.equipament['offhand'] == 'heavyweapon' or self.equipament['offhand'] == 'empty':
            d = 8
        return a + b + c + d
    def CT(self):
        call = getattr(Power, str(self.useskill))
        a = self.mod('ct')
        c = self.mod('int')/5
        d = a + c
        b = call(self, self.target).CT
        return round(b * (1-d/100),2)
    @property
    def CRIT(self):
        a = 15
        b = self.mod('anatomy')/5
        c = self.mod('crit')
        return a+b+c
    @property
    def RESILIENCE(self):
        a = 5
        b = self.mod('resilience')
        c = self.mod('parry')/5
        return a + b + c
    @property
    def DAMAGE_AT(self):
        a = self.mod('armslore')/5
        b = self.mod('damage')
        return a + b
    @property
    def FORTITUDE(self):
        a = self.mod('parry')/5
        b = self.mod('vit')/5
        c = self.mod('fortitude')
        return a + b + c
    def DAMAGE_AE(self,atr):
        a = self.mod('lore')/5
        b = self.mod('ae_damage')
        c = self.mod(atr)/5
        return a + b
    @property
    def REFLEX(self):
        a = self.mod('resistspells')/5
        b = self.mod('int')/5
        c = self.mod('tactics')
        return a + b + c
    @property
    def cast(self):
        call = getattr(Power,str(self.useskill))
        call(self, self.AE_target).use()
    @property
    def COUNTER_RATING(self):
        a = self.equipament['mainhand'].wep_atr['counterrating']
        b = self.mod('counterrating')
        return a + b
    
    #[0,1,'string',5]
    #[0,1,'string',5,'string2',1]
    def mod(self,str,value = None):
        if value != None:
            setattr(self,str,getattr(self,str)+value)
        else:
            if hasattr(self,str):
                a = getattr(self,str)
            else:
                a = 0
            b = 0
            c = 0
            if self.bonus_E.has_key(str):
                b += self.bonus_E[str]
            for enc in self.bonus_T:
                if enc.has_key(str):
                    c += enc[str]
            
            return  a+ b + c
            
    class Unarmed:
        def __init__(self,skillnv,enchant):
            self.enchant = enchant
            for bon in self.enchant.keys():
                if bon == 'damage' or bon == 'AT':
                  
                    continue
                self.enchant[bon] *= 2
            self.enchant['damage'] = skillnv * 12
            self.wep_atr = {}
            for key, atr in wep_size_info['unarmed'].items():                                                                                                                                                                     
                self.wep_atr[key] = atr
            self.wep_skills = {'atkskill':'wrestling','atkatr':'str','danoatr':'str'} 
    @property
    def def_AT(self):
        conds = []
        for arg in self.AI_AT:
            conds.append(arg)
        for x in conds:
            call = getattr(Test,x[1])
            if call(*x):
                self.AT_target = call(*x)[1]
            else:
                check = False
                while check == False:
                    self.AT_target = Test.random_tar(*x)[1]
                    if len(Test.random_tar(*x)[1]) == 0:
                        check = True
                    if self.AT_target[0].ALIVE:
                        check = True
        return 0
    @property
    def defpower(self):
    #[life, '<', 50, allies, 1 target,skill]
        conds = []
        for arg in self.AI:
            conds.append(arg)        
        for x in conds:
            #teste = Test(*conds[h:h+6])
            call = getattr(Test,x[1])
            if call(*x):
                self.useskill = x[6]
                self.AE_target = call(*x)[1]
                return self.CT()
        self.useskill = 'Wait'
        self.AE_target = []
        return 0
    @property    
    def active_checker(self):
        if self.LIFE <= 0 or self.effects.has_key('stunned') or self.effects.has_key('sleeping'):
            return False
        else:
            return True
    def order(self,value = None):
        if self.active_checker:  
            if value == None:
                '''define the Power, the target and the casting time'''
                self._attack_spec_order = self.defpower
                '''define the attack order'''
                self._attack_order = []
                self._attack_order.append(self.AS('mainhand'))
                if hasattr(self.equipament['offhand'],'weapons'):
                    self._attack_order.append(self.AS('offhand'))
            else:
                '''faz passar o tempo para esse personagem, e 
                vefirica se esta na hora de atacar ou nao'''
                for atk in range(len(self._attack_order)):
                    self._attack_order[atk] = round(self._attack_order[atk]-value,2)
                    
                    #print atk
                self._attack_spec_order = round(self._attack_spec_order - value,2)
                #time.sleep(0.1)
                if self._attack_order[0] <= 0:
                    self.attack('mainhand')
                    self._attack_order[0] += self.AS('mainhand')
                if hasattr(self.equipament['offhand'],'weapons'):
                    if self._attack_order[1] <= 0:
                        self.attack('offhand')
                        self._attack_order[1] += self.AS('offhand')
                if self._attack_spec_order <= 0:
                    self.cast
                    self._attack_spec_order += self.defpower
    def attack(self,hand):
        time.sleep(1)
        if self.target == None:
            self.def_AT
            comparare = [[char, char.risk_lv] for char in self.AT_target]
            compare =  max(comparare, key=lambda x:x[1])
            target = compare[0]
        else:
            target = self.target
        crit = False
        hit = False
        counter = False
        z = random.randint(1,100)
        a = self.AT(self.equipament['mainhand'])
        b = target.EVD
        if z + a - b >= 100 - (self.CRIT-target.RESILIENCE):
            crit = True
        if z + a - b >= 20:
            hit = True
        if z + a - b <= target.mod('counterrating'):
            counter = True
        if counter:
            d = target.main_damage(self)
            print 'Counter attack!!!---', self.name , 'received', d,'damage'
            self.LIFE -= d
            print self.name, 'has', self.LIFE, 'of life'
        if hit:
            d = self.main_damage(target)
            str = 'Hit!!!----'
            if crit:
                str =  'Crit!!!----'
                d *= 2
            target.LIFE -= d
            print str, self.name, 'caused', d, 'damage to', target.name, target.LIFE_PERCENT
            print target.name, 'has', target.LIFE, 'of life', target.LIFE_PERCENT,'%','\n'
        if hit == False:
            print self.name, 'Missed'
    def main_damage(self,target):                                                                                                                                                                                                                      
        wep = self.equipament['mainhand']                                                                                                                                                                                                
        a = random.randint(wep.wep_atr['danomin'],wep.wep_atr['danomax']) 
        a = (wep.wep_atr['danomin']+wep.wep_atr['danomax'])/2
        b = wep.wep_atr['dano_mult']*(self.mod(wep.wep_skills['atkskill'])/5+self.DAMAGE_AT-target.FORTITUDE)                                                                       
        c = wep.wep_atr['atr_mult']*self.mod(wep.wep_skills['danoatr'])/5*2                                                                                                                                               
        d = target.mod('prot')-wep.wep_atr['armor_pen']-self.mod('armor_pen')
        if d < 0: d = 0
        f = a+b+c-d
        if f < 0:
            return 0
        return f                                                                                                                                                                                                                    
            

class Testchar(Char):
    def __init__(self,nv,sizeweapon,armortype, weapontype = None):
        Char.__init__(self,nv)
        self.nv = nv
        for atr in C.atr_list:
            self.mod(atr,5*self.nv)
        for skill in C.skills_list:
            self.mod(skill,5*self.nv)
        self.bonus = {}
        weapon = I.T_weapon(nv, sizeweapon)
        armor = I.T_armor(nv,armortype)
        weapon.equipmain(self)
        armor.equip(self)
        self.LIFEMAX
    def main_damage(self,target):
        wep = self.equipament['mainhand']                                                                                                                                                                                                
        a = random.randint(wep.wep_atr['danomin'],wep.wep_atr['danomax']) 
        a = (wep.wep_atr['danomin']+wep.wep_atr['danomax'])/2
        b = wep.wep_atr['dano_mult']*(self.mod(wep.wep_skills['atkskill'])/5+self.DAMAGE_AT-target.FORTITUDE)                                                                       
        c = wep.wep_atr['atr_mult']*(self.mod(wep.wep_skills['danoatr'])/5*2)                                                                                                                                               
        d = target.mod('prot')-wep.wep_atr['armor_pen']-self.mod('armor_pen')
        if d < 0: d = 0                                                                                                                                             
        return (a+b+c-d)
        #/(60/self.equipament['mainhand'].wep_atr['ASbase'])

class Player(Char):
    def __init__(self,name,nv,str,agi,vit,wis,int,skill1,value1,skill2,value2):
        Char.__init__(self,nv)
        #Atributes
        for atr in C.atr_list:
            setattr(self,atr,0)                                                                                                                                                                                                 
        #Skills                                                                                                                                                                                                                   
        for skill in C.skills_list:
            setattr(self,skill,0)
        self.str += str
        self.agi += agi
        self.vit += vit
        self.wis += wis
        self.int += int
        setattr(self,skill1,getattr(self,skill1)+value1)
        setattr(self,skill2,getattr(self,skill2)+value2)
    def force_target(self,target = None):
        if target == None:
            self.target = None
        else:
            self.target = target
        
class Monster(Char):
    def __init__(self,name,nv):
        #Char.__init__(self,nv)
        super(Monster,self).__init__(nv)
        self.name = name
        for atr in C.atr_list:
            self.mod(atr,1+5*self.nv)
        for skill in C.skills_list:
            self.mod(skill,1+5*self.nv)
    @classmethod                                                                                                                                                                                                                           
    def brute(cls,name,nv):                                                                                                                                                                                                               
        brute = cls(name,nv)
        best_atr = ['vit','str']
        best_skill = ['swordmanship','heavyweaponship','fencing','anatomy','armslore','military']
        for x in C.atr_list:                                                                                                                                                                                                         
            if x in best_atr:                                                                                                                                                                                                  
                brute.mod(x,F.randATR(brute.nv))                                                                                                                                                                                           
            else:                                                                                                                                                                                                                          
                brute.mod(x,F.randatr(brute.nv))                                                                                                                                                                                          
        for x in C.skills_list:                                                                                                                                                                                                            
            if x in best_skill:
                brute.mod(x,F.randSKILL(brute.nv))                                                                                                                                                                                            
            else:                                                                                                                                                                                                                          
                brute.mod(x,F.randskill(brute.nv))
        brute.SPMAX
        brute.LIFEMAX
        brute.STAMINMAX
        #criar arma principal
        categoria = random.choice(['cutting','smashing','piercing'])
        size = 'heavy'
        arma = random.choice(C.weapons[categoria][size].keys())        
        mainhand = I.Weapon(nv,categoria,size,arma)                                                                                                                                      
        offhand = '2handed'                                                                                                                                                                                                            
         
        #criar armadura
        armor = I.Armor(nv,'medium')
        armor.equip(brute)
        mainhand.equipmain(brute)
        brute.LIFEMAX
        brute.AI = [[brute,'SP','<=',20,'self',1,'Meditation'],[brute,'life', '<=', 80, 'monsters', 1, 'Heal'],[brute,'life', '<=',100,'allies',1,'Power_Attack']]
        brute.AI_AT = [[brute,'armor','','heavy','allies',1,'AT'],[brute,'life','<=',100,'allies',1,'AT']]
        return brute
    @classmethod                                                                                                                                                                                                                           
    def t_play(cls,name,nv):                                                                                                                                                                                                               
        t_play = cls(name,nv)
        best_atr = ['vit','str']
        best_skill = ['swordmanship','heavyweaponship','fencing','anatomy','armslore','military']
        for x in C.atr_list:                                                                                                                                                                                                         
            if x in best_atr:                                                                                                                                                                                                  
                t_play.mod(x,F.randATR(t_play.nv))                                                                                                                                                                                           
            else:                                                                                                                                                                                                                          
                t_play.mod(x,F.randatr(t_play.nv))                                                                                                                                                                                          
        for x in C.skills_list:                                                                                                                                                                                                            
            if x in best_skill:
                t_play.mod(x,F.randSKILL(t_play.nv))                                                                                                                                                                                            
            else:                                                                                                                                                                                                                          
                t_play.mod(x,F.randskill(t_play.nv))
        t_play.SPMAX
        t_play.LIFEMAX
        t_play.STAMINMAX
        #criar arma principal
        categoria = random.choice(['cutting','smashing','piercing'])
        size = 'heavy'
        arma = random.choice(C.weapons[categoria][size].keys())        
        mainhand = I.Weapon(nv,categoria,size,arma)                                                                                                                                      
        offhand = '2handed'                                                                                                                                                                                                            
         
        #criar armadura
        armor = I.Armor(nv,'medium')
        armor.equip(t_play)
        mainhand.equipmain(t_play)
        t_play.LIFEMAX
        t_play.AI = [[t_play,'SP','<=',20,'self',1,'Meditation'],[t_play,'life', '<=', 80, 'allies', 1, 'Heal'],[t_play,'life', '<=',100,'monsters',1,'Power_Attack']]
        t_play.AI_AT = [[t_play,'armor','','heavy','monsters',1,'AT'],[t_play,'life','<=',100,'monsters',1,'AT']]
        return t_play