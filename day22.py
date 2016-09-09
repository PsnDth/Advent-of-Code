    # Flatten:
    #derivative = [range(2), range(3), range(4)]
    #derivative = [item for drv in derivative for item in drv]
def product(list1, list2):
    for x in list2:
        copy = list(list1)
        copy.append(x)
        yield copy
class Boss:
    hp = 71
    dmg = 10
class Wizard:
    def __init__(self):
        self.effects = {}
        self.manaUsed = 0
        self.armor = 0
        self.hp = 50
        self.mana = 500
        
        pass
    def magicMissle(self):
        dmg = 4 + self.effect()
        #print "Player Casts magic missle."
        self.mana -= 53
        self.manaUsed += 53
        return dmg
    def shield(self):
        dmg = 0 + self.effect()
        #print "Player Casts Shield. Timer is now 6"
        self.mana -= 113
        self.manaUsed += 113
        self.effects["shield"] = 6
        return dmg
    def drain(self):
        dmg = 2 + self.effect()
        #print "Player Casts Drain."
        self.mana -= 73
        self.manaUsed += 73
        self.hp += 2
        return dmg
    def poison(self):
        dmg = 0 + self.effect()
        #print "Player Casts Poison. Timer is now 6"
        self.manaUsed += 173
        self.mana -= 173
        self.effects["poison"] = 6
        return dmg
    def recharge(self):
        dmg = 0 + self.effect()
        #print "Player Casts Recharge. Timer is now 6"
        self.mana -= 229
        self.manaUsed += 229
        self.effects["recharge"] = 5
        return dmg
        #effect happens at the beginning of an attack
    def effect(self):
        totalDmg = 0
        for effect in self.effects.keys():
            self.effects[effect] -= 1
            #print effect + " timer is now " + str(self.effects[effect])
            if effect == "shield":
                self.armor = 7
            elif effect == "recharge":
                #print "recharge provides 101 mana."
                self.mana += 101
            else:
                #print "poison does 3 dmg"
                totalDmg += 3
            if self.effects[effect] == 0:
                #print effect + " wears off."
                del self.effects[effect]
                if effect == "shield":
                    self.armor = 0
        return totalDmg
effects = ["poison", "shield", "recharge"]
def playGame(sequence):
    player = Wizard()
    boss = Boss()
    #print sequence
    while boss.hp > 0 and player.hp > 0 and player.mana > 0 and len(sequence) > 0:
        attack = sequence.pop(0)
        player.hp -= 1
        if player.hp <= 0:
            break
        if attack in effects and attack in player.effects:
            if player.effects[attack] != 1:
                return "lose"
        #print "player has " + str(player.hp) + " hp and " + str(player.mana) + " mana."
        #print "Boss has " + str(boss.hp) + " hp"
        boss.hp -= getattr(player, attack)()
        if boss.hp <= 0:
            break
        if player.mana < 0:
            break
        #print "player has " + str(player.hp) + " hp and " + str(player.mana) + " mana."
        #print "Boss has " + str(boss.hp) + " hp. Player has " + str(player.armor) + " armor"
        if boss.dmg > player.armor:
            boss.hp -= player.effect()
            if boss.hp <= 0:
                break
            player.hp -= boss.dmg - player.armor
            #print "Boss does " + str(boss.dmg - player.armor) + " dmg"
        else:
            boss.hp -= player.effect()
            if boss.hp <= 0:
                break
            player.hp -= 1
            #print "Boss does 1 dmg!"
    if player.hp <= 0 or player.mana < 0:
        return "lose"
    elif boss.hp <= 0:
        #print player.hp, boss.hp
        #print player.mana, player.manaUsed
        return player.manaUsed
    else:
        return 0
def findManaCost(sequence):
    manaCost = {
        "magicMissle": 53,
        "drain": 73,
        "shield": 113,
        "poison": 173,
        "recharge": 229
        }
    total = 0
    for attack in sequence:
        total += manaCost[attack]
    return total
