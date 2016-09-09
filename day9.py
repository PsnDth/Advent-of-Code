from itertools import permutations
f = open('day9.txt', 'r')
distances = f.read().splitlines()
f.close()
locations = []
#length between 2 places goes here
lengths = {}
for distance in distances:
    #save length between 2 places into length array as {"place1-place2": distance}
    lengths["-".join([distance.split(" ")[0], distance.split(" ")[2]])] = int(distance.split(" ")[4])
    location = distance.split(" ")[0]
    if location not in locations:
        locations.append(location)
    location = distance.split(" ")[2]
    if location not in locations:
        locations.append(location)
paths = [path for path in permutations(locations)]

pathLengths = {}
# {"number": ["order", length], }
for name in range(len(paths)):
    pathLength = 0
    path = paths[name]
    pathName = "-".join(path)
    for dest in range(len(path) - 1):
        dest1 = path[dest]
        dest2 = path[dest + 1]
        if "-".join([dest1, dest2]) in lengths.keys():
            pathLength += lengths["-".join([dest1, dest2])]
        else:
             pathLength += lengths["-".join([dest2, dest1])]
    pathLengths[pathName] = pathLength
    
print max(pathLengths.values())
    
