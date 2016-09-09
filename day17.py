from itertools import combinations
f = open('day17.txt', 'r')
containers = f.read().splitlines()
f.close()
containers = [int(container) for container in containers]
sample = containers[:7]

#combiner
sums = []
minLen = 0
for length in range(3,len(containers)):
	for combo in combinations(containers, length):
		if sum(combo) == 150:
			sums.append(combo)
for combo in sums:
    if len(combo) == 4:
        minLen += 1
print minLen
