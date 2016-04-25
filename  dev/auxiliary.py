#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
Auxiliary classes file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''

#remove constants if they're not necessary
from constants import attributes as A
from constants import defenses as D
from constants import resists as R
from constants import equipment as E
from constants import inventory as I
from constants import skills as S
import dice

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
            self.get_attr_fn(attr)
            self.get_attr_mod_fn(attr)
            if attr in kwargs:
                setattr(self, '_'+attr, kwargs[attr])
            else:
                setattr(self, '_'+attr, 0)
            if attr+'_bonus' in kwargs:
                setattr(self, attr+'_bonus', kwargs[attr+'_bonus'])
            else:
                setattr(self, attr+'_bonus', 0)

    def __repr__(self):
        string = ''
        for attr in A.attributes_list:
            string += '{0}: {1}\tbonus: {2}\n'.format(attr, getattr(self, attr)(), getattr(self, attr+'_bonus'))
        return string

    def get_attr_fn(self, attr):
        def attr_fn():
            return getattr(self,'_'+attr) + getattr(self,attr+'_bonus')
        attr_fn.__doc__ = "docstring for ",attr
        attr_fn.__name__ = str(attr)
        setattr(self,attr_fn.__name__, attr_fn)

    def get_attr_mod_fn(self, attr):
        def attr_mod_fn(value = None):
            value = value if value is not None else 5
            return (getattr(self,'_'+attr) + getattr(self,attr+'_bonus'))/value
        attr_mod_fn.__doc__ = "docstring for ",attr
        attr_mod_fn.__name__ = str(attr)+'_mod'
        setattr(self,attr_mod_fn.__name__, attr_mod_fn)

    def roll(self, attribute):
        '''
        Makes a roll of the attribute in the argument
        '''
        return dice.roll_01(getattr(self, attribute)())

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
            self.get_def_fn(defense)
            if defense in kwargs:
                setattr(self, '_'+defense, kwargs[defense])
            else:
                setattr(self, '_'+defense, 0)
            if defense+'_bonus' in kwargs:
                setattr(self, defense+'_bonus', kwargs[defense+'_bonus'])
            else:
                setattr(self, defense+'_bonus', 0)
    def __repr__(self):
        string = ''
        for defense in D.defenses_list:
            string += '{0}: {1}\tbonus: {2}\n'.format(defense, getattr(self, defense), getattr(self, defense+'_bonus'))
        return string
    def get_def_fn(self,defen):
        def def_fn():
            return getattr(self,'_'+defen) + getattr(self,defen+'_bonus')
        def_fn.__doc__ = "docstring for ",defen
        def_fn.__name__ = str(defen)
        setattr(self,def_fn.__name__, def_fn)
    #@property
    #def cutting(self):
    #    return self._cutting + self.cutting_bonus
    #@property
    #def smashing(self):
    #    return self._smashing + self.smashing_bonus
    #@property
    #def piercing(self):
    #    return self._piercing + self.piercing_bonus
    #@property
    #def magic(self):
    #    return self._magic + self.magic_bonus
    def roll(self, defense):
        '''
        Makes a roll of the defense in the argument
        '''
        return dice.roll_01(getattr(self, defense)())

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
            self.get_resist_fn(resist)
            if resist in kwargs:
                setattr(self, '_'+resist, kwargs[resist])
            else:
                setattr(self, '_'+resist, 0)
            if resist+'_bonus' in kwargs:
                setattr(self, resist+'_bonus', kwargs[resist+'_bonus'])
            else:
                setattr(self, resist+'_bonus', 0)


    def __repr__(self):
        string = ''
        for resist in R.resists_list:
            string += '{0}: {1}\tbonus: {2}\n'.format(resist, getattr(self, resist), getattr(self, resist+'_bonus'))
        return string
    def get_resist_fn(self,resist):
        def def_fn():
            return getattr(self,'_'+resist) + getattr(self,resist+'_bonus')
        def_fn.__doc__ = "docstring for ",resist
        def_fn.__name__ = str(resist)
        setattr(self,def_fn.__name__, def_fn)
    def roll(self, resist):
        '''
        Makes a roll of the resist in the argument
        '''
        return dice.roll_01(getattr(self, resist)())


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

    def __repr__(self):
        string = ''
        for equipment in E.equipment_list:
            string += '{0}: {1}\n'.format(equipment, getattr(self, equipment))
        return string


    def equip(self, item,  slot = None):
        '''
        Equips the item in the slot.
        Returns the item if the slot doesn't exists or the old item if the slot is
        occupied
        '''
        slot = item.slot if slot == None else slot
        if slot in E.equipment_list:
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

    def __iter__(self):
        for item in self.items:
            yield item

    def __repr__(self):
        return str(self.items)

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
            self.get_skill_fn(skill)
            self.get_skill_mod_fn(skill)
            if skill in kwargs:
                setattr(self, '_'+skill, kwargs[skill])
            else:
                setattr(self, '_'+skill, 0)
            if skill+'_bonus' in kwargs:
                setattr(self, skill+'_bonus', kwargs[skill+'_bonus'])
            else:
                setattr(self, skill+'_bonus', 0)

    def __repr__(self):
        string = ''
        for skill in S.skills_list:
            string += '{0}: {1}\tbonus: {2}\n'.format(skill, getattr(self, skill), getattr(self, skill+'_bonus'))
            return string
    def get_skill_fn(self,skill):
        def def_fn():
            return getattr(self,'_'+skill) + getattr(self,skill+'_bonus')
        def_fn.__doc__ = "docstring for ",skill
        def_fn.__name__ = str(skill)
        setattr(self,def_fn.__name__, def_fn)
    def get_skill_mod_fn(self,skill):
        def def_fn(value = None):
            value = value if not value == None else 5
            return (getattr(self,'_'+skill) + getattr(self,skill+'_bonus'))/value
        def_fn.__doc__ = "docstring for ",skill+'_mod'
        def_fn.__name__ = str(skill)+'_mod'
        setattr(self,def_fn.__name__, def_fn)
    def roll(self, skill):
        '''
        Makes a roll of the skill in the argument
        '''
        return dice.roll_01(getattr(self, skill)())



if __name__ == '__main__':
    Resist1 = Resists()
    assert type(Resist1.weakness()) is int
    Defense1 = Defenses()
    assert type(Defense1.cutting()) is int
    Attr1 = Attributes()
    Attr1._agility = 20
    assert type(Attr1.strength()) is int
    assert type(Attr1.str_mod()) is int
    assert type(Attr1.strength_bonus) is int

    assert type(Attr1.agility()) is int
    assert type(Attr1.agi_mod()) is int
    assert type(Attr1.agility_bonus) is int

    assert type(Attr1.vitality()) is int
    assert type(Attr1.vit_mod()) is int
    assert type(Attr1.vitality_bonus) is int

    assert type(Attr1.wisdom()) is int
    assert type(Attr1.wis_mod()) is int
    assert type(Attr1.wisdom_bonus) is int

    assert type(Attr1.inteligence()) is int
    assert type(Attr1.int_mod()) is int
    assert type(Attr1.inteligence_bonus) is int

    assert type(Attr1.charisma()) is int
    assert type(Attr1.cha_mod()) is int
    assert type(Attr1.charisma_bonus) is int

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
    print dir(Skill1)
    assert type(Skill1.meditating()) is int
    print Attr1
    print Defense1
    print Resist1
    print Attr1.strength
    print Attr1.roll('agility')
    Attr1.str_bonus = 10
    print Attr1.strength
    print 'All tests ok!'
