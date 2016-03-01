#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

import random
from conf import const as C

magicoffhand = {'evade':1,'AE':1,'AS':1,'crit':1,'resil':1,}
wep_enchant_range = {'well made':6,'masterpiece':5,'magic':4,'enhanced':3,'rare':2,'legendary':1}

class Item(object):
    item_cat = ['broken','half broken','deficient','poor','inferior','moderated',
                'acceptable','common','fine','good','useful','fency','superior',
                'excelent','admirable','splendid','extraordinary','awesome','best','first-class']
    item_value = [4,8,12,16,20,40,60,80,100,120,220,320,420,520,620,1120,1620,2120
                    ,2620,3120,5620,8120,10620,13120,15620,28120,40620,53120,65620
                    ,78120]
    def __init__(self,nv):
        self.nv = nv
        self.cat = self.item_cat[nv-1]
        self.base_value = self.item_value[nv-1]
class Equipable(Item):
    def __init__(self,nv):

        super(Equipable,self).__init__(nv)
        self.enchant = {}
    def rand_bonus_equip(self,nv,x):
        b = nv/2*x
        for j in range(b):
            b += random.randint(-1,1)
        return b
    def selfequip(self,char,slot):

        if slot in self.equipable_slot:
            char.equipament[slot] = self
            for bon in self.enchant.keys():
                char.bonus_E[bon] = char.bonus_E.get(bon,0) + self.enchant[bon]
        else:
            print 'This item cannot be equipped in this slot'
            #rodar função do inventorio de voltar o item para o slot
    def det_enchant(self,dict_slot,r,save= None):
        enchant = dict(dict_slot)
        for x in range(r-1):
            y = enchant.keys()
            if save != None: y.pop(y.index(save))
            enchant.pop(random.choice(y),None)
        for z,y in enchant.items():
            self.enchant[z] = self.enchant.get(z,0) + enchant[z]
    def det_cond(self,mf=0):
        roll = random.randint(1,10000)
        if roll+mf/10 >= 9999:
            self.cond = 'legendary'
        elif roll+mf >= 9989:
            self.cond = 'rare'
        elif roll+mf >= 9889:
            self.cond = 'enhanced'
        elif roll+mf >= 9389:
            self.cond = 'magic'
        elif roll+mf >= 8389:
            self.cond = 'masterpiece'
        elif roll+mf >= 6889:
            self.cond = 'wellmade'
        else:
            self.cond = 'normal'
    def det_weak(self,list):
        self.enchant[list[0]] = self.enchant.get(list[0],0) - 5
        self.enchant[list[1]] = self.enchant.get(list[1],0) + 5
