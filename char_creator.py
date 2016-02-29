import const as C
import config
import Chars
def create_combat():
    for x in ['roggar','miggah','kaifro','ziltan','potrak']:
        y = Chars.Monster.t_play(x,1)
        config.players.append(y)
    for x in ['goblin warrior','goblin mage','goblin cleric','goblin assassin','goblin shaman']:
        y = Chars.Monster.brute(x,1)
        config.monsters.append(y)
if __name__ == "__main__":
    for x in range(5):
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
        while awsr == False:
            skill2 = raw_input('What is your secondary skill')
            if skill2 in C.skills_list:
                awsr = True
        while awsr == False:
            skill3 = raw_input('What is your tertiary skill')
            if skill3 in C.skills_list:
                awsr = True        
        player = Char.Player(str,agi,vit,wis,int,skill1,30,skill2,20,skill3,10)
        config.players.append(player)