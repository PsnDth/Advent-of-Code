f = open('day23.txt', 'r')
instructions = f.read().splitlines()
f.close()
registers = {
    "a": 1,
    "b": 0
    }
def run(function):
    function = function.split()
    register = function[1].strip(",")
    if function[0] == "inc":
        registers[register] += 1
        return 1
    if function[0] == "hlf":
        registers[register] = registers[register] / 2
        return 1
    if function[0] == "tpl":
        registers[register] = registers[register] * 3
        return 1
    if function[0] == "jmp":
        return int(register)
    if function[0] == "jio":
        if registers[register] == 1:
            return int(function[2])
        else:
            return 1
    if function[0] == "jie":
        if registers[register] % 2 == 0:
            return int(function[2])
        else:
            return 1
#instructions = ["inc a","jio a, +2","tpl a", "inc a"]
done = False
current = 0
while not done:
    nxt = run(instructions[current])
    #print current, instructions[current]
    #for register in registers:
    #   print register, registers[register]
    if current + nxt > 0  and current + nxt < len(instructions):
        current += nxt
    else:
        break
print registers
