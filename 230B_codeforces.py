import math

prime_status = [0, 0, 1, 1] + [1] * 1000000

def sieve():
    for i in range(2, 1000001):
        if prime_status[i] == 1:
            for j in range(i + i, 1000001, i):
                prime_status[j] = 0

    # for i in range(2, len(prime_status)):
    #     print str(i) + " " + str(prime_status[i])

n = int(raw_input())
p = raw_input().split(' ')
p = [int(i) for i in p]

sieve()

# T-primes = 1, sqrt(t), t

for i in range(0, n):
    sq = int(math.sqrt(p[i]))
    if sq**2 == p[i] and prime_status[sq] == 1:
        print "YES"
    else:
        print "NO"