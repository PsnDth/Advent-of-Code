f = open('day16.txt', 'r')
aunts = f.read().splitlines()
f.close()
auntStats = []
ticker = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
    }
theAunt = []
for aunt in aunts:
    auntStat = {}
    auntStr = aunt.split()[2:]
    for stat in range(len(auntStr)/2):
        auntStat[auntStr[2*stat].strip(":")] = int(auntStr[2*stat + 1].strip(","))
    auntStats.append(auntStat)
for auntNum in range(len(auntStats)):
    aunt = auntStats[auntNum]
    isSue = True
    for info in aunt:
            if info == "cats" or info == "trees":
                if aunt[info] < ticker[info]:
                    isSue = False
                    break
            elif info == "pomeranians" or info == "goldfish":
                if aunt[info] > ticker[info]:
                    isSue = False
                    break
            else:
                if ticker[info] != aunt[info]:
                    isSue = False
                    break
    if isSue:
        theAunt.append(aunt)
        print auntNum, aunt
        
    
