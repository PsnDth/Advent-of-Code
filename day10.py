puzzle = "1113122113"
'''
def lookSay(num):
    num = str(num)
    output = ""
    prevNum = num[0]
    countNum = 0
    for digit in range(len(num)):
        pos = digit
        digit = num[digit]
        if prevNum == digit:
            countNum += 1
        else:
            output += str(countNum) + num[pos - 1]
            countNum = 1
        if pos == len(num) - 1:
            output += str(countNum) + digit
        prevNum = digit
    return output
for i in range(50):
    print i
    puzzle = int(lookSay(puzzle))
print len(str(puzzle))
'''
def lookSay(num):
    new = ""
    #num is in an array
    for i in range(len(num)/2):
        # 2i is current
        # 2i + 1 is partner
        # 2i + 2 is following neighbour (1st of pair)
        # 2i - 1 is leading neighbour (2nd of pair)
        if num[2*i] != num[2*i + 1]:
            #if pair not equal
            if i != 0:
                #if first not same as previous
                if num[2*i] != num[2*i - 1]:
                    new += "1" + num[2*i]
            else:
                new += "1" + num[2*i]
            if 2*i + 2 != len(num):
                #if second not same / same as next
                if num[2*i + 1] != num[2*i + 2]:
                    new += "1" + num[2*i + 1]
                else:
                    new += "2" + num[2*i + 1]
            else:
                new += "1" + num[2*i + 1]
            
        else:
            #if pair is equal
            if 2*i + 2 != len(num):
                #if second same as next / not same as next
                if num[2*i + 1] != num[2*i + 2]:
                    new += "2" + num[2*i]
                else:
                    new += "3" + num[2*i]
            else:
                new += "2" + num[2*i + 1]
    return new
for i in range(50):
    print i
    puzzle = lookSay(puzzle)
print len(str(puzzle))
        

