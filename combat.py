#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from rymora import conf as C
from rymora.conf import config
from rymora import Powers as P
from rymora.Powers import Power
from rymora import Functions as F
from rymora import itens as I
from rymora import Chars
from rymora import char_creator as CC
import random
import time
import numbers
import pygame
#Globals0
BLACK = ( 0,0,0)
BLUE    = (   0,   0,   255)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
GRAY   = ( 100, 100, 100)
rangecolor = [BLUE, WHITE, GREEN, RED, GRAY]
class Battle():
    def __init__(self,Players, Monsters,Enviroment = None):
        pygame.init()
        self.basicFont = pygame.font.Font(None, 20)
        self.Players = Players
        self.Monsters = Monsters
        self.screen = pygame.display.set_mode((1280,720))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(BLACK)
        self.frame = 60
        self.fpstime = pygame.time.Clock()
        self.pl = pygame.sprite.RenderPlain()
        if True in [play.ALIVE for play in self.Players]:
            print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    def Normal_Battle(self):
            self.screen.fill(BLACK)
            self.organize()
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            pygame.display.flip()

            self.t = 0
            tick = 0.1
            for player in self.Players:
                self.order(player)
            for mons in self.Monsters:
                self.order(mons)
            while 1:
                if self.t%1 == 0.0:  print 'time is',self.t
                for play in self.Players:
                    self.det_end
                    self.risk_lv
                    self.order(play,tick)
                    self.allSprites.clear(self.screen,self.screen)
                    self.allSprites.update()
                    self.allSprites.draw(self.screen)
                    self.check_alive()
                for mons in self.Monsters:
                    self.det_end
                    self.risk_lv
                    self.order(mons,tick)
                    self.check_alive()

                #time.sleep(0.1)
                self.t = round(self.t+0.1,2)
            pygame.display.update()
            self.fpstime.tick(self.fps)
    @property
    def risk_lv(self):
        for char in self.Players:
            char.risk_lv = round((100 - char.LIFE_PERCENT)/10,2)
            char.risk_lv += len(char.effects['harmfull'])
            char.risk_lv -= len(char.effects['helpfull'])
        for char in self.Monsters:
            char.risk_lv = round((100 - char.LIFE_PERCENT)/10,2)
            char.risk_lv += len(char.effects['harmfull'])
            char.risk_lv -= len(char.effects['helpfull'])
    @property
    def det_end(self):
        y = False
        for x in self.Players:
            if x.ALIVE:
                y = True
        z = False
        for h in self.Monsters:
            if h.ALIVE:
                z = True
        if z == False or y == False:
            self.end_battle
    @property
    def end_battle(self):
        for play in self.Players:
            print play.name,play.LIFE
        for mons in self.Monsters:
            print mons.name,mons.LIFE
        print 'time is',self.t
        quit()



    def check_alive(self):
        for p in self.Players:
            if not p.ALIVE:
                pygame.draw.line(self.screen,RED,p.combat_gra._char.rect.topleft,p.combat_gra._char.rect.bottomright,3)
                pygame.draw.line(self.screen,RED,p.combat_gra._char.rect.topright,p.combat_gra._char.rect.bottomleft,3)
                pygame.display.update()
        for m in self.Monsters:
            if not m.ALIVE:
                pygame.draw.line(self.screen,RED,m.combat_gra._char.rect.topleft,m.combat_gra._char.rect.bottomright,3)
                pygame.draw.line(self.screen,RED,m.combat_gra._char.rect.topright,m.combat_gra._char.rect.bottomleft,3)
                pygame.display.update()

    def organize(self):
        self.allSprites = pygame.sprite.LayeredUpdates()
        x = 10
        xoffset = 210
        for p in self.Players:
            self.allSprites.add(p.combat_gra._background,p.combat_gra._life_bar,p.combat_gra._SP_bar,p.combat_gra._char,p.combat_gra._life_bar)
            p.combat_gra.screen = self.screen
            p.combat_gra.update(x,450)
            x += xoffset
        x = 10
        for m in self.Monsters:
            self.allSprites.add(m.combat_gra._background,m.combat_gra._life_bar,m.combat_gra._SP_bar,m.combat_gra._char,m.combat_gra._life_bar)
            m.combat_gra.screen = self.screen
            m.combat_gra.update(x,10)
            x += xoffset
    def order(self,creature,value = 0):
        if creature.active_checker:
            if value == 0:
                '''define the Power, the target and the casting time'''
                creature._attack_spec_order = creature.defpower
                '''define the attack order'''
                creature._attack_order = []
                creature._attack_order.append(creature.AS('mainhand'))
                if hasattr(creature.equipament['offhand'],'weapons'):
                    creature._attack_order.append(creature.AS('offhand'))
            else:
                '''faz passar o tempo para esse personagem, e
                vefirica se esta na hora de atacar ou nao'''
                for atk in range(len(creature._attack_order)):
                    creature._attack_order[atk] = round(creature._attack_order[atk]-value,2)

                    #print atk
                creature._attack_spec_order = round(creature._attack_spec_order - value,2)
                #time.sleep(0.1)
                if creature._attack_order[0] <= 0:
                    damage, atk, target = creature.attack('mainhand')
                    if atk == "Hit":
                        creature.combat_gra.anima_at()
                        target.combat_gra.anima_dam(damage)
                    if atk == "Crit":
                        creature.combat_gra.anima_crit()
                        target.combat_gra.anima_dam(damage)
                    if atk == "Miss":
                        creature.combat_gra.anima_at()
                        target.combat_gra.anima_evd()
                    if atk == "Counter":
                        creature.combat_gra.anima_at()
                        target.combat_gra.anima_counter()
                        creature.combat_gra.anima_dam(damage)
                    creature._attack_order[0] += creature.AS('mainhand')
                if hasattr(creature.equipament['offhand'],'weapons'):
                    if creature._attack_order[1] <= 0:
                        damage, atk, target = creature.attack('offhand')
                        if atk == "Hit":
                            creature.combat_gra.anima_at()
                            target.combat_gra.anima_dam(damage)
                        if atk == "Crit":
                            creature.combat_gra.anima_crit()
                            target.combat_gra.anima_dam(damage)
                        if atk == "Miss":
                            creature.combat_gra.anima_at()
                            target.combat_gra.anima_evd()
                        if atk == "Counter":
                            creature.combat_gra.anima_at()
                            target.combat_gra.evade()
                            target.combat_gra.anima_counter()
                            target.combat_gra.anima_dam(damage)
                        creature._attack_order[1] += creature.AS('offhand')
                if creature._attack_spec_order <= 0:
                    creature.cast
                    creature._attack_spec_order += creature.defpower
