f = open('day8.txt', 'r')
strings = f.read().splitlines()
f.close()
new = []
count = 0
for string in strings:
    newString = string.replace('\\', '\\\\')
    newString = newString.replace('"', r'\"')
    newString = r'"' + newString + r'"'
    count += len(newString) - len(string)
    
print count
