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
        self.screen = pygame.display.set_mode((640,640))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(BLACK)
        self.frame = 30
        self.fpstime = pygame.time.Clock()
        self.pl = pygame.sprite.RenderPlain()

    def Normal_Battle(self):
            self.screen.fill(BLACK)
            offset = 0
            for play in self.Players:
                play.sprite.image, play.sprite.rect = CC.load_image("Green_Goblin.png",-1)

                play.sprite.rect.topleft = (64+offset,640-128)
                self.pl.add(play.sprite)
                offset += 100
            offset = 0
            for mons in self.Monsters:
                mons.sprite.image, mons.sprite.rect = CC.load_image("Green_Goblin.png",-1)

                #self.screen.blit(play.image,(-64+offset,640))
                mons.sprite.rect.topleft = (64+offset,128)
                self.pl.add(mons.sprite)
                offset += 100
            self.pl.draw(self.screen)
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
                for mons in self.Monsters:
                    self.det_end
                    self.risk_lv
                    self.order(mons,tick)
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
    def anima_evd(self,creature):


        text = self.basicFont.render('Evade', 1, BLUE)
        self.screen.blit(text,(creature.sprite.rect.left,creature.sprite.rect.top-30))
        pygame.display.flip()

    def anima_dam(self,creature,damage):
        text = self.basicFont.render(str(damage), 1, RED)
        textrect = creature.sprite.rect.move(0,64)
        self.screen.blit(text,(textrect))
        pygame.display.flip()
        for x in range(3):
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centerx += 3
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centerx -= 3
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centerx -= 3
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centerx += 3
            pygame.time.delay(50)
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
        self.screen.blit(self.background,textrect,textrect)
    def anima_at(self,creature):
        for x in range(1):
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centery += 6
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centery -= 6
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centery -= 6
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
            self.screen.blit(self.background,creature.sprite.rect,creature.sprite.rect)
            creature.sprite.rect.centery += 6
            pygame.time.delay(50)
            self.screen.blit(creature.sprite.image,creature.sprite.rect)
            pygame.display.flip()
            pygame.time.delay(50)
    def anima_counter(self,creature):
        return 0
    def anima_crit(self,creature):
        return 0
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
                        self.anima_at(creature)
                        self.anima_dam(target,damage)
                    if atk == "Crit":
                        self.anima_crit(creature)
                        self.anima_dam(creature,damage)
                    if atk == "Miss":
                        self.anima_at(creature)
                        self.anima_evd(target)
                    if atk == "Counter":
                        self.anima_at(creature)
                        self.anima_counter(target)
                        self.anima_dam(creature,damage)
                    creature._attack_order[0] += creature.AS('mainhand')
                if hasattr(creature.equipament['offhand'],'weapons'):
                    if creature._attack_order[1] <= 0:
                        creature.attack('offhand')
                        creature._attack_order[1] += creature.AS('offhand')
                if creature._attack_spec_order <= 0:
                    creature.cast
                    creature._attack_spec_order += creature.defpower
'''roda um teste, para verificar a igualdade entre as armas e armaduras'''
if __name__ == "__main__":
    yes = 'no'
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
