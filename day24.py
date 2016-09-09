from itertools import combinations
f = open('day24.txt', 'r')
containers = f.read().splitlines()
f.close()
containers = [int(container) for container in containers]
sample = containers[:7]

def product(nums):
    total = 1
    for num in nums:
        total = total * num
    return total
boxSize = sum(containers)/4
#combiner
sums = []
minLen = 0
print len(containers)/4
for length in range(len(containers)/4):
    print length, len(tuple(combinations(containers, length)))
    for combo in combinations(containers, length):
            if sum(combo) == boxSize:
                    sums.append(combo)
print len(sums)
lowest = []
minLen = len(min(sums, key=lambda x: len(x)))

print minLen
for combo in sums:
    if len(combo) == minLen:
        lowest.append(combo)
minProduct = product(min(lowest, key=lambda x: product(x)))
print minProduct
for combo in lowest:
    if product(combo) == minProduct:
            print product(combo)
