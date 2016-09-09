def parseWires(booklet):
    wires = {}
    for wire in booklet:
        
        wire = wire.split(" ")
        if len(wire) == 3 and wire[0].isdigit():
            if wire[2] == "b":
                del booklet[booklet.index(" ".join(wire))]
                wires["b"] = 46065
            else:
                del booklet[booklet.index(" ".join(wire))]
                wires[wire[2]] = int(wire[0])
    run = 0
    while "a" not in wires:
        run+= 1
        for instruction in booklet:
            command = instruction.split(" ")
            if "NOT" in command:
                if command[1] in wires:
                    wires[command[3]] = 65535 - int(wires[command[1]])
                    del booklet[booklet.index(" ".join(command))]
                elif command[1].isdigit():
                    wires[command[3]] = 65535 - int(command[1])
                    del booklet[booklet.index(" ".join(command))]
            elif "RSHIFT" in command:
                if command[0] in wires:
                     wires[command[4]] = wires[command[0]] >> int(command[2])
                     del booklet[booklet.index(" ".join(command))]
            elif "LSHIFT" in command:
                if command[0] in wires:
                    wires[command[4]] = wires[command[0]] << int(command[2])
                    del booklet[booklet.index(" ".join(command))]
            elif "AND" in command:
                if command[0] in wires and command[2] in wires:
                    wires[command[4]] = wires[command[0]] & wires[command[2]]
                    del booklet[booklet.index(" ".join(command))]
                elif command[0].isdigit() and command[2] in wires:
                    wires[command[4]] = int(command[0]) & wires[command[2]]
                    del booklet[booklet.index(" ".join(command))]
            elif "OR" in command:
                if command[0] in wires and command[2] in wires:
                    wires[command[4]] = wires[command[0]] | wires[command[2]]
                    del booklet[booklet.index(" ".join(command))]
                elif command[0].isdigit() and command[2] in wires:
                    wires[command[4]] = int(command[0]) & wires[command[2]]
                    del booklet[booklet.index(" ".join(command))]
            else:
                if command[0] in wires:
                    wires[command[2]] = wires[command[0]]
                    
                    
                
    return wires["a"]
f = open('day7.txt', 'r')
booklet = f.read().splitlines()
f.close()
print parseWires(booklet)


        
    
