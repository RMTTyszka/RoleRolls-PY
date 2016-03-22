#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import char as C
import base
import auxiliary
import effects
import items
import powers
import spells
import dice

class Char(base.Base):
    ''' Base class for any item in the game '''

    def __init__(self, name, **kwargs):
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

            HP: char HP - if not specified it's set with char's attributes

            SP: char SP - if not specified it's set with char's attributes

            ST: char ST - if not specified it's set with char's attributes
        '''
        super(Char, self).__init__(name, **kwargs)
        if 'skills' in kwargs:
            self.skills = kwargs['skills']
        else:
            self.skills = 0

        if 'equipment' in kwargs:
            self.equipment = kwargs['equipment']
        else:
            self.equipment = 0

        self.calculate_stats()
        self._HP = self.HP if self.HP is not None else self.maxHP
        self._SP = self.SP if self.SP is not None else self.maxSP
        self._ST = self.ST if self.ST is not None else self.maxST
        self._update_bonus()

    def __repr__(self):
        string = 'char: {0}\nHP: {1} MP: {2}'.format(self.name, self.HP, self.SP)
        if self.effects:
            string += '\neffects: {0}'.format(self.effects.keys())
        return string

    def calculate_stats(self):
        self.maxHP = C.HP_BASE + self.attributes.vit_mod*10
        self.maxSP = C.SP_BASE + self.attributes.int_mod
        self.maxST = C.ST_BASE + self.attributes.vit_mod/2+self.skills.meditating/2

    def attack(self, enemy):
        '''
        Attacks the enemy, returning the damage and any other penalty
        '''
        pass

    def equip(self, item, slot):
        '''
        Equips the item in the slot
        '''
        self.equipment.equip(item, slot)
        self._update_bonus()

    # def update_bonus(self, ):

    def roll_attr(self, attribute):
        '''
        Makes a roll of the attribute in the argument
        '''
        return dice.roll_01(getattr(self.attributes, attribute))

    def roll_skill(self, skill):
        '''
        Makes a roll of the skill in the argument
        '''
        return dice.roll_01(getattr(self.skills, skill))

    def roll_defense(self, defense):
        '''
        Makes a roll of the defense in the argument
        '''
        return dice.roll_01(getattr(self.defenses, defense))

    def roll_resist(self, resist):
        '''
        Makes a roll of the resist in the argument
        '''
        return dice.roll_01(getattr(self.resists, resist))

    def _update_bonus(self):
        '''
        Method for updating all the bonuses an adding them to their current instances
        '''
        bonus_dict = {}
        for bonus_name, bonus_value in self.bonuses.items():
            if bonus in bonus_dict:
                bonus_dict[bonus] += bonus_value
            else:
                bonus_dict[bonus] = bonus_value
        for equipment_slot, equipment in self.equipment:
            if equipment is not None:
                for bonus_name, bonus_value in equipment.bonuses.items():
                    if bonus_name in bonus_dict:
                        bonus_dict[bonus] += bonus_value
                    else:
                        bonus_dict[bonus_name] = bonus_value
        for bonus_name, bonus_value in bonus_dict.items():
            if bonus_name in auxiliary.A.attributes_list:
                setattr(self.attributes, bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.S.skills_list:
                setattr(self.skills, bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.D.defenses_list:
                setattr(self.defenses, bonus_name+'_bonus', bonus_value)
            elif bonus_name in auxiliary.R.resists_list:
                setattr(self.resists, bonus_name+'_bonus', bonus_value)

    @property
    def EVD(self):
        return self.skills.reflex +self.equipment.evade +self.attributes.agility

    @property
    def PROT(self):
        return self.equipment.prot

    def AT(self,weapon):
        return self.equipament.attk # add bonus do char

    def AE(self,atr,skill):
        return self.equipament.attk # add bonus do char

    # def CT(self):
    #     call = getattr(Power, str(self.useskill))
    #     a = self.mod('ct')
    #     c = self.mod('int')/5
    #     d = a + c
    #     b = call(self, self.target).CT
    #     return round(b * (1-d/100),2)

    @property
    def CRIT(self):
        return C.CRIT_BASE + self.skills.anatomy + self.stats.crit

    @property
    def RESILIENCE(self):
        return C.RESILIENCE_BASE + self.skills.parry #mod resilience? +

    @property
    def DAMAGE_AT(self):
        return self.skills.armslore # + where is the damage?

    @property
    def FORTITUDE(self):
        return self.skills.parry + self.attributes.vitality + self.equipment.fortitude

    def DAMAGE_AE(self, atr):
        return self.skills.lore # what is atr?+

    @property
    def REFLEX(self):
        return self.attributes.inteligence + self.skills.tactics # + resistspells

    @property
    def cast(self):
        call = getattr(Power,str(self.useskill))
        call(self, self.AE_target).use()

    @property
    def COUNTER_RATING(self):

        a = self.equipament['mainhand'].wep_atr['counterrating']
        b = self.mod('counterrating')
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
            'HP': 0,
            'SP': 0,
            'ST': 0}
        for key, value in kwargs:
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
    Armor1 = items.Equipable.Armor('red_chainmail', bonuses={'strength': 10})
    Equ1 = auxiliary.Equipment()
    Eff1 = {'poisoned': effects.Effects.poisoned}
    Pow1 = {}
    Spell1 = {}
    Bonus1 = {}

    char1 = Char(name='bob', lvl=1, attributes=Attr1, skills=Skill1, defenses=Def1, resists=Res1, effects=Eff1, equipment=Equ1, powers=Pow1, spells=Spell1, bonuses=Bonus1)

    # run poison effect
    print char1, 'before poison'
    char1.run_effects()
    print char1, 'after poison'
    blank_char = Char.blank('boris')
    print blank_char
    blank_char
    print char1.roll_attr('vitality'), 'roll vit'
    print char1.roll_skill('alchemy'), 'roll alchemy'
    print char1.roll_defense('cutting'), 'roll cutting'
    print char1.roll_resist('weakness'), 'roll weakness'
    print
    print 'Roll without bonus'
    print char1.roll_attr('strength'), 'roll str'
    print 'Equip armor with bonus and roll again'
    char1.equip(Armor1, 'armor')
    # print char1.equipment.armor.bonuses
    # print char1.equipment
    print char1.roll_attr('strength'), 'roll str'


    # print blank_char.attributes
    # print blank_char.attributes._vitality
    # print blank_char.attributes.vitality