'''roda um teste, para verificar a igualdade entre as armas e armaduras'''
if __name__ == "__main__":
    yes = 'yes'
    if yes == 'yes':
        change = ['light','medium','heavy']
        t1 = {}
        t2 = {}
        media = {'light':[],'medium':[],'heavy':[]}
        media_armor = []
        for x in change:
            t1[x] = []
            total3 = {}
            for w in change:
                nv = 1
                total3[w] = []
                while nv < 21:
                    num = 0
                    a = Chars.Testchar(nv,w,w)
                    d = Chars.Testchar(nv,x,x)
                    total = []
                    while num < 6000/a.AS('mainhand'):
                        b = F.t_autoattack(a,d)
                        total.append(b)
                        #t1[x].append(round(sum(soma)/len(soma),3))
                        #t2[w].append(round(sum(soma)/len(soma),3))
                        num += 1
                    total2 = [n for n in total if n>0]
                    total3[w].append(round(sum(total)/6000,3))
                    nv +=1
                media[w].append(sum(total3[w])/len(total3[w]))
                print w, sum(total3[w])/len(total3[w])
        print 'media das armas'
        for arma in change:
            print sum(media[arma])/len(media[arma])
                #for x in change:
        #   print 'armor',x
        #  print sum(t1[x])/len(t1[x])
        print 'media das armaduras'
        for i in (0,1,2):
            media_armor.append(media['light'][i]+media['medium'][i]+media['heavy'][i])
            print media_armor[i]
        quit()
    else:
        '''cria um combate 5x5 entre monstros e players'''
        Players, Monsters = CC.create_combat()
        Combat = Battle(Players,Monsters)
        Combat.Normal_Battle()
