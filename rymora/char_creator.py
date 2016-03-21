#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes
Char Creator

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from conf import const as C
from conf import config
import Chars
import pygame
import os
import time
import random
import Graph_Char
BLACK = ( 0,0,0)
BLUE    = (   0,   0,   255)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
XCOLOR   = ( 100, 100, 100)
rangecolor = [BLUE, WHITE, GREEN, RED, XCOLOR]


def load_image(name, colorkey=None):
    fullname = os.path.join( name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    #image = image.convert()
    image = image.convert_alpha()
    #if colorkey is not None:
    #    if colorkey is -1:
    #        colorkey = image.get_at((0,0))
    #    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
def create_combat():
    col = 0
    col2 = 0
    for x in ['roggar','miggah','kaifro','ziltan','potrak']:
        y = Mons_Pygame.t_play(x,1,rangecolor[len(config.players)])
        y.combat_gra = Graph_Char.Graph_Player(y)
        config.players.append(y)

    for x in ['goblin warrior','goblin mage','goblin cleric','goblin assassin','goblin shaman']:
        y = Mons_Pygame.brute(x,1,rangecolor[len(config.monsters)])
        y.combat_gra = Graph_Char.Graph_Player(y)
        config.monsters.append(y)
    return config.players, config.monsters
class Mons_Pygame(Chars.Monster):
    def __init__(self,name,nv,color):
        super(Mons_Pygame,self).__init__(name,nv,color)
        self.sprite = pygame.sprite.Sprite()
        self.name = name
        for atr in C.atr_list:
            self.mod(atr,1+5*self.nv)
        for skill in C.skills_list:
            self.mod(skill,1+5*self.nv)
    def attack(self,hand):
        time.sleep(1)
        if self.target == None:
            self.def_AT
            comparare = [[char, char.risk_lv] for char in self.AT_target]
            compare =  max(comparare, key=lambda x:x[1])
            target = compare[0]
        else:
            target = self.target
        crit = False
        hit = False
        counter = False
        z = random.randint(1,100)
        a = self.AT(self.equipament['mainhand'])
        b = target.EVD
        if z + a - b >= 100 - (self.CRIT-target.RESILIENCE):
            crit = True
        if z + a - b >= 20:
            hit = True
        if z + a - b <= target.mod('counterrating'):
            counter = True
        if counter:
            d = target.main_damage(self)
            return d, "Counter", self
            self.LIFE -= d
            #print self.name, 'has', self.LIFE, 'of life'
        if hit:
            d = self.main_damage(target)
            string = 'Hit'
            if crit:
                string =  'Crit'
                d *= 2
            target.LIFE -= d
            return d, string, target

        if hit == False:
            return 0,'Miss', target



if __name__ == "__main__":
    class Char_Creator(C.Player):
        def __init__(self):
            self.points = 30
            def str(self):
                pass
    points = 30
    while points != 0:
        str = raw_input('strengh')
        agi = raw_input('agility')
        vit = raw_input('vitality')
        wis = raw_input('wisdom')
        int = raw_input('intuition')
        awsr = False
        print C.skills_list
        while awsr == False:
            skill1 = raw_input('What is your main skill')
            if skill1 in C.skills_list:
                awsr = True
            else:
                print 'Thats not a skill'
        while awsr == False:
            skill2 = raw_input('What is your secondary skill')
            if skill2 in C.skills_list:
                awsr = True
            else:
                print 'Thats not a skill'
        while awsr == False:
            skill3 = raw_input('What is your tertiary skill')
            if skill3 in C.skills_list:
                awsr = True
            else:
                print 'Thats not a skill'

        player = Char.Player(str,agi,vit,wis,int,skill1,30,skill2,20,skill3,10)
        config.players.append(player)
