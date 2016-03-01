#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
class T(object):
    def __init__(self):
        self.a = 0
    @property
    def A(num):
        return self.a
t = T()
bra = 'ras'
if hasattr(t,'a'):
    print t.a
if hasattr(bra,'a'):
    print 'deu certo'
else:
    print 'nao'
