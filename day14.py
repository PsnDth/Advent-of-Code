import math
f = open('day14.txt', 'r')
stats = f.read().splitlines()
f.close()
reindeers = {}
distances = {}
score = {}
duration = 2503
for idt in range(len(stats)):
    info = stats[idt].split()
    reindeers[info[0]] = [int(info[3]), int(info[6]), int(info[-2])]
    score[info[0]] = 0
'''
#Day 1
for idt in reindeers:
    reindeer = reindeers[idt]
    speed = int(reindeer[0])
    time = int(reindeer[1])
    rest = int(reindeer[2])
    
    distance = speed*(time*math.floor(duration/( time + rest) ))
    if  duration %(time + rest) <= time:
        distance += speed *( duration %(time + rest ))
    else:
        distance  += speed * time
    distances[idt] = distance

print max(distances.values())
'''
#Day 2
for second in range(1,duration + 1):
    for idt in reindeers:
        second = int(second)
        reindeer = reindeers[idt]
        speed = int(reindeer[0])
        time = int(reindeer[1])
        rest = int(reindeer[2])

        distance = speed *(time*math.floor(second/( time + rest) ))
        if  second %(time + rest) <= time:
            distance += speed *( second %(time + rest ))
        else:
            distance  += speed * time
        distances[idt] = distance
    leaderboard = sorted(distances.items(),key=lambda x: x[1])[::-1]
    for leader in range(len(leaderboard)):
        if leader == 0:
            score[leaderboard[leader][0]] += 1
        elif leaderboard[leader][1] == leaderboard[0][1]:
            score[leaderboard[leader][0]] += 1
        else:
            break

print max(score.values())

