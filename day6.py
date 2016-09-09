house = [[0]*1000 for light in range(1000)]
def lightUp(instr):
    command = ""
    instr = instr.split(" ")
    if instr[0] != "turn": start = [int(pos) for pos in instr[1].split(",")]
    end = [int(pos) for pos in instr[-1].split(",")]
    command = instr[0]
    if instr[0] == "turn":
        command =  instr[0]+ " "+ instr[1]
        start = [int(pos) for pos in instr[2].split(",")]
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            if command == "toggle":
                house[row][col] += 2
            elif command == "turn on":
                house[row][col] += 1
            else:
                if house[row][col] > 0:
                    house[row][col] -= 1

f = open('day6.txt', 'r')
instructions = f.read().splitlines()
f.close()
for instruction in instructions:
    lightUp(instruction)
lit = 0
for row in range(len(house)):
    for col in range(len(house[row])):
            lit += house[row][col]
print lit

    
    
