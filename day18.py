f = open('day18.txt', 'r')
configuration = f.read().splitlines()
f.close()
house = []

for row in range(len(configuration)):
    house.append([])
    for light in configuration[row]:
        if light == "#":
            house[row].append(1)
        else:
            house[row].append(0)
    house[row] = tuple(house[row])
house = tuple(house)

def findneighbors(row, col, house):
    if row == 0:
        #TL, TR, T
        if col == 0:
            #R, B, BR
            return "corner"
            #return house[row][col + 1], house[row + 1][col], house[row + 1][col + 1]
        elif col == len(house[0]) - 1:
            #B, L, BL
            return "corner"
            #return house[row + 1][col], house[row][col - 1], house[row + 1][col - 1]
        else:
            #R, B, L, BR, BL
            return house[row][col + 1], house[row + 1][col], house[row][col - 1], house[row + 1][col + 1], house[row + 1][col - 1]
    elif row == len(house) - 1:
        #BL, BR, B
        if col == 0:
            #T, R, TR
            return "corner"
            #return house[row - 1][col], house[row][col + 1], house[row - 1][col + 1]
        elif col == len(house[0]) - 1:
            #T, L, TL
            return "corner"
            #return house[row - 1][col], house[row][col - 1], house[row - 1][col - 1]
        else:
            #T, R, L, TR, TL
            return house[row - 1][col], house[row][col + 1], house[row][col - 1], house[row - 1][col + 1], house[row - 1][col - 1]
    else:
        #L, R, MID
        if col == 0:
            #T, R, B, TR, BR
            return house[row - 1][col], house[row][col + 1], house[row + 1][col], house[row - 1][col + 1], house[row + 1][col + 1]
            
        elif col == len(house[0]) - 1:
            #T, B, L, BL, TL
             return house[row - 1][col], house[row + 1][col], house[row][col - 1], house[row + 1][col - 1], house[row - 1][col - 1]
            
        else:
            #T, R, B, L, TR, BR, BL, TL
            return house[row - 1][col], house[row][col + 1], house[row + 1][col], house[row][col - 1], house[row - 1][col + 1], house[row + 1][col + 1], house[row + 1][col - 1], house[row - 1][col - 1]    
def animate(house):
    newHouse = []
    for row in house:
        newHouse.append(list(row))
    for row in range(len(house)):
        for col in range(len(house[row])):
            if house[row][col]:
                if findneighbors(row, col, house) == "corner":
                    newHouse[row][col] = 1
                elif not (2 <= findneighbors(row, col, house).count(1) <= 3):
                    newHouse[row][col] = 0
                    #print row, col, "off"
            else:
                #print row, col, findneighbors(row, col, house)
                if findneighbors(row, col, house).count(1) == 3:
                    newHouse[row][col] = 1
                    #print row, col, "on"
    house = []
    for row in newHouse:
        house.append(tuple(row))
    return tuple(house)
for x in range(100):
    house = animate(house)
count = 0
for row in house:
    count += row.count(1)


#'''
                    
