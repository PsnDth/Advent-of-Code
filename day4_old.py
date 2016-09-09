import hashlib
def check(string):
    num = 0
    bit = hashlib.md5()
    while [bit.hexdigest()[x] for x in range(5)].count('0') != 5:
        bit = hashlib.md5(string + str(num))
    return x, bit.hexdigest()
