'''
import math
def factorize(x):
    for num in range(int(math.ceil(x**0.5)), x + 1):
        if not x % num:
            yield num
            if x / num != num:
                yield x / num
def lazyFactorize(x):
    if x < 50:
        for  num in factorize(x):
            yield num
    else:
        for num in range(x/50, x + 1):
            if  not x % num:
                yield num
                if x / num != num:
                    yield x / num
perfectNums = [(2**(num-1))*(2**num - 1) for num in [2,3]]
def isAbundant(x):
    if sum(lazyFactorize(x)) - x > x:
        return True
    return False

gotIt = False
#too slow for part 2
num =  6
abundants = list(perfectNums)
while not gotIt:
    if 10*sum(factorize(num)) >= 36000000:
        gotIt = True
        print num
    num += 6
'''
# ^ not good enough, prolly becuase of alot of numbers, and variables etc
from math import ceil, sqrt
def genFactors(num):
    for x in range(1,int(sqrt(num)) + 1):
        if not num % x:
            yield x
            if x ** 2 != num:
                yield num / x
def genLazyFactors(num):
    for x in range(1,int(sqrt(num)) + 1):
        if not num % x and x * 50 >= num:
            yield x
        if not num % x and x ** 2 != num and (50*num)/x >= num:
            yield num / x
ans = 0
num = 1
'''
#Part 1
while not ans:
	presentsDelivered = sum(tuple(genFactors(num)))
	if 10*presentsDelivered >= 36000000:
		ans = presentsDelivered
		break
	num += 1
'''
#Part 2
while not ans:
	presentsDelivered = sum(tuple(genLazyFactors(num)))
	if 11*presentsDelivered >= 36000000:
		ans = presentsDelivered
		break
	num += 1
            


      


