import math

def isPrime (n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True

result = 0

for i in range(2, 2000000):
    if isPrime(i):
        result += i
    
print result