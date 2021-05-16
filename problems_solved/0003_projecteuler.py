import math

def isPrime (n):
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True

# goal = 13195
goal = 600851475143
for i in range(int(math.sqrt(goal)), 2, -1):
    if goal % i == 0 and isPrime(i):
        print i
        break

