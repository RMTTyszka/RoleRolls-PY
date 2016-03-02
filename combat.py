#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
from rymora.conf import const as C
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
#Globals0


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
        CC.create_combat()
        t = 0
        for player in config.players:
            player.order()
        for mons in config.monsters:
            mons.order()
        while F.det_end(config.players) == True and F.det_end(config.monsters) == True:
            if t%1 == 0.0:  print 'time is',t
            F.risk_lv(config.players,config.monsters)
            for play in config.players:
                play.order(0.1)
            for mons in config.monsters:
                mons.order(0.1)
            #time.sleep(0.1)
            t = round(t+0.1,2)
        for play in config.players:
            print play.name, play.LIFE
        for mons in config.monsters:
            print mons.name, mons.LIFE
        print 'time is',t
        quit()
        '''combate entre duas criaturas, tudo desconfigurado'''
        config.monsters.append(Chars.Monster.brute('Goblin Mage',1))
        config.players.append(Chars.Monster.brute('Human Cleric',1))
        #config.players['4'] = Monster.brute('Human Cleric',10)
        #for x in range(len(config.players)):
         #   attack[x] = config.players[x].AS
        config.monsters[0].def_AT()
        config.players[0].def_AT()
        attack1 = config.monsters[0].AS('mainhand')
        attack2 = config.players[0].AS('mainhand')
        AE1 = config.monsters[0].defpower
        AE2 = config.players[0].defpower
        print config.monsters[0].LIFE,config.players[0].LIFE
        print config.monsters[0].LIFE_PERCENT,config.players[0].LIFE_PERCENT
        print config.monsters[0].SP,config.players[0].SP
        print config.monsters[0].SP_PERCENT,config.players[0].SP_PERCENT
        #quit()
        t = 1
        F.risk_lv(config.players,config.monsters)
        while config.monsters[0].LIFE > 0 and config.players[0].LIFE > 0:
            if t%1 == 0.0:
                print 'time ==', t
               #for cat in chars.keys():
               #    for char in chars[cat].values():
               #        print char.name,char.life,'lifes'  ,char.risk_lv
            if attack1 <= 0:
                F.autoattack(config.monsters[0])
                attack1 += config.monsters[0].AS('mainhand')
                config.monsters[0].def_AT()
            if attack2 <= 0:
                F.autoattack(config.players[0])
                attack2 += config.players[0].AS('mainhand')
                config.players[0].def_AT()
            if AE1 <= 0:
                config.monsters[0].cast()
                AE1 = config.monsters[0].defpower
            if AE2 <= 0:
                config.players[0].cast()
                AE2 = config.players[0].defpower
            attack1 -= 0.1
            attack2 -= 0.1
            AE1 -= 0.1
            AE2 -= 0.1
            t = round(t+0.1,2)
            #comparar = [(char[0], char[1].life) for char in config.players.items()]
            F.risk_lv(config.players,config.monsters)
            #aba =  min(comparar, key = lambda x:x[1])
            #print aba[0]
            #time.sleep(0.01)

        print config.monsters[0].LIFE
        print config.players[0].LIFE
