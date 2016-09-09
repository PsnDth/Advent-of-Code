vowels = 'aeiou'
def isNice(string):
    '''
    vowelCount = 0
    doubleLetter = False
    for vowel in vowels:
        vowelCount += string.count(vowel)
    if vowelCount < 3:
        return False
    if ('ab' in string) or ('cd' in string) or ('pq' in string) or ('xy' in string):
        return False
    for ch in range(len(string) - 1):
        if string[ch] == string[ch + 1]:
            return True
    else:
        return False
    ^ PART 1 ^
    '''
    #Part 2
    hasPairs = False
    hasBoB = False
    for letter in range(len(string) - 1):
        pair = string[letter] + string[letter + 1]
        if string.count(pair) > 1:
            hasPairs = True
        if letter != len(string) - 2:
            if string[letter] == string[letter + 2]:
                hasBoB = True
    if hasBoB and hasPairs:
        return True
    else:
        return False
                
    
f = open('day5.txt', 'r')
strings = f.read().splitlines()
count = 0
for string in strings:
    if isNice(string):
        count += 1
f.close()
print count
