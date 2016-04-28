#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import char as C
from constants import attributes as A
import auxiliary
import effects
import items
import powers
import spells
import dice

class Char(object):
    ''' Base class for any item in the game '''

    def __init__(self,*args, **kwargs):
        '''
        Initializes the class.
        arguments:
            name: char name

            lvl: char level

            attributes: char attributes ('Attribute' object)

            skills: char skills ('Skill' object)

            defenses: char defenses ('Defense' object)

            resists: char resists ('Resist' object)

            equipment: char equipment (dict, values are 'Item' objects)

            inventory: char inventory ('Inventory' object)

            effects: char effects (dict, values are 'Effects' objects)

            powers: char powers (dict, values are 'Power' objects)

            spells: char spells (dict, values are 'Spells' objects)

            bonuses: char bonuses (dict, 'keys' are bonus type, values are the bonus)

            life: char life - if not specified it's set with char's attributes

            SP: char SP - if not specified it's set with char's attributes

            ST: char ST - if not specified it's set with char's attributes
        '''
        #start bonuses dict
        self.bonuses = {}
        # handles positional
        # handles kwargs
        for arg_name in C.args_list:
            if arg_name in kwargs:
                if arg_name in C.properties:
                    setattr(self, 'max'+arg_name, kwargs[arg_name])
                    setattr(self, '_'+arg_name, kwargs[arg_name])
                if arg_name == 'bonuses':
                    for bon in C.bonuses:
                        if kwargs[arg_name].has_key(bon):
                            self.bonuses[bon] = kwargs[arg_name][bon]
                if arg_name in C.stats:
                    setattr(self,'_'+arg_name+'_bonus', kwargs[arg_name])
                if arg_name not in list(set(C.properties) | set(C.bonuses) | set(C.stats)):
                    setattr(self, arg_name, kwargs[arg_name])
            else:
                if arg_name in C.properties:
                    setattr(self, 'max'+arg_name, None)
                    setattr(self, '_'+arg_name, None)
                if arg_name in C.stats:
                    setattr(self,'_'+arg_name+'_bonus', 0)
                if arg_name not in list(set(C.properties) | set(C.bonuses) | set(C.stats)):
                    setattr(self, arg_name, None)
        for bon in C.bonuses:
            if not self.bonuses.has_key(bon):
                self.bonuses[bon] = {}
        self.lvl = self.lvl or 0

        if 'equipment' in kwargs:
            self.equipment = kwargs['equipment']
        else:
            self.equipment = None

        self.calculate_stats()
        self._life = self.life if self.life is not None else self.maxlife
        self._sp = self.sp if self.sp is not None else self.maxSP
        self._st = self.st if self.st is not None else self.maxST
        self._update_bonus()

    def __repr__(self):
        string = 'char: {0}\nlife: {1} MP: {2}'.format(self.name, self.life, self.sp)
        if self.effects:
            string += '\neffects: {0}\n'.format(self.effects.keys())
        return string

    def calculate_stats(self):

        self.maxlife = C.LIFE_BASE + self.attributes.vitality_mod()*10 + self._life_bonus
        self.maxSP = C.SP_BASE + self.attributes.intuition_mod()
        self.maxST = C.ST_BASE + self.attributes.vitality_mod()/2+self.skills.meditating()/2

    @property
    def life(self):
        '''
        base life
        '''
        return self._life
    @life.setter
    def life(self, value):
        self._life = value
        if self._life > self.maxlife:
            self._life = self.maxlife
        self._life = 0 if self._life < 0 else self._life
        self._alive = True if self._life > 0 else False
    @property
    def life_percent(self):
        '''
        base life in percentage
        interval: 0 - 1
        '''
        return self._life/self.maxlife if self.maxlife > 0 else 0
    @life_percent.setter
    def life_percent(self, value):
        self.life = int(round(value*self.maxlife))
        self._alive = True if self._life > 0 else False

    # SP property
    @property
    def sp(self):
        '''
        base SP
        '''
        return self._sp
    @sp.setter
    def sp(self, value):
        value = self.maxSP if value > self.maxSP else value
        self._sp = value
    @property
    def sp_percent(self):
        '''
        base SP in percentage
        interval: 0 - 1
        '''
        return self._sp/self.maxSP if self.maxSP > 0 else 0
    @sp_percent.setter
    def sp_percent(self, value):
        self._sp = int(round(value*self.maxSP))

    # ST property
    @property
    def st(self):
        '''
        base ST
        '''
        return self._st
    @st.setter
    def st(self, value):
        value = self.maxST if value > self.maxST else value
        self._st = value
    @property
    def st_percent(self):
        '''
        base ST in percentage
        interval: 0 - 1
        '''
        return self._st/self.maxST if self.maxST > 0 else 0
    @st_percent.setter
    def st_percent(self, value):
        self._st = int(round(value*self.maxST))



    def equip(self, item, slot):
        '''
        Equips the item in the slot
        '''
        self.equipment.equip(item, slot)
        self._update_bonus()

    def _update_bonus(self):
        '''
        Method for updating all the bonuses an adding them to their current instances
        '''
        bonus_dict = {}
        for bonus_cat in self.bonuses.values():
            for bonus_name, bonus_value in bonus_cat.items():
                if bonus_name in bonus_dict:
                    bonus_dict[bonus_name] += bonus_value
                else:
                    bonus_dict[bonus_name] = bonus_value
        for equipment_slot, equipment in self.equipment:
            if equipment is not None:
                for bonus_type, bonus_type_value in equipment.bonuses.items():
                    for bonus_name, bonus_value in bonus_type_value.items():
                        if bonus_name in bonus_dict:
                            bonus_dict[bonus_name] += bonus_value
                        else:
                            bonus_dict[bonus_name] = bonus_value
        for bonus_name, bonus_value in bonus_dict.items():
            if bonus_name in auxiliary.A.attributes_list:
                setattr(self.attributes, '_'+bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.S.skills_list:
                setattr(self.skills, '_'+bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.D.defenses_list:
                setattr(self.defenses, '_'+bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.R.resists_list:
                setattr(self.resists, '_'+bonus_name+'_bonus', bonus_value)
            elif bonus_name in C.stats:
                setattr(self, '_'+bonus_name+'_bonus', bonus_value)

    def run_effects(self):
        '''
        Runs the effects in the effects dict
        '''
        for effect_name, effect in self.effects.items():
            effect(self)

    def calculate_bonus(self):
        '''
        Calculates all the bonuses and add them to it's corresponding object
        '''

    @property
    def evade(self):
        return (C.EVASION_BASE + self.skills.reflex() +
                self.attributes.agility() + self._evasion_bonus +
                self.equipment.armor.evasion)
    def attack(self,weapon=None):
        attk_sk = getattr(self.skills,weapon.attk_skill)()
        attk_attr = getattr(self.attributes,weapon.attk_attr)()
        attk_bon = self._attack_bonus
        attk_wep = weapon.attk_bonus
        return attk_sk + attk_attr + attk_bon + attk_wep
    @property
    def protection(self):
        return self._protection_bonus #*(1+( self.equipment.armor.prot_mod*self.attributes.vitality_mod()/100.0))
    def armor_penetration(self,weapon):
        return weapon.armor_penetration + self._armor_penetration_bonus

    def special_attack(self,attr,skill):
        return self.special_attack_bonus + getattr(self.attributes,skill+'_mod') # add bonus do char

    # def CT(self):
    #     call = getattr(Power, str(self.useskill))
    #     a = self.mod('ct')
    #     c = self.mod('int')/5
    #     d = a + c
    #     b = call(self, self.target).CT
    #     return round(b * (1-d/100),2)

    @property
    def critical(self):
        return C.CRIT_BASE + self.skills.anatomy_mod() + self._critical_bonus
    @property
    def critical_damage(self):
        return (self._critical_damage_bonus+100.0)/100.0
    @property
    def RESILIENCE(self):
        return C.RESILIENCE_BASE + self.skills.parry_mod() + self._resilience_bonus

    @property
    def at_damage_mod(self):
        return self.skills.armslore_mod()*2 + self._at_damage_bonus

    @property
    def fortitude(self):
        return self.skills.parry_mod() + self.attributes.vitality_mod() + self._fortitude_bonus

    def sa_damage_mod(self, attr):
        return self.skills.lore() + getattr(self.attributes,attr)() # what is atr?+

    @property
    def reaction(self):
        return self.attributes.intuition() + self.skills.tactics # + resistspells

    @property
    def cast(self):
        call = getattr(Power,str(self.useskill))
        call(self, self.AE_target).use()

    @property
    def counter(self):
        a = self.equipment.mainhand.counter
        b = self._counter_bonus
        #parry?
        return a + b

    @classmethod
    def blank(cls, name, *args, **kwargs):
        '''
        Creates a blank char with 0 in all stats
        '''
        blank = {
            'lvl': 0,
            'attributes': auxiliary.Attributes(),
            'skills': auxiliary.Skills(),
            'defenses': auxiliary.Defenses(),
            'resists': auxiliary.Resists(),
            'equipment': auxiliary.Equipment(),
            'inventory': auxiliary.Inventory(0),
            'effects': {},
            'powers': {},
            'spells': {},
            'bonuses': {},
            'life': 0,
            'SP': 0,
            'ST': 0}
        for key, value in kwargs.items():
            if key in blank:
                blank[key] = value
        return cls(name, *args, **blank)

def wrap_bonus(self, *args, **kwargs):
    '''
    Wrapper for updating bonuses when equipping items
    '''

if __name__ == '__main__':
    import items

    Attr1 = auxiliary.Attributes(vitality=10)
    Skill1 = auxiliary.Skills(alchemy=10)
    Def1 = auxiliary.Defenses(cutting=10)
    Res1 = auxiliary.Resists(weakness=10)
    #Armor1 = items.Equipable.Armor('red_chainmail', bonuses={'strength': 10})
    Equ1 = auxiliary.Equipment()
    Eff1 = {'poisoned': effects.Effects.poisoned}
    Pow1 = {}
    Spell1 = {}
    Bonus1 = {'innate':{'wisdom':50}}

    char1 = Char(name='bob', lvl=1, attributes=Attr1, skills=Skill1, defenses=Def1,
                    resists=Res1, effects=Eff1, equipment=Equ1, powers=Pow1, spells=Spell1, bonuses=Bonus1)
    print char1.bonuses
    var = vars(char1)
    for a in var:
        print a
    # run poison effect
    print char1, 'before poison'
    char1.run_effects()
    print char1, 'after poison'
    blank_char = Char.blank(name='boris')
    print blank_char
    blank_char
    print char1.attributes.roll('vitality'), 'roll vit'
    print char1.skills.roll('alchemy'), 'roll alchemy'
    print char1.defenses.roll('cutting'), 'roll cutting'
    print char1.resists.roll('weakness'), 'roll weakness'
    print
    print 'Roll without bonus'
    print char1.attributes.roll('strength'), 'roll str'
    print 'Equip armor with bonus and roll again'
    #char1.equip(Armor1, 'armor')
    # print char1.equipment.armor.bonuses
    # print char1.equipment
    print char1.attributes.roll('strength'), 'roll str'
    var = vars(char1)
    for item in var.items():
        print item
    print
    print
    print
    char1.attributes._agility = 10
    char1.attributes.agility_bonus = 10
    print char1.attributes.agility()
    print char1.attributes._agility
    print char1.bonuses
    char1.bonuses['magic']['agility'] = 80
    print char1.bonuses
    char1._update_bonus()
    print char1.attributes.agility()
    quit()
    # print blank_char.attributes
    # print blank_char.attributes._vitality
    # print blank_char.attributes.vitality
    print char1.attributes.vit_mod()
    print char1.maxlife
    print char1.life
    char1.life +=1000
    print char1.life

    char1.calculate_stats()
