import pygame
import Chars
import os
TAN = (210,200,180)
BLACK = ( 0,0,0)
BLUE    = (   0,   0,   255)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
GRAY   = ( 100, 100, 100)
YELLOW = (255,255,0)
class Graph_Char(object):
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self._backgroundsize = (200,260)
        pygame.font.init()
        self.basicFont = pygame.font.Font(None, 30)
class Graph_Player(Graph_Char):
    def __init__(self,Player):
        super(Graph_Player,self).__init__()
        self.screen = None
        self.player = Player
        self._SP_bar = pygame.sprite.Sprite()
        #self._ST_bar = pygame.sprite.Sprite()
        self._char = pygame.sprite.Sprite()
        self._background = pygame.sprite.Sprite()
        self.define_values()
        self.combat_sprites = pygame.sprite.LayeredUpdates(self._background,self._char,self._SP_bar,self._life_bar)
    def define_values(self):
        self._background.image = pygame.Surface(self._backgroundsize)
        self._background.image.fill(TAN)
        self._background.rect = self._background.image.get_rect()
        self._char.image = pygame.image.load(os.path.join("Green_Goblin.png"))
        self._char.rect = self._char.image.get_rect()
        self._life_bar = Life_Bar(self._background,self.player)
        self._SP_bar = SP_Bar(self._background,self.player)

    def update(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self._background.rect.topleft = (self.posx,self.posy)
        self._char.image.convert()
        self._char.rect.center = self._background.rect.center
        self._SP_bar.update()
        self._life_bar.update()
        #self.ST_bar
    def anima_crit(self):
        dist = 16
        times = 2
        text = self.basicFont.render('Evade', 1, YELLOW)
        textrect = self._char.rect.move(self._char.rect.width/4,-42)
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,-dist)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,dist)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
    def anima_at(self):
        dist = 8
        times = 3
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,-dist)
            self.combat_sprites.draw(self.screen)
            pygame.display.flip()
            pygame.time.delay(25)
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,dist)
            self.combat_sprites.draw(self.screen)
            pygame.display.flip()
            pygame.time.delay(25)
    def anima_evd(self):
        dist = 8
        times = 3
        text = self.basicFont.render('Evade', 1, BLUE)
        textrect = self._char.rect.move(self._char.rect.width/4,-32)
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,dist)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
        for x in range(times):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(0,-dist)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
        self.screen.blit(self._background.image,textrect,textrect)
    def anima_dam(self,damage):
        dist = 3

        text = self.basicFont.render(str(damage), 1, RED)
        textrect = self._background.rect.move(self._background.rect.width/2,self._background.rect.height*0.9)
        self.screen.blit(text,(textrect))
        pygame.display.flip()
        for x in range(3):
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(dist,0)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(-dist,0)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(-dist,0)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
            self.combat_sprites.clear(self.screen,self.screen)
            self._char.rect = self._char.rect.move(dist,0)
            self.combat_sprites.draw(self.screen)
            self.screen.blit(text,(textrect))
            pygame.display.flip()
            pygame.time.delay(25)
        self.screen.blit(self._background.image,textrect,textrect)
class Bar(pygame.sprite.Sprite):
    def __init__(self,background):
        self.color = BLACK
        self.height = 6
        self.background = background
        self.image = pygame.Surface((self.background.rect.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.percent = 100
class Life_Bar(Bar):
    def __init__(self,background,creature):
        pygame.sprite.Sprite.__init__(self)
        Bar.__init__(self,background)
        self.color = RED
        self.image = pygame.Surface((self.background.rect.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.creature = creature
    def update(self):
        #if self.percent != self.creature.LIFEPERCENT:
        #self.background.image.blit(self.background.image,self.rect,self.rect)
        #self.rect.width = int(self.rect.width * self.creature.LIFE_PERCENT/100.0)
        #self.rect.height = int(self.background.rect.height*0.8)
        #self.image = pygame.Surface((self.rect.width,self.height))
        #self.image.fill(self.color)
        #self.background.image.blit(self.image,self.rect)
        self.image = pygame.Surface((int(self.background.rect.width*self.creature.LIFE_PERCENT/100),self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.left = self.background.rect.left
        self.rect.top = int(self.background.rect.top+self.background.rect.height*0.8)
class SP_Bar(Bar):
    def __init__(self,background,creature):
        pygame.sprite.Sprite.__init__(self)
        Bar.__init__(self,background)
        self.color = BLUE
        #self.image = pygame.Surface((self.background.rect.width,self.height))
        #self.image.fill(self.color)
        #self.rect = self.image.get_rect()
        self.creature = creature
    def update(self):
        self.image = pygame.Surface((int(self.background.rect.width*self.creature.SP_PERCENT/100),self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.left = self.background.rect.left
        self.rect.top = int(self.background.rect.top+self.background.rect.height*0.85)
        #@classmethod
def organize(screen,players,monsters):
    x = 10
    xoffset = 210
    for p in players:
        allSprites.add(p.combat_gra._background,p.combat_gra._life_bar,p.combat_gra._SP_bar,p.combat_gra._char,p.combat_gra._life_bar)
        p.combat_gra.screen = screen
        p.combat_gra.update(x,450)
        x += xoffset
if __name__ == "__main__":
    p1 = Chars.Monster.brute("Raccon",1,BLUE)
    p2 = Chars.Monster.brute("Maggah",1,BLUE)
    p3 = Chars.Monster.brute("Falcon",1,BLUE)
    p4 = Chars.Monster.brute("Pluritus",1,BLUE)
    p5 = Chars.Monster.brute("Kalkayua",1,BLUE)
    players = [p1,p2,p3,p4,p5]
    allSprites = pygame.sprite.LayeredUpdates()
    for p in players:
        p.combat_gra = Graph_Player(p)
    players[0].LIFE -= 150
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    background = pygame.Surface((1280,720))
    background.fill(BLACK)
    organize(screen,players, [])
    while 1:
        allSprites.clear(screen,screen)
        allSprites.update()
        allSprites.draw(screen)
        p1.graphic.anima_evd(screen)
        p2.graphic.anima_at(screen)
        p3.graphic.anima_dam(screen,'53')
        pygame.display.update()
