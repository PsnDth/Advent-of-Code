import hashlib
def check(string):
    num = 0
    bit = hashlib.md5()
    while bit.hexdigest().startswith('000000') != True:
        num+=1
        bit = hashlib.md5(string + str(num))
        
    return num, bit.hexdigest()
