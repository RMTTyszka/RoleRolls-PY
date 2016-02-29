atr_list = ['str','agi','vit','wis','int']
skills_list =   [
    'alchemy', 'anatomy', 'animaltaming', 'archery', 'armorcrafting', 'armslore','awareness', 
    'bowcrafting', 'carpentery', 'fencing', 'gathering', 'healing','heavyweaponship', 'jewelcrafting',
    'leatherworking', 'lore', 'lumberjacking', 'magery','meditating','mercantilism','military', 'parry','reflex', 'resistspells', 
    'skinning', 'stealth', 'swordmanship', 'tactics', 'tailoring', 'wrestling'
                ]

defenses_list = ['cutting','smashing','piercing','magic']
resist_list = ['weakness','slow','stun','blind','curse']
#Items
wep_size_list = ['heavy','medium','light']
weapons = {'catalyst':{'heavy':{'staff':'normal'},'medium':{'rod':'normal'},'light':{'wand':'normal','orb':'normal'}},
            'cutting':{'medium':{'longsword':'normal'},'light':{'dagger':'normal'},'heavy':{'Great Axe':'normal'}},
            'smashing':{'light':{'hammer': 'normal'},'medium':{'morningstar': 'normal'},'heavy':{'maul': 'normal'}}
            ,'piercing':{'light':{'dagger':'normal'},'medium':{'rapier':'normal'},'heavy':{'war pickaxe':'normal'}}}                                                                                                                                             
# wep_skills                                                                                                                                                                                                                         
wep_type = {'cutting':{'atkskill':'swordmanship','atkatr':'str','danoatr':'str'},                                                                                                                                                 
            'smashing':{'atkskill':'heavyweaponship','atkatr':'str','danoatr':'str'},                                                                                                                                                
            'piercing':{'atkskill':'fencing','atkatr':'agi','danoatr':'agi'},                                                                                                                                                        
            'ranged':{'atkskill':'archery','atkatr':'agi','danoatr':'agi'},                                                                                                                                                          
            'thrown':{'atkskill':'archery','atkatr':'agi','danoatr':'str'},                                                                                                                                                          
            'catalyst':{'atkskill':'magery','atkatr':'wis','danoatr':'wis'}}                                                                                                                                                                                                                                                                                                                                                                  
# wep_atr                                                                                                                                                                                                                       
#!/usr/bin/env python2                                                                                                                                                                                                               
# -*- coding: utf-8 -*-

wep_size_info = {'light':{'ASbase':5.0,'danomin':6,'danomax':10,'modataque':0,                                                                                                                                                           
            'dano_mult':1.2,'atr_mult':1.5,'counterrating':15,'armor_pen':0},                                                                                                                                                        
        'medium':{'ASbase':10.0,'danomin':11,'danomax':19,'modataque':0,'dano_mult':1.6,                                                                                                                                          
            'atr_mult':2,'counterrating':10,'armor_pen':0},                                                                                                                                                                                
        'heavy':{'ASbase':15.0,'danomin':14,'danomax':26,'modataque':10,'dano_mult':2.0,                                                                                                                                        
           'atr_mult':3,'counterrating':10,'armor_pen':6},                                                                                                                                                                                 }                                                                                                    
#armas = {'light':[5.0,8,12,15,0,1.0,1],'medium':[10.0,11,19,10,0,1.5,2],'heavy':[15.0,14,26,5,10,2.0,3],'duaslights':[5.0,]}
armors = {'light':('robe'),'medium': ('studded leather'),'heavy':('scale')}                                                                                                   
armorstype = {'None': {'prot':0,'evade':5},'light': {'prot':1,'evade':-1},'medium':{'prot':6,'evade':-5},'heavy':{'prot':11,'evade':-12}}                                                                                                                
                                                                                                                                                                                                         
# ordem dos atributos do tyopemonster   armadura // arma //                                                                                                                                                                          
typemonster = {'tanker':['heavy','medium',],'assassin':['light','light'],'brute':['medium','heavy'],'caster':['light','spell'],'hunter':['light','distancia'],'striker':['light','duaslights'],'ranger':['medium','duasmediums'],}           
crit_list = [15,1,'anatomy', 5 ,'crit',1]                                                                                                                                                                                                      
resil_list = [5,1, 'parry', 5, 'resil',1]                                                                                                                                                                                                    
fortitude_list = [0,1, 'parry', 5, 'vit', 5, 'fortitude', 1]                                                                                                                                                                                 
damage_list = [0,1, 'armslore', 5, 'damage', 1]
magicred_list = [0,5, 'resistspells', 5, 'int', 5, 'magicred', 5]                                                                                                                                                                
AS_list = [0,1,'AS',1]
CT_list = [0,1,'CT',1,'int',5] 
life_list = []

armor_enchants = {'bonus':{'evade':1,'resil':1,'fortitude':1,'magicred':5},                                                                                                                                                                    
                'resist':{'stun':2,'weakness':2,                                                                                                                                                                            
                    'slow':2,'blindness':2,'curse':2},                                                                                                                                                                               
                'defense':{'cutting':1,'smashing':1,'piercing':1,'spell':1}}                                                                                                                                                                
wep_enchants = {'AS':1,'resil':1,'crit':1,'AE':1,'evade':1,'damage':8,'AT':1}                                                                                                                                                              
magicoffhand = {'evade':1,'AE':1,'AS':1,'crit':1,'resil':1,}                                                                                                                                                                               
rareweapons = {'assassin':'0','sadic':'1'}
uniqueweapons = {}
legendaryweapons = {}