def playGameSimple(sequence):
    boss = {
        "hp": 71,
        "dmg": 10,
        }
    player = {
        "hp":50,
        "armor": 0,
        "mana": 500,
        "effects": {}
        }
    for attack in sequence:
        #apply effects
        for effect in player["effects"].keys():
            player["effects"][effect] -= 1
            if player["effects"][effect] == 0:
                del player["effects"][effect]
            if effect == "psn":
                boss["hp"] -= 3
            elif effect == "shield":
                player["armor"] = 7
            elif effect == "rchrg":
                player["mana"] += 101
        #player apply
        if attack == "magicMissle":
            player["mana"] -= 53
            boss["hp"] -= 4
        elif attack == "drain":
            player["mana"] -= 73
            player["hp"] += 2
            boss["hp"] -= 2
        elif attack == "shield":
            if "shield" not in player["effects"]:
                player["mana"] -= 113
                player["effects"]["shield"] = 6
            else:
                return 0
        elif attack == "poison":
            if "psn" not in player["effects"]:
                player["mana"] -= 173
                player["effects"]["psn"] = 6
            else:
                return 0
        elif attack == "recharge":
            if "rchrg" not in player["effects"]:
                player["mana"] -= 229
                player["effects"]["rchrg"] = 5
            else:
                return 0
        if player["mana"] <= 0:
            break
        for effect in player["effects"].keys():
            player["effects"][effect] -= 1
            if player["effects"][effect] == 0:
                del player["effects"][effect]
            if effect == "psn":
                boss["hp"] -= 3
            elif effect == "shield":
                player["armor"] = 7
            elif effect == "rchrg":
                player["mana"] += 101
        if boss["hp"] <= 0:
            break
        else:
            player["hp"] -= boss["dmg"] - player["armor"]
            if player["hp"] <= 0:
                break
    if player["hp"] < 0 or player["mana"] < 0:
        return "lose"
    elif boss["hp"] <= 0:
        #print player.hp, boss.hp
        #print player.mana
        return findManaCost(sequence)
    else:
        return 0
            
                
    


sequences = [('drain', 'poison', 'magicMissle', 'recharge', 'poison', 'magicMissle', 'magicMissle', 'poison', 'magicMissle'),
('magicMissle', 'magicMissle', 'poison', 'drain', 'recharge', 'poison', 'magicMissle', 'magicMissle', 'poison'),
('magicMissle', 'magicMissle', 'poison', 'drain', 'magicMissle', 'poison', 'recharge', 'magicMissle', 'poison'),
('magicMissle', 'poison', 'drain', 'magicMissle', 'poison', 'magicMissle', 'recharge', 'poison', 'magicMissle'),
('magicMissle', 'recharge', 'poison', 'magicMissle', 'drain', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('drain', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'poison', 'recharge', 'magicMissle', 'magicMissle'),
('magicMissle', 'magicMissle', 'poison', 'magicMissle', 'drain', 'poison', 'recharge', 'magicMissle', 'magicMissle'),
('magicMissle', 'drain', 'poison', 'recharge', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('recharge', 'magicMissle', 'poison', 'shield', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('magicMissle', 'shield', 'poison', 'magicMissle', 'magicMissle', 'poison', 'recharge', 'magicMissle', 'magicMissle'),
('magicMissle', 'shield', 'poison', 'recharge', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('shield', 'magicMissle', 'poison', 'magicMissle', 'recharge', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('recharge', 'shield', 'poison', 'magicMissle', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('magicMissle', 'shield', 'poison', 'magicMissle', 'recharge', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('shield', 'recharge', 'poison', 'magicMissle', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('drain', 'recharge', 'poison', 'magicMissle', 'drain', 'poison', 'magicMissle', 'magicMissle', 'magicMissle'),
('drain', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'poison', 'recharge', 'drain', 'magicMissle'),
('magicMissle', 'drain', 'poison', 'magicMissle', 'recharge', 'poison', 'drain', 'magicMissle', 'magicMissle'),
('drain', 'drain', 'poison', 'magicMissle', 'magicMissle', 'poison', 'recharge', 'magicMissle', 'magicMissle'),
('magicMissle', 'drain', 'poison', 'magicMissle', 'recharge', 'poison', 'magicMissle', 'drain', 'magicMissle'),
('drain', 'recharge', 'poison', 'drain', 'magicMissle', 'poison', 'magicMissle', 'magicMissle', 'magicMissle')]
#'''
attacks = ["poison", "magicMissle", "drain", "shield", "recharge"]
paths = [[attack] for attack in attacks]
paths = sorted(paths, key=lambda x: findManaCost(x))
done = False
lowest = 0
while len(paths) > 0:
    pathHolder = []
    for path in range(len(paths)):
        sequence = list(paths[path])
        result = playGame(paths[path])
        if type(result) is int and result:
            if not lowest:
                print sequence, result
                lowest = result
                break
        elif not result:
            for newPath in product(sequence, attacks):  
                    pathHolder.append(list(newPath))
    if lowest:
        break
    paths = sorted(pathHolder, key=lambda x: findManaCost(x))
    print len(paths), len(paths[0])
    #paths[0]
#''' 
    
     
'''
    next steps:
        sort the resulting combos in permutations by cost
    create combinations of attacks (of increasing lengths),
    then playGame with each sequence and find cheapest one. Shorter battle length = shorter mana cost theoretically.
'''

            
            
        
