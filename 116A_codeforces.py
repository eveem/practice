n = int(raw_input())

c = 0
mx = 0

for i in range(n):
    a, b = raw_input().split(' ')
    c -= int(a)
    c += int(b)
    if c > mx:
        mx = c
    
print mx
    