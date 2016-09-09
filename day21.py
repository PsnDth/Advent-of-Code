weapons = {}
armor = {"none": {"cost":0, "dmg": 0, "armor":0}}
rings = {}
hero = {
    "hp": 100,
    "armor": 0,
    "dmg": 0
    }
boss = {
    "hp": 100,
    "dmg": 8,
    "armor": 2
    }
weaponStats = ["Dagger 8 4 0",
"Shortsword 10 5 0",
"Longsword 40 7 0",
"Greataxe 74 8 0"]
armorStats = ["Leather 13 0 1",
"Chainmail 31 0 2",
"Splintmail 53 0 3",
"Bandedmail 75 0 4",
"Platemail 102 0 5"]
ringStats = ["Damage+1 25 1 0",
"Damage+2 50 2 0",
"Damage+3 100 3 0",
"Defense+1 20 0 1",
"Defense+2 40 0 2",
"Defense+3 80 0 3"]
for stat in ringStats:
    info = stat.split()
    rings[info[0]] = {
        "cost": int(info[1]),
        "dmg": int(info[2]),
        "armor": int(info[3])
        }
for stat in weaponStats:
    info = stat.split()
    weapons[info[0]] = {
        "cost": int(info[1]),
        "dmg": int(info[2]),
        "armor": int(info[3])
        }
for stat in armorStats:
    info = stat.split()
    armor[info[0]] = {
        "cost": int(info[1]),
        "dmg": int(info[2]),
        "armor": int(info[3])
        }
#^^SET UP ARRAYS^^#
from itertools import product, combinations
combos = {}
for numRings in range(3):
    for combo in product(weapons, armor, combinations(rings, numRings)):
        comboCost = 0
        for element in range(len(combo)):
            if element == 2:
                for ring in combo[element]:
                    comboCost += rings[ring]["cost"]
            elif element == 1:
                comboCost += armor[combo[element]]["cost"]
            else:
                comboCost += weapons[combo[element]]["cost"]
        combos[combo] = comboCost
#go through each combination starting from cheapest
def beatBoss(stats):
	dps = stats["dmg"] - boss["armor"]
	if dps <= 0: dps = 1
	bossDps = boss["dmg"] - stats["armor"]
	if bossDps <= 0: bossDps = 1
	if dps >= bossDps:
		return True
	else:
		return False
for combo in reversed(sorted(combos, key=combos.get)):
    stats = hero.copy()
    for element in range(len(combo)):
            if element == 2:
                for ring in combo[element]:
                    stats["armor"] += rings[ring]["armor"]
                    stats["dmg"] += rings[ring]["dmg"]
            elif element == 1:
                stats["armor"] += armor[combo[element]]["armor"]
            else:
                stats["dmg"] += weapons[combo[element]]["dmg"]
    if not beatBoss(stats):
        print combo, combos[combo]
        break
    
