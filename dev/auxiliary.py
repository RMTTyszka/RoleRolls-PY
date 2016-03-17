#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
Auxiliary classes file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import attributes as A
from constants import defenses as D
from constants import resists as R
from constants import equipment as E
from constants import inventory as I
from constants import skills as S

class Attributes(object):
    ''' Base Atributes for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the attributes.
            "strength": char strength,
            "agility": char agility,
            "vitality": char vitality,
            "wisdom": char wisdom,
            "inteligence": char inteligence}
            # "charisma": char charisma} - not implemented so far
        '''
        for attr in A.attributes_list:
            if attr in kwargs:
                setattr(self, attr, kwargs[attr])
            else:
                setattr(self, attr, 0)

    @property
    def str_mod(self):
        return self.strength/2 - 5
    @property
    def agi_mod(self):
        return self.agility/2 - 5
    @property
    def vit_mod(self):
        return self.vitality/2 - 5
    @property
    def wis_mod(self):
        return self.wisdom/2 - 5
    @property
    def int_mod(self):
        return self.inteligence/2 - 5
    @property
    def cha_mod(self):
        return self.charisma/2 - 5

class Defenses(object):
    ''' Base Defenses for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the defenses.
            "cutting", cutting,
            "smashing", smashing,
            "piercing", piercing,
            "magic", magic
        '''
        for defense in D.defenses_list:
            if defense in kwargs:
                setattr(self, defense, kwargs[skill])
            else:
                setattr(self, defense, 0)

class Resists(object):
    ''' Base Resists for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the resists.
            "weakness": weakness,
            "slow": slow,
            "stun": stun,
            "blind": blind,
            "curse": curse
        '''
        for resist in R.resists_list:
            if resist in kwargs:
                setattr(self, resist, kwargs[resist])
            else:
                setattr(self, resist, 0)

class Equipment(object):
    ''' Base Equipment for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the equipment.
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
            "extra": extra
        '''
        for equipment in E.equipment_list:
            if equipment in kwargs:
                setattr(self, equipment, kwargs[equipment])
            else:
                setattr(self, equipment, None)

    def __iter__(self):
        for equipment in E.equipment_list:
            yield equipment, getattr(self, equipment)

    @property
    def evade(self):
        return sum(equipment.evade for name, equipment in self if hasattr(equipment, 'evade'))

    def equip(self, item,  slot):
        '''
        Equips the item in the slot.
        Returns the item if the slot doesn't exists or the old item if the slot is
        occupied
        '''
        if item in C.equipment_list:
            old_item = self.unequip(slot)
            setattr(self, slot, item)
            return old_item
        return item

    def unequip(self, slot):
        '''
        Unequips the item in the slot.
        Returns the item if the slot doesn't exists or the old item if the slot is
        occupied
        '''
        return getattr(self, slot) if hasattr(self, slot) else None

class InventoryError(Exception):
    pass

class Inventory(object):
    ''' Base Inventory for any item in the game '''

    def __init__(self, size, *args):
        '''
        Initializes the inventroy.
        "size" is a positional argument to determine the max size of the inventroy
        Optional arguments are items objects to be inserted to the inventroy.
        Raises an error when trying to create an inventroy with more items than it's capacity
        '''
        self.size = size
        self.gold = 0
        self.items = list(args)

        if len(args) > size:
            raise InventoryError('Cannot create inventory with more items than it\'s capacity')

    @property
    def num_items(self):
        '''
        Number of items in the inventory
        '''
        return len(self.items)

    def add_item(self, item):
        '''
        Adds another item to the inventroy.
        Returns the item if the inventroy is full
        '''
        if self.num_items >= self.size:
            return item
        else:
            self.items.append(item)
            return False

    def remove_item(self, item):
        '''
        Removes the item from the inventory.
        Returns True if the item is not in the inventroy
        '''
        try:
            self.items.remove(item)
            return False
        except:
            return True

    def change_size(self, size):
        '''
        Changes the size of the inventroy
        '''
        self.size = size

class Skills(object):
    ''' Base Atributes for any item in the game '''

    def __init__(self, **kwargs):
        '''
        Initializes the skills.
            "alchemy": alchemy,
            "anatomy": anatomy,
            "animaltaming": animaltaming,
            "archery": archery,
            "armorcrafting": armorcrafting,
            "armslore": armslore,
            "awareness": awareness,
            "bowcrafting": bowcrafting,
            "carpentery": carpentery,
            "fencing": fencing,
            "gathering": gathering,
            "healing": healing,
            "heavyweaponship": heavyweaponship,
            "jewelcrafting": jewelcrafting,
            "leatherworking": leatherworking,
            "lore": lore,
            "lumberjacking": lumberjacking,
            "magery": magery,
            "meditating": meditating,
            "mercantilism": mercantilism,
            "military": military,
            "parry": parry,
            "reflex": reflex,
            "resistspells": resistspells,
            "skinning": skinning,
            "stealth": stealth,
            "swordmanship": swordmanship,
            "tactics": tactics,
            "tailoring": tailoring,
            "wrestling": wrestling
        '''
        for skill in S.skills_list:
            if skill in kwargs:
                setattr(self, skill, kwargs[skill])
            else:
                setattr(self, skill, 0)

if __name__ == '__main__':
    Resist1 = Resists()
    assert type(Resist1.weakness) is int
    Defense1 = Defenses()
    assert type(Defense1.cutting) is int
    Attr1 = Attributes()
    assert type(Attr1.strength) is int
    assert type(Attr1.str_mod) is int

    assert type(Attr1.agility) is int
    assert type(Attr1.agi_mod) is int

    assert type(Attr1.vitality) is int
    assert type(Attr1.vit_mod) is int

    assert type(Attr1.wisdom) is int
    assert type(Attr1.wis_mod) is int

    assert type(Attr1.inteligence) is int
    assert type(Attr1.int_mod) is int

    assert type(Attr1.charisma) is int
    assert type(Attr1.cha_mod) is int

    Equi1 = Equipment()
    print dir(Equi1)
    # pass
    for i in Equi1:
        print i

    Inv1 = Inventory(2, 'gato')
    assert type(Inv1.size) is int
    assert Inv1.size is 2
    assert Inv1.num_items is 1
    assert Inv1.add_item('bola') is False
    assert Inv1.num_items is 2
    assert Inv1.items  == ['gato', 'bola']
    assert Inv1.add_item('bola') == 'bola'
    assert Inv1.num_items is 2
    assert Inv1.remove_item('gato') is False
    assert Inv1.remove_item('gato') is True
    assert Inv1.items  == ['bola']
    Inv1.change_size(3)
    assert Inv1.size == 3

    Skill1 = Skills()
    assert type(Skill1.meditating) is int

    print 'All tests ok!'
