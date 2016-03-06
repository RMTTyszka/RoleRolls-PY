#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
json parameters parser

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import json
from os.path import dirname, abspath

FOLDER_PATH = dirname(abspath(__file__))+'/'
DEFAULT_CONST = FOLDER_PATH+'const.json'

with open(DEFAULT_CONST, 'r') as text:
    data = json.loads(text.read())
    globals().update(**data)

if __name__ == '__main__':
    assert data
    print 'All tests ok!'
