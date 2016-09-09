alpha = map(chr, range(ord('a'), ord('z') + 1))
def increment(string):
    outpt = string
    current = alpha.index(string[-1])
    new = ""
    pos = -1
    while True:
        if current != 25:
            new = alpha[current + 1] + new
            outpt = string[:pos] + new
            break
        else:
            new = "a" + new
            pos -= 1
            if pos == - 1 - len(string):
                new = "a" + new
                outpt = new
                break
            else:
                current = alpha.index(string[pos])
    return outpt
    
def has2Pairs(string):
    pair1 = ""
    pair2 = ""
    for letter in range(len(string) - 1):
        if string[letter] == pair1:
            continue
        if string[letter] == string[letter + 1]:
            if pair1:
                pair2 = string[letter]
                return True
            else:
                pair1 = string[letter]
    return False
def notConfusing(string):
    confusing = "iol"
    for letter in confusing:
        if letter in string:
            return False
    return True
def checkConseq(string):
    for char in range(len(string) - 2):
        i = alpha.index(string[char])
        j = alpha.index(string[char + 1])
        k = alpha.index(string[char + 2])
        if  j == i + 1 and k == j + 1:
            return True
    return False

#NextPwd
current = "cqjxxyzz"
current =   increment(current)
while True:
    
    if has2Pairs(current) and checkConseq(current) and notConfusing(current):
        print current
        break
    else:
        current = increment(current)

    
