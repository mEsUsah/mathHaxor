import random

def generateNumber(siphers, maxNumber=None):
    if maxNumber and maxNumber <= (10**(siphers))-1:
        return random.randint(10**(siphers-1), maxNumber)

    return random.randint(10**(siphers-1), (10**(siphers))-1)

def randomPosition(a, b):
    if random.randint(0, 1) == 0:
        return a, b
    else:
        return b, a