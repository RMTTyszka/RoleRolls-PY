#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pygame
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

def Start_Monsters():
    #Create Monsters
    for x in ['roggar','miggah','kaifro','ziltan','potrak']:
        y = Chars.Monster.t_play(x,1,BLUE)
        config.players.append(y)
        #Creator Players
        for x in ['goblin warrior','goblin mage','goblin cleric','goblin assassin','goblin shaman']:
            y = Chars.Monster.brute(x,1,BLUE)
            config.monsters.append(y)
def Draw_Monsters():
    for x in range (5):
        #pygame.draw.rect(screen,rangecolor[x],(x*100,64,64,64))
        config.monsters[x].sprite = pygame.sprite.Sprite()
        font = pygame.font.SysFont('Calibri', 15, True, False)
        text = font.render(str(config.monsters[x].name),True,rangecolor[x-1])
        screen.blit(text,[x*100,64])
        config.players[x].image = pygame.draw.rect(screen,rangecolor[x],(640-64-x*100,640-64,64,64))
        font = pygame.font.SysFont('Calibri', 15, True, False)
        text = font.render(str(config.players[x].name),True,rangecolor[x-1])
        screen.blit(text,[640-64-x*100,640-64])
pygame.init()
BLACK = ( 0,0,0)
BLUE    = (   0,   0,   255)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
XCOLOR   = ( 100, 100, 100)
rangecolor = [BLUE, WHITE, GREEN, RED, XCOLOR]
size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Testing Combat")

done = False
#pygame.draw.rect(screen,RED,(64,64,30,30))
Start_Monsters()
Draw_Monsters()

pygame.display.flip()
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
    

    clock.tick(60)
