import math

def isPrime (n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(2, 1000000):
    if isPrime(i):
        count += 1
    if count == 10001:
        print i
        break