class Weapon(Equipable):
    wep_type = {'cutting':{'atkskill':'swordmanship','atkatr':'str','danoatr':'str'},
            'smashing':{'atkskill':'heavyweaponship','atkatr':'str','danoatr':'str'},
            'piercing':{'atkskill':'fencing','atkatr':'agi','danoatr':'agi'},
            'ranged':{'atkskill':'archery','atkatr':'agi','danoatr':'agi'},
            'thrown':{'atkskill':'archery','atkatr':'agi','danoatr':'str'},
            'catalyst':{'atkskill':'magery','atkatr':'wis','danoatr':'wis'}}
    weapons = {'catalyst':{'heavy':{'staff':'normal'},'medium':{'rod':'normal'},'light':{'wand':'normal','orb':'normal'}},
            'cutting':{'medium':{'longsword':'normal'},'light':{'dagger':'normal'},'heavy':{'Great Axe':'normal'}},
            'smashing':{'light':{'hammer': 'normal'},'medium':{'morningstar': 'normal'},'heavy':{'maul': 'normal'}}
            ,'piercing':{'light':{'dagger':'normal'},'medium':{'rapier':'normal'},'heavy':{'war pickaxe':'normal'}}}
    wep_size_info = {'light':{'ASbase':2.5,'danomin':8,'danomax':18,'modataque':0,
            'dano_mult':1.0,'atr_mult':0.5,'counterrating':15,'armor_pen':0},
        'medium':{'ASbase':5.0,'danomin':8,'danomax':18,'modataque':0,'dano_mult':1.5,
            'atr_mult':1,'counterrating':10,'armor_pen':0},
        'heavy':{'ASbase':15.0,'danomin':8,'danomax':18,'modataque':8,'dano_mult':2.0,
           'atr_mult':3,'counterrating':5,'armor_pen':5}}
    wep_enchants = {'as':1,'resil':1,'crit':1,'AE':1,'evade':1,'damage':8,'AT':1}
    equipable_slot = ['mainhand','offhand']
    def __init__(self,nv,type = None,size = None,weapon = None, mf = 0):
        super(Weapon,self).__init__(nv)
        if type == None:
            self.type = random.choice([cat for cat in C.defenses_list if cat != 'magic'])
        else:
            self.type = type
        if size == None:
            self.size = random.choice(self.wep_size_info.keys())
        else:
            self.size = size
        if weapon == None:
            self.weapon = random.choice(self.weapons[self.type][self.size].keys())
        else:
            self.weapon = weapon
        '''pegar atributos de acordo com a arma'''
        self.wep_atr = {}
        for key, atr in C.wep_size_info[self.size].items():
            self.wep_atr[key] = atr
        '''pegar skills e atr usados pelo personagem para ataque com a arma'''
        self.wep_skills = {}
        for key, s in C.wep_type[self.type].items():
            self.wep_skills[key] = s
        '''jogar porcentagem para determinar a condição mágica da arma'''
        self.det_cond(mf)
        if self.cond == 'Legendary':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        elif self.cond == 'rare':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        elif self.cond == 'enhanced':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        elif self.cond == 'magic':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        elif self.cond == 'masterpiece':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        elif self.cond == 'well made':
            self.det_enchant(self.wep_enchants,wep_enchant_range[self.cond],'damage')
        else:
            self.enchant = {'damage':4}
        for x in self.enchant.keys():
            self.enchant[x] += self.rand_bonus_equip(nv,self.enchant[x])
        self.wep_atr['armor_pen'] *= self.nv
    def equipmain(self,char):
        self.selfequip(char,'mainhand')
        if self.size == 'heavy':
            char.equipament['offhand'] = 'heavyweapon'
    def equipoff(self,char):
        if self.size != 'heavy':
            self.selfequip(char,'offhand')
        else:
            print 'This weapon is too heavy to be equipped on your offhand'
class Armor(Equipable):
    armors = {'light':{'cloth':['smashing','piercing'],'robe':['cutting','smashing'], 'leather':['piercing','cutting']},
            'medium': {'studded leather':['cutting','smashing'],'chain mail':['smashing','piercing'],'half plate':['piercing','cutting']},
            'heavy':{'scale armor':['cutting','smashing'],'fullplate':['smashing','piercing'],'splint mail':['piercing','cutting']}}
    armorstype = {'None': {'prot':0,'evade':5},'light': {'prot':1,'evade':0},'medium':{'prot':6,'evade':-6},'heavy':{'prot':11,'evade':-19}}
    armor_enchants = {'bonus':{'evade':1,'resil':1,'fortitude':1,'magicred':5},
                'resist':{'stun':2,'weakness':2,
                    'slow':2,'blindness':2,'curse':2},
                'defense':{'cutting':1,'smashing':1,'piercing':1,'spell':1}}
    equipable_slot = ['armor']
    def __init__(self,nv,type = None,armor = None, mf = 0):
        super(Armor,self).__init__(nv)
        self.type = type
        if type == None:
            self.type = random.choice(self.armors.keys())
            print self.type
        self.armor = armor
        if armor == None:
            self.armor = random.choice(self.armors[self.type].keys())
        self.det_cond(mf)
        if self.cond == 'Legendary':
            self.det_enchant(self.armor_enchants['bonus'],1)
            self.det_enchant(self.armor_enchants['resist'],1)
            self.det_enchant(self.armor_enchants['defense'],2)
        elif self.cond == 'rare':
            self.det_enchant(self.armor_enchants['bonus'],2)
            self.det_enchant(self.armor_enchants['resist'],2)
            self.det_enchant(self.armor_enchants['defense'],2)
        elif self.cond == 'enhanced':
            self.det_enchant(self.armor_enchants['bonus'],2)
            self.det_enchant(self.armor_enchants['resist'],3)
            self.det_enchant(self.armor_enchants['defense'],3)
        elif self.cond == 'magic':
            self.det_enchant(self.armor_enchants['bonus'],2)
            self.det_enchant(self.armor_enchants['resist'],4)
            self.det_enchant(self.armor_enchants['defense'],3)
        elif self.cond == 'masterpiece':
            self.det_enchant(self.armor_enchants['bonus'],3)
            self.det_enchant(self.armor_enchants['resist'],4)
            self.det_enchant(self.armor_enchants['defense'],4)
        elif self.cond == 'well made':
            self.det_enchant(self.armor_enchants['bonus'],3)
            self.det_enchant(self.armor_enchants['resist'],5)
            self.det_enchant(self.armor_enchants['defense'],4)
        else:
            self.enchant = {}
        self.enchant['prot'] = self.armorstype[self.type]['prot']
        self.enchant['evade'] = self.armorstype[self.type]['evade']
        for x in self.enchant.keys():
            self.enchant[x] += self.rand_bonus_equip(nv,self.enchant[x])
        self.det_weak(self.armors[self.type][self.armor])
    def equip(self,char):
        self.selfequip(char,'armor')
