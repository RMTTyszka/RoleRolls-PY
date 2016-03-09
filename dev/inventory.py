#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
inventory file

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from constants import inventory as C

class InventroyError(Exception):
    pass

class Inventroy(object):
    ''' Base Inventroy for any item in the game '''

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
            raise InventroyError('Cannot create inventory with more items than it\'s capacity')

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


if __name__ == '__main__':
    Inv1 = Inventroy(2, 'gato')
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
    print 'All tests ok!'
