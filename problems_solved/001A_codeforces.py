st = raw_input().split(' ')

n = int(st[0])
m = int(st[1])
a = int(st[2])

result = 1

if n % a == 0:
    result = n/a
else:
    result = int(n/a) + 1

if m % a == 0:
    result *= m/a
else:
    result *= int(m/a) + 1

print result