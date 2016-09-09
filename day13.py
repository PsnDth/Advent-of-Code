import itertools
f = open('day13.txt', 'r')
seats = f.read().splitlines()
f.close()
family = []
relations = {}
happyLevel = {}
for person in seats:
    person = person.split()
    if person[2] == "gain":
        relations["-".join([person[0], person[-1].strip(".")])] = int(person[3])
    else:
        relations["-".join([person[0], person[-1].strip(".")])] = - int(person[3])
    if person[0] not in family:
        family.append(person[0])
for person in family:
    relations["self-" + person] = 0
    relations[person + "-self"] = 0
family.append("self")
    
arrangements = [arrangement for arrangement in itertools.permutations(family)]
for arrangement in arrangements:
    totalHappyLevel = 0
    for person in range(len(arrangement) - 1 ):
        name = "-".join([arrangement[person], arrangement[person + 1]])
        revName = "-".join([arrangement[person], arrangement[person - 1]])
        totalHappyLevel += relations[name]
        totalHappyLevel += relations[revName]
    totalHappyLevel += relations["-".join([arrangement[-1], arrangement[0]])]
    totalHappyLevel += relations["-".join([arrangement[-1], arrangement[-2]])]
    happyLevel["-".join(arrangement)] = totalHappyLevel
print max(happyLevel.values())