class Glove(Equipable):
    gloves_enchants = {'AT':1,'AE':1,'AS':1,'crit':1,'stareg':1}
    gloves_type = {'cloth':['cutting','smashing'],'leather':['smashing','piercing'],'metal':['piercing','cutting']}
    equipable_slot = ['gloves']
    def __init__(self,nv,type = None,mf = 0):
        super(Glove,self).__init__(nv)
        if type == None:
            self.type = random.choice(self.gloves_type.keys())
        self.det_cond(mf)
        if self.cond == 'legendary':
            self.det_enchant(self.gloves_enchants,0)
        elif self.cond == 'enhanced':
            self.det_enchant(self.gloves_enchants,1)
        elif self.cond == 'magic':
            self.det_enchant(self.gloves_enchants,2)
        elif self.cond == 'masterpiece':
            self.det_enchant(self.gloves_enchants,3)
        elif self.cond == 'well made':
            self.det_enchant(self.gloves_enchants,4)
        elif self.cond == 'normal':
            self.det_enchant(self.gloves_enchants,5)
        for x in self.enchant.keys():
            self.enchant[x] += self.rand_bonus_equip(nv,self.enchant[x])
        self.det_weak(self.gloves_type[self.type])

class Head(Equipable):
    heads_enchants = {'bonus':{'evade':1,'resil':1,'fortitude':1},
                        'defense':{'cutting':1,'smashing':1,'piercing':1,'spell':1},
                        'resist':{'stun':2,'weakness':2,'slow':2,'blindness':2,'curse':2}}
    heads_type = {'cloth':['cutting','smashing'],'leather':['smashing','piercing'],'metal':['piercing','cutting']}
    equipable_slot = ['head']
    def __init__(self,nv,type = None,mf = 0):
        super(Head,self).__init__(nv)
        if type == None:
            self.type = random.choice(self.heads_type.keys())
        self.det_cond(mf)
        if self.cond == 'legendary':
            self.det_enchant(self.heads_enchants['bonus'],0)
            self.det_enchant(self.heads_enchants['resist'],1)
            self.det_enchant(self.heads_enchants['defense'],2)
        elif self.cond == 'enhanced':
            self.det_enchant(self.heads_enchants['bonus']  ,1)
            self.det_enchant(self.heads_enchants['resist'] ,2)
            self.det_enchant(self.heads_enchants['defense'],2)
        elif self.cond == 'magic':
            self.det_enchant(self.heads_enchants['bonus']  ,1)
            self.det_enchant(self.heads_enchants['resist'] ,3)
            self.det_enchant(self.heads_enchants['defense'],3)
        elif self.cond == 'masterpiece':
            self.det_enchant(self.heads_enchants['bonus']  ,2)
            self.det_enchant(self.heads_enchants['resist'] ,4)
            self.det_enchant(self.heads_enchants['defense'],3)
        elif self.cond == 'well made':
            self.det_enchant(self.heads_enchants['bonus']  ,2)
            self.det_enchant(self.heads_enchants['resist'] ,4)
            self.det_enchant(self.heads_enchants['defense'],4)
        elif self.cond == 'normal':
            self.det_enchant(self.heads_enchants['bonus']  ,2)
            self.det_enchant(self.heads_enchants['resist'] ,5)
            self.det_enchant(self.heads_enchants['defense'],4)
        for x in self.enchant.keys():
            self.enchant[x] += self.rand_bonus_equip(nv,self.enchant[x])
        self.det_weak(self.heads_type[self.type])
