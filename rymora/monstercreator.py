#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Rymora Land of Heroes

Coyright © 2016 - Ramiro Tyzkza - ramiro.tyszka@gmail.com
'''
import random
import time
import numbers

weapons = {'catalyst':{'staff':'grande','rod':'media','wand':'pequena','orb':'pequena'}}
# armaskills
weaponstype = {'cutting':{'atkskill':'swordmanship','atkatr':'str','danoatr':'str'},
            'smashing':{'atkskill':'heavyweaponship','atkatr':'str','danoatr':'str'},
            'piercing':{'atkskill':'fencing','atkatr':'agi','danoatr':'agi'},
            'ranged':{'atkskill':'archery','atkatr':'agi','danoatr':'agi'},
            'thrown':{'atkskill':'archery','atkatr':'agi','danoatr':'str'},
            'catalyst':{'atkskill':'magery','atkatr':'sab','danoatr':'sab'}}

# armatributos
weaponssize = {'pequena':{'AS':5.0,'danomin':8,'danomax':12,'modataque':0,
            'multiplicadordano':1.0,'multiplicadoratr':1,'counterrating':15},
        'media':{'AS':10.0,'danomin':11,'danomax':19,'modataque':0,'multiplicadordano':1.5,
            'multiplicadoratr':2,'counterrating':10},
        'grande':{'AS':15.0,'danomin':14,'danomax':26,'modataque':10,'multiplicadordano':2.0,
           'multiplicadoratr':3,'counterrating':10},
       'duaspequenas':{'AS':0,'danomin':0,'danomax':0,'modataque':0,
           'multiplicadordano':0,'multiplicadoratr':0,'counterrating':0},
        'duasmedias':{'AS':0,'danomin':0,'danomax':0,'modataque':0,'multiplicadordano':0,'multiplicadoratr':0,'counterrating':0}}
#armas = {'pequena':[5.0,8,12,15,0,1.0,1],'media':[10.0,11,19,10,0,1.5,2],'grande':[15.0,14,26,5,10,2.0,3],'duaspequenas':[5.0,]}
armors = {'leve':('robe'),'media': ('couro batido'),'pesada':('armadura de escamas')}
armorstype = {'None': {'prot':0,'evade':0},'leve': {'prot':1,'evade':0},'media':{'prot':6,'evade':-5},'pesada':{'prot':11,'evade':-10}}
# ordem dos atributos do tyopemonster   armadura // arma //
typemonster = {'tanker':['pesada','media',],'assassin':['leve','pequena'],'brute':['media','grande'],'caster':['leve','magia'],'hunter':['leve','distancia'],'striker':['leve','duaspequenas'],'ranger':['media','duasmedias'],}
crit_list = [15,'anatomy', 5 ,'crit']
resil_list = [5, 'parry', 5, 'resil',1]
damagered_list = [0, 'parry', 5, 'vit', 5, 'damagered', 1]
magicred_list = [0, 'resistspells', 5, 'int', 5, 'magicred', 5, 'mult = 5']
damage_list = [0, 'armslore', 5, 'damage', 1]
AS_list = (0,'AS',1)
life_list = ()
class Char:
    def __init__(self,name,nv):
        self.name = name
        '''atributes'''
        self.nv = nv
        self.atributes = {}
        self.atributes['str'] = 5*nv  +5
        self.atributes['agi'] = 5*nv  +5
        self.atributes['vit']= 5*nv   +5
        self.atributes['sab'] = 5*nv  +5
        self.atributes['int'] = 5*nv  +5
        #Skills
        self.skills = {}
        '''combat'''
        self.skills['archery'] = nv*5
        self.skills['fencing'] = nv*5
        self.skills['heavyweaponship'] = nv*5
        self.skills['magery'] = nv*5
        self.skills['parry'] = nv*5
        self.skills['swordmanship'] = nv*5
        self.skills['tactics'] = nv*5
        self.skills['resistspells'] = nv*5
        #self.atkskill = max(self.skills['swordmanship'], self.skills['fencing'], self.skills['heavyweaponship'])
        '''support'''
        self.skills['armslore'] = nv*5
        self.skills['anatomy'] = nv*5
        self.skills['healing'] = nv*5
        self.skills['lore'] = nv*5
        '''passives'''
        self.skills['awareness'] = nv*5
        self.skills['mercantilism'] = nv*5
        self.skills['stealth'] = nv*5
        '''professions'''
        self.skills['animaltaming'] = nv*5
        self.skills['armorcrafting'] = nv*5
        self.skills['alchemy'] = nv*5
        self.skills['bowcrafting'] = nv*5
        self.skills['carpentery'] = nv*5
        self.skills['gathering'] = nv*5
        self.skills['jewelcrafting'] = nv*5
        self.skills['leatherworking'] = nv*5
        self.skills['lumberjacking'] = nv*5
        self.skills['skinning'] = nv*5
        self.skills['tailoring'] = nv*5

        '''modficators'''
        self.modif = {}
        self.modif['AT'] = 0
        #self.modif['evade'] = self.skills['tactics'] + self.atributes['agi']
        self.modif['AS'] = 0
        self.modif['prot'] = 0
        self.modif['AE'] = 0

        #self.modif['resil'] = 5 + self.skills['parry']/5
        #self.modif['crit'] = 15+ self.skills['anatomy']/5
        #self.modif['damagered'] = self.skills['parry']/5 + self.atributes['vit']/5
        #self.modif['magicred'] = self.skills['resistspells']/5 * self.atributes['int']/10

        '''inv'''
        self.defesas = {}
        self.resist = {}
        self.equipamento = {}
        self.weaponpower = 'x'
        self.defesas['cutting'] = 0
        self.defesas['smashing'] = 0
        self.defesas['piercing'] = 0
        self.defesas['magia'] = 0
        self.resist['enfraquecimento'] = 0
        self.resist['lentidão'] = 0
        self.resist['atordoamento'] = 0
        self.resist['cegueira'] = 0
        self.resist['maldição'] = 0



        self.bonusequip = {}
        self.bonustemp = {'moral':{},'magic':{},'profession':{}}
        self.pontos = {}
        self.pontos['MAXPV'] = 0
        self.pontos['PV'] = None
    def PVMAX(self):
        self.pontos['MAXPV'] = 100 + 10*self.atributes['vit']
        if self.pontos['PV'] == None:
            self.pontos['PV'] = self.pontos['MAXPV']
    def atkspd(self,weaponhand):
        a = self.equipamento[weaponhand].armatributos['AS']
        b = self.modifroll(*AS_list)
        return a * (1-b/100)
    def evaderoll(self):
        a = self.modifroll(0,'tactics',1)
        b = self.modifroll(0,'agi',5)
        c = self.modifroll(0,'evade',1)
        return a + b + c
    def atkroll(self,weapon):
        a = self.modifroll(0,'AT',1)
        b = self.modifroll(0,weapon.armaskills['atkskill'],1)
        c = self.modifroll(0,weapon.armaskills['atkatr'],5)
        return a + b + c
    def atkesp(self,atr,skill):
        a = self.modifroll(0,atr,5)
        b = self.modifroll(0,skill,1)
        c = self.modifroll(0,'AE',1)
        return a + b + c
    def modifroll(self,default = 0, first = None, one = 1, second = None, two = 1, third = None, three = 1, fourth = None, four = 1, mult = 1):

        g,h,i,j = 0,0,0,0
        if self.atributes.has_key(first):
            g += self.atributes[first]
        if self.skills.has_key(first):
            g += self.skills[first]
        if self.modif.has_key(first):
            g += self.modif[first]
        if self.defesas.has_key(first):
            g += self.defesas[first]
        if self.resist.has_key(first):
            g += self.resist[first]
        if self.bonusequip.has_key(first):
            g += self.bonusequip[first]
        for bon in self.bonustemp.keys():
            if self.bonustemp[bon].has_key(first):
                g += self.bonustemp[bon][first]
        g /= one
        if self.atributes.has_key(second):
            h += self.atributes[second]
        if self.skills.has_key(second):
            h += self.skills[second]
        if self.modif.has_key(second):
            h += self.modif[second]
        if self.defesas.has_key(second):
            h += self.defesas[second]
        if self.resist.has_key(second):
            h += self.resist[second]
        for bon in self.bonustemp.keys():
            if self.bonustemp[bon].has_key(second):
                h += self.bonustemp[bon][second]
        h /= two
        if self.atributes.has_key(third):
            i += self.atributes[third]
        if self.skills.has_key(third):
            i += self.skills[third]
        if self.modif.has_key(third):
            i += self.modif[third]
        if self.defesas.has_key(third):
            i += self.defesas[third]
        if self.resist.has_key(third):
            i += self.resist[third]
        for bon in self.bonustemp.keys():
            if self.bonustemp[bon].has_key(third):
                i += self.bonustemp[bon][third]
        i /= three
        if self.atributes.has_key(fourth):
            j += self.atributes[fourth]
        if self.skills.has_key(fourth):
            j += self.skills[fourth]
        if self.modif.has_key(fourth):
            j += self.modif[fourth]
        if self.defesas.has_key(fourth):
            j += self.defesas[fourth]
        if self.resist.has_key(fourth):
            j += self.resist[fourth]
        for bon in self.bonustemp.keys():
            if self.bonustemp[bon].has_key(fourth):
                j += self.bonustemp[bon][fourth]
        j /= four
        return (default + g + h + i + j)*mult
    def especdamage(self,damage,castingtime,):
        print 'abacate'
    #def defpower(
    #    self,status1 = None, cond1 = None, number1 = 1 ,skill1 = None,target1 = None, targetnum1 = 1,
    #    status2 = None,cond2 = None, number2 = 1 ,skill2 = None,target2 = None, targetnum2 = 1,
    #    status3 = None,cond3 = None, number3 = 1 ,skill3 = None,target3 = None, targetnum3 = 1,
    #    status4 = None,cond4 = None, number4 = 1 ,skill4 = None,target4 = None, targetnum4 = 1
    #            ):
    #    sum1 = 0
    #    if cond1 == '<':
    #        if target1 == 'friendly':
    #            for member in party:
    #                if member.status1 < number1:
    #                    sum1 += 1
    #            if sum1 >= targetnum1:
    #                return skill1
    #    if cond1 == <:
    #        if target1 == 'friendly':
    #            for member in party:
    #                if member.status1 < number1:
    #                    sum1 += 1
    #            if sum1 >= targetnum1:
    #                return skill1
    def equip(self,mainhand,armor,offhand = None,):
        self.equipamento['mainhand'] = mainhand
        self.equipamento['armor'] = armor
        #self.equipamento['offhand'] = offhand
        #mainhand
        for slot in self.equipamento.keys():
            for bon in self.equipamento[slot].enchant.keys():
                if bon == 'damage':
                    continue
                self.bonusequip[bon] = self.bonusequip.get(bon,0) + self.equipamento[slot].enchant[bon]

    def unequip(self,mainhand):
        self.equipamento['mainhand'] = mainhand
        for slot in self.equipamento.keys():
            for x in self.atributes.keys():
                if not self.equipamento[slot] == None:
                    if self.equipamento[slot].enchant.has_key(x):
                        self.atritutes[x] -= self.equipamento[slot].enchant[x]
        for slot in self.equipamento.keys():
            for x in self.skills.keys():
                if not self.equipamento[slot] == None:
                    if self.equipamento[slot].enchant.has_key(x):
                        self.skills[x] -= self.equipamento[slot].enchant[x]
    def seconddamage(self):
        if self.equipamento['offhand'].__class__.__name__ == 'Weapon':
            print 'do attacker'
    def selfdamage(self):
        aaa = self.equipamento['mainhand']
        a = random.randint(aaa.armatributos['danomin'],aaa.armatributos['danomax'])
        a = (aaa.armatributos['danomin']+aaa.armatributos['danomax'])/2
        b = aaa.armatributos['multiplicadordano']*(aaa.enchant['damage']+ self.modifroll(0,aaa.armaskills['atkskill'],5)+self.modifroll(*damage_list)   )
        c = aaa.armatributos['multiplicadoratr']*self.atributes[aaa.armaskills['danoatr']]*2
        return a+b+c/self.equipamento['mainhand'].armatributos['AS']
    def damage(self,target):
        aaa = self.equipamento['mainhand']
        a = random.randint(aaa.armatributos['danomin'],aaa.armatributos['danomax'])
        #a = (aaa.armatributos['danomin']+aaa.armatributos['danomax'])/2
        b = aaa.armatributos['multiplicadordano']*(self.modifroll(0,aaa.armaskills['atkskill'],5)+self.modifroll(*damage_list)-target.modifroll(*damage_list))
        c = aaa.armatributos['multiplicadoratr']*self.atributes[aaa.armaskills['danoatr']]*2
        return a+b+c - target.modifroll(0,'prot',1) + aaa.enchant['damage']
    def skillroll(self, skill, target = None):
        x, y, z = 0,0,0
        if skill in self.skills:
            x = self.skills[skill]
        elif skill in self.atributes:
            x = self.atributes[skill]
        elif skill in self.modif:
            x = self.modif[skill]
        elif skill in self.defesas:
            x = self.defesas[skill]
        else:
            x = self.resist[skill]
        try:
            y = self.bonusequip[skill]
        except:
            y = 0
        for bon in self.bonustemp.keys():
            try:
                z += self.bonustemp[bon][skill]
            except:
                z += 0
        return x + y + z
    @classmethod
    def caster(cls,name,nv):
        caster = Char(name,nv)
        for x in caster.atributes:
            if x == 'sab' or x == 'int':
                caster.atributes[x] += randATR()
            else:
                caster.atributes[x] += randatr()
        for x in caster.skills:
            if x == 'magery' or x == 'lore' or x == 'arcanery' or x == 'necromancy':
                caster.skills[x] += randSKILL()
            else:
                caster.skills[x] += randskill()
        #criar arma principal
        mainhand = Weapon(nv,'catalyst',random.choice(weapons['catalyst'].keys()))
        if weapons['catalyst'][mainhand.arma] == 'grande':
            offhand = '2handed'
        else:
            offhand =  None
        #criar armadura
        armor = Armor(nv,'leve',random.choice(armors['leve']))
        caster.equip(mainhand, armor)
        caster.PVMAX()
        return caster
class Armor:
    def __init__(self,nv, categoria, armadura, enchant = {}):
        self.nv = nv
        self.categoria = categoria
        self.armadura = armadura
        self.enchant = enchant
        #pega atributos base da armadura
        for key, atr in armorstype[categoria].items():
            self.enchant[key] = atr
        #joga atributos mágicos da armadura
class Offhand:
    def __init__(self,nv,categoria,enchant = {}, mfchance = 0):
        self.enchant = enchant
        self.nv = nv
        self.categoria = categoria
class Weapon:
    def __init__(self,nv,categoria,arma,enchant = {}, mfchance = 0):
        self.enchant = enchant
        self.nv = nv
        self.categoria = categoria
        self.arma = arma
        '''pegar atributos de acordo com a arma'''
        self.armatributos = {}
        for key, atr in weaponssize[weapons[categoria][arma]].items():
            self.armatributos[key] = atr
        '''pegar skills e atr usados pelo personagem para ataque com a arma'''
        self.armaskills = {}
        for key, s in weaponstype[categoria].items():
            self.armaskills[key] = s
        '''chance da arma ser encantada, unica ou legendaria e sorteia os bonus dela'''
        if len(enchant) == 0:
            self.enchant = dict(magicweapons)
            roll = random.randint(1,10000) + mfchance
            #print roll
            #'''legendaria'''
            #if roll + mfchance <= 10:
            #    self.enchant = legendaryweapons
            #    for x in range(len(self.enchant)-1):
            #        elf.enchant.pop(random.choice(self.enchant.keys()),None)
            #'''unica'''
            #elif roll + mfchance <= 100:
            #    self.enchant = uniqueweapons
            #    for x in range(len(self.enchant)-1):
            #        elf.enchant.pop(random.choice(self.enchant.keys()),None)
            '''magica'''
            if roll  <= 4000:
                for enchant in self.enchant.keys():
                    self.enchant[enchant] += randbonusarma(nv,self.enchant[enchant])
                self.enchant['damage'] = int(self.enchant['damage'] * self.armatributos['multiplicadordano'])
                #tira um atributo random, com exceção de 'damage'
                for x in range(4):
                    y = self.enchant.keys()
                    print x,y
                    y.pop(y.index('damage'))
                    self.enchant.pop(random.choice(y),None)
            #superior atualiza o valor dos enchants para o NV
            elif roll <= 7500:

                for enchant in self.enchant.keys():
                    self.enchant[enchant] += randbonusarma(nv,self.enchant[enchant])
                self.enchant['damage'] = int(self.enchant['damage'] * self.armatributos['multiplicadordano'])
                #tira um atributo random, com exceção de 'damage'
                for x in range(5):
                    y = self.enchant.keys()
                    print x,y
                    y.pop(y.index('damage'))
                    self.enchant.pop(random.choice(y),None)
            else:
                self.enchant = {'damage':4,'AT':0}
                for x in self.enchant.keys():
                    self.enchant[x] += randbonusarma(nv,self.enchant[x])
                self.enchant['damage'] = int(self.enchant['damage'] * self.armatributos['multiplicadordano'])
            '''multiplicar os bonus de acordo com o tamanho da arma'''

            #self.armatributos['danomin'] -= self.enchant['damage']/4
            #self.armatributos['danomax'] += self.enchant['damage']/4
            if weapons[self.categoria][self.arma] == 'grande':
                for x in self.enchant.keys():
                    if x != 'damage' and x != 'AT': self.enchant[x] *= 2
            print self.enchant


def randATR():
    b = 0
    for j in range(15):
        b += random.randint(0,1)
    return b-5
def randatr():
    b = 0
    for j in range(5):
        b += random.randint(-1,1)
    return b
def randSKILL():
    b = 0
    for j in range(15):
        b += random.randint(0,1)
    return b-5
def randskill():
    b = 0
    for j in range(10):
        b += random.randint(-1,1)
    return b

def randbonusarma(nv,x):
    b = nv/2*x
    for j in range(b):
        b += random.randint(-1,1)
    return b
def autoattack(attacker,defender):
    crit = False
    hit = False
    counter = False
    z = random.randint(1,100)
    a = attacker.atkroll(attacker.equipamento['mainhand'])
    b = defender.evaderoll()
    if z + a - b >= 100 - (attacker.modifroll(*crit_list)-defender.modifroll(*resil_list)):
        crit = True
    if z + a - b >= 50:
        hit = True
    if z + a - b <= defender.modifroll(0,'counterrating',1):
        counter = True
    if counter:
        d = defender.damage(attacker)
        print 'Counter attack!!!---', attacker.name , 'received', d,'damage'
        attacker.pontos['PV'] -= d
        print attacker.name, 'has', attacker.pontos['PV'], 'PVs'
    if hit:
        d = attacker.damage(defender)
        if crit:
            print 'Crit!!!'
            d *= 2
        print "It's a hit!!!----", attacker.name, 'caused', d, 'damage'
        defender.pontos['PV'] -= attacker.damage(defender)
        print defender.name, 'has', defender.pontos['PV'], 'PVs'
    if hit == False:
        print attacker.name, 'Missed'
    #{'AT':,'evade':,'AE':,'resist':,'AS':,'crit':,'resil':,'defesa':,'atr':,'pontos':,'stagen':,'damage':,'damagered':,'prot':,'skills':}
magicarmor = {'bonus':{'evade':1,'resil':1,'damagered':1,'magicred':5},
                'resist':{'atordoamento':2,'enfraquecimento':2,
                    'lentidao':2,'cegueira':2,'maldição':2},
                'defesa':{'cutting':1,'smashing':1,'piercing':1,'magia':1}}
magicweapons = {'AS':1,'resil':1,'crit':1,'AE':1,'evade':1,'damage':8,'AT':1}
magicoffhand = {'evade':1,'AE':1,'AS':1,'crit':1,'resil':1,}
rareweapons = {'assassin':'0','sadic':'1'}
uniqueweapons = {}
legendaryweapons = {}

#d_char = {}
#d_char['abc'] = Char.caster('Goblin Mage',1)
#print weapons['catalyst'][d_char['abc'].equipamento['mainhand'].arma]
#print d_char['abc'].equipamento['mainhand'].enchant
##print d_char['abc'].damage()
##time.sleep(d_char['abc'].equipamento['mainhand'].armatributos['AS'])
#d_char['abc'].bonustemp['moral']['parry'] = 10
#print d_char['abc'].skillroll('parry',d_char['abc'])
#print d_char['abc'].damage()#/(60/(d_char['abc'].equipamento['mainhand'].armatributos['AS']*(1-d_char['abc'].modifroll(*AS_list)/100)))
#print d_char['abc'].equipamento['mainhand'].armatributos['AS']*(1-d_char['abc'].modifroll(*AS_list)/100)

monstros = {}
monstros['1'] = Char.caster('Goblin Mage',1)
monstros['2'] = Char.caster('Robgoblin Shaman',1)
attack1 = monstros['1'].atkspd('mainhand')
attack2 = monstros['2'].atkspd('mainhand')
#specatk1 = monstros['1'].atkesp()
#specatk2 = monstros['2'].atkesp()
print monstros['1'].selfdamage()
print monstros['2'].selfdamage()
print monstros['1'].equipamento['mainhand'].armatributos['danomin'],monstros['1'].equipamento['mainhand'].armatributos['danomax']
print monstros['2'].equipamento['mainhand'].armatributos['danomin'],monstros['2'].equipamento['mainhand'].armatributos['danomax']
t = 1
for x in monstros['1'].atributes:
    print monstros['1'].atributes[x]
while monstros['1'].pontos['PV'] > 0 and monstros['2'].pontos['PV'] > 0:

    print 'time ==', t
    if attack1 <= 0:
        autoattack(monstros['1'],monstros['2'])
        attack1 += monstros['1'].equipamento['mainhand'].armatributos['AS']

    if attack2 <= 0:
        autoattack(monstros['2'],monstros['1'])

        attack2 += monstros['2'].equipamento['mainhand'].armatributos['AS']

    attack1 -= 1
    attack2 -= 1
    t += 1
    #time.sleep(1)
print monstros['1'].pontos['PV']
print monstros['2'].pontos['PV']
c =  monstros['1'].skills.keys()
c.sort()
print c
