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

            bonuses: char bonuses (dict, values are 'Bonus' objects)

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
    def blank(cls, name, **kwargs):
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
        return cls(name, **blank)


if __name__ == '__main__':

    Attr1 = auxiliary.Attributes(vitality=10)
    Skill1 = auxiliary.Skills()
    Def1 = auxiliary.Defenses()
    Res1 = auxiliary.Resists()
    Equ1 = auxiliary.Equipment()
    Eff1 = {'poisoned': effects.Effects.poisoned}

    char1 = Char(name='bob', lvl=1, attributes=Attr1, skills=Skill1, defenses=Def1, resists=Res1, effects=Eff1, equipment=Equ1) #... inserir o resto aqui

    # run poison effect
    print char1, 'before poison'
    char1.run_effects()
    print char1, 'after poison'
    blank_char = Char.blank('boris')
    print blank_char
