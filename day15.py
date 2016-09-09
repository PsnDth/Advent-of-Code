#helper
from itertools import combinations, chain, permutations, combinations_with_replacement
from math import floor

def genpairsto(num):
    x = 1
    while x <= floor(num/2):
        yield (x, num - x)
        x += 1
    
def genpartsto(num, limit):
    if limit == 0:
        yield ()
    elif limit == 1:
        yield (10,)
    elif limit == 2:
        for pair in genpairsto(num):
            yield pair
    else:
        for combination in list(combinations_with_replacement(range(1, num - 2), limit - 2)):
            if sum(combination) + 2 <= num:
                for pair in genpairsto(num - sum(combination)):
                    yield tuple(sorted(combination + pair))


f = open('day15.txt', 'r')
ingredients = f.read().splitlines()
f.close()
stats = {}
names = []
for ingredient in ingredients:
    ingredient = ingredient.split()
    name = ingredient[0].strip(":")
    calories = ingredient[-1]
    texture = ingredient[-3].strip(",")
    flavor = ingredient[-5].strip(",")
    durability = ingredient[-7].strip(",")
    capacity = ingredient[-9].strip(",")
    names.append(name)
    stats[name] = {
        "capacity": int(capacity),
        "durability": int(durability),
        "flavor": int(flavor),
        "texture": int(texture),
        "calories": int(calories)
        }
def calculateScore( amounts):
    scores = [0,0,0,0]
    totalScore = 1
        
    for ingredient in stats:
        amount = amounts[ingredient]
        scores[0]+= stats[ingredient]["capacity"] * amount
        scores[1]+= stats[ingredient]["durability"] * amount
        scores[2]+= stats[ingredient]["flavor"] * amount
        scores[3]+= stats[ingredient]["texture"] * amount
    for score in scores:
        if score > 0:
            totalScore = score * totalScore
    return totalScore
scores = []
def calorieCount(amounts):
    total = 0
    for ingredient,amount in amounts.iteritems():
        total += stats[ingredient]["calories"] * amount
    return total
'''

print len(list(permutations(names)))
combos = sumTo(20,2)
for combo in combos:
    print combo
'''
for part in genpartsto(100, len(names)):
    for combo in permutations(part):
        amounts = {names[k]: combo[k] for k in range(len(names))}
        if calorieCount(amounts) == 500:
            scores.append(calculateScore({names[k]: combo[k] for k in range(len(names))}))
print max(scores)
