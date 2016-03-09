#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
char file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import char as C

class Char(object):
    ''' Base class for any item in the game '''

    def __init__(self, name, lvl, attributes, skills, defenses=None, resists=None,
        equipment=None, inventory=None, effects=None, powers=None, spells=None,
        bonuses=None, HP=None, SP=None, ST=None):
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
                "equipment" = {
                    "mainhand": mainhand,
                    "offhand": offhand,
                    "helmet": helmet,
                    "neck": neck,
                    "armor": armor
                    "wrist": wrist
                    "gauntlet": gauntlet
                    "ring1": ring1
                    "ring2": ring2
                    "belt": belt
                    "boots": boots
                    "extra": extra}

            inventory: char inventory (dict, values are 'Item' objects)
                "inventory" = {
                    "item1": item1,
                    "item2": item2,
                    "item3": item3,
                    ...}

            effects: char effects (dict, values are 'Effects' objects)
                "effects" = {
                    "effect1": effect1,
                    "effect2": effect2,
                    "effect3": effect3,
                    ...}

            powers: char powers (dict, values are 'Power' objects)
                "powers" = {
                    "power1": power1,
                    "power2": power2,
                    "power3": power3,
                    ...}

            spells: char spells (dict, values are 'Spells' objects)
                "powers" = {
                    "spell1": spell1,
                    "spell2": spell2,
                    "spell3": spell3,
                    ...}

            bonuses: char bonuses (dict, values are 'Bonus' objects)
                "bonuese" = {
                    "bonus1": bonus1,
                    "bonus2": bonus2,
                    "bonus3": bonus3,
                    ...}

            HP: char HP - if not specified it's set with char's attributes

            SP: char SP - if not specified it's set with char's attributes

            ST: char ST - if not specified it's set with char's attributes
        '''
        # Char mains
        self.name = name
        self.lvl = lvl
        self._alive = True
        # Char attributes
        self.attributes = attributes
        # Skills
        self.skills = skills
        # Defenses
        self.defenses = defenses
        # Resists
        self.resists = resists
        # Equipment
        self.equipment = equipment
        # Inventory
        self.inventory = inventory
        # effects
        self.effects = effects
        # Powers
        self.powers = powers
        # Spells
        self.spells = spells
        # Bonuses
        self.bonuses = bonuses
        # Extra data
        self.calculate_data()
        # Starting HP and MP
        self._HP = HP if HP is not None else self.maxHP
        self._SP = SP if SP is not None else self.maxSP
        self._ST = ST if ST is not None else self.maxST

    def __repr__(self):
        string = 'char: {0}\nHP: {1} MP: {2}'.format(self.name, self.HP, self.SP)
        if self.effects:
            string += '\neffects: {0}'.format(self.effects.keys())
        return string

    def calculate_data(self):
        self.maxHP = C.HP_BASE + self.attributes.vit_mod*10
        self.maxSP = C.SP_BASE + self.attributes.int_mod
        self.maxST = C.ST_BASE + self.attributes.vit_mod/2+self.skills.meditating/2

    def run_effects(self):
        for effect_name, effect in self.effects.items():
            effect(self)
            # if not hasattr(self, effect_name):
                # setattr(self, effect_name, effect)
            # getattr(self, effect_name).run(self)

    # HP property
    @property
    def HP(self):
        '''
        character HP
        '''
        return self._HP
    @HP.setter
    def HP(self, value):
        value = self.maxHP if value > self.maxHP else value
        self._HP = value
        self._alive = True if self._HP > 0 else False
    @property
    def HP_percent(self):
        '''
        character HP in percentage
        interval: 0 - 1
        '''
        return self._HP/self.maxHP
    @HP_percent.setter
    def HP_percent(self, value):
        self.HP = int(round(value*self.maxHP))

    # SP property
    @property
    def SP(self):
        '''
        character SP
        '''
        return self._SP
    @SP.setter
    def SP(self, value):
        value = self.maxSP if value > self.maxSP else value
        self._SP = value
    @property
    def SP_percent(self):
        '''
        character SP in percentage
        interval: 0 - 1
        '''
        return self._SP/self.maxSP
    @SP_percent.setter
    def SP_percent(self, value):
        self.SP = int(round(value*self.maxSP))

    # ST property
    @property
    def ST(self):
        '''
        character ST
        '''
        return self._ST
    @ST.setter
    def ST(self, value):
        value = self.maxST if value > self.maxST else value
        self._ST = value
    @property
    def ST_percent(self):
        '''
        character ST in percentage
        interval: 0 - 1
        '''
        return self._ST/self.maxST
    @ST_percent.setter
    def ST_percent(self, value):
        self.ST = int(round(value*self.maxST))

if __name__ == '__main__':
    import attributes
    import skills
    import defenses
    import resists
    import effects
    Attr1 = attributes.Attributes()
    Skill1 = skills.Skills()
    Def1 = defenses.Defenses()
    Res1 = resists.Resists()
    Eff1 = {'poisoned': effects.Effects.poisoned}

    char1 = Char(name='bob', lvl=1, attributes=Attr1, skills=Skill1, defenses=Def1, resists=Res1, effects=Eff1) #... inserir o resto aqui

    # run poison effect
    print char1, 'antes do veneno'
    char1.run_effects()
    print char1, 'depois do veneno'
