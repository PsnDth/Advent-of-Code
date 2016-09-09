import json
f = open('day12.txt', 'r')
encoded = f.read().splitlines()
f.close()

#Part 1
'''
for string in encoded:
    numString =  ""
    for char in range(len(string)):
        if string[char] == "-" or string[char].isdigit():
            numString += string[char]
        if char != len(string) - 1 :
            if (not string[char + 1].isdigit()) and numString:
                total += int(numString)
                numString = ""
    print total
'''
encoded = json.loads(encoded[0])
totalSum = 0
def loopthru(var, typ):
        if typ is int:
            global totalSum
            totalSum += var
        elif typ is dict:
            if u"red" not in var.values() and u"red" not in var.keys():
                for value in var.values():
                    loopthru(value, type(value))
        elif typ is list:
                for value in var:
                    loopthru(value, type(value))
loopthru(encoded, type(encoded))
print totalSum
            
            
