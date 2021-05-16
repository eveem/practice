fib = [1, 2]
i = 0
j = 1
s = 2

while True:
    n = fib[i] + fib[j]
    i = j
    j += 1
    if (n > 4000000):
        break
    if n % 2 == 0:
        s += n
    fib.append(n)

print s