class Boots(Equipable):
    boots_enchants = {'AT':1,'AE':1,'AS':1,'crit':1,'stareg':1,'counterrating':1}
    boots_type = {'cloth':['cutting','smashing'],'leather':['smashing','piercing'],'metal':['piercing','cutting']}
    equipable_slot = ['boots']
    def __init__(self,nv,type = None,mf = 0):
        super(Boots,self).__init__(nv)
        if type == None:
            self.type = random.choice(self.boots_type.keys())
        self.det_cond(mf)
        if self.cond == 'legendary':
            self.det_enchant(self.boots_enchants,0)
        elif self.cond == 'enhanced':
            self.det_enchant(self.boots_enchants  ,1)
        elif self.cond == 'magic':
            self.det_enchant(self.boots_enchants  ,1)
        elif self.cond == 'masterpiece':
            self.det_enchant(self.boots_enchants  ,2)
        elif self.cond == 'well made':
            self.det_enchant(self.boots_enchants  ,2)
        elif self.cond == 'normal':
            self.det_enchant(self.boots_enchants  ,2)
        for x in self.enchant.keys():
            self.enchant[x] += self.rand_bonus_equip(nv,self.enchant[x])
        self.det_weak(self.boots_type[self.type])
class T_armor(Armor):
    def __init__(self,nv,cat):
        self.nv = nv
        self.cat = cat
        self.enchant = {}
        #pega atributos base da armadura
        for key, atr in self.armorstype[cat].items():
            self.enchant[key] = atr
        self.enchant['prot'] *= self.nv
class T_weapon(Weapon):
    def __init__(self,nv,size,categoria = None):
        self.nv = nv
        self.categoria = categoria
        self.size = size
        if categoria == None:
            self.categoria = random.choice(['cutting','smashing','piercing'])
        '''pegar atributos de acordo com a arma'''
        self.wep_atr = {}
        for key, atr in self.wep_size_info[self.size].items():
            self.wep_atr[key] = atr
        '''pegar skills e atr usados pelo personagem para ataque com a arma'''
        self.wep_skills = {}
        for key, s in self.wep_type[self.categoria].items():
            self.wep_skills[key] = s
        self.enchant = {'damage':10*self.nv,'AS':2*self.nv}
        self.wep_atr['armor_pen'] *= self.nv
if __name__ == '__main__':

    a = Weapon(10)
    c = Armor(10)
    g = Glove(10)
    h = Head(10)
    boots = Boots(10)
    print a.base_value
    b = R.Char(1)
    a.selfequip(b,'mainhand')
    c.selfequip(b,'armor')
    g.selfequip(b,'hand')
    h.selfequip(b,'head')
    boots.selfequip(b,'boots')
    #print b.equipament['mainhand'].enchant
    #print b.equipament['mainhand'].weapon
    #print b.equipament['mainhand'].size
    #print b.equipament['mainhand'].type
    #print b.equipament['mainhand'].cond
    print b.equipament['armor'].enchant
    print b.equipament['armor'].armor
    print b.equipament['armor'].type
    print b.equipament['armor'].cond
    print b.equipament['hand'].cond
    print b.equipament['hand'].type
    print b.equipament['hand'].enchant
    print b.equipament['head'].cond
    print b.equipament['head'].type
    print b.equipament['head'].enchant
    print b.equipament['boots'].type
    print b.equipament['boots'].enchant
    print b.bonus_E
