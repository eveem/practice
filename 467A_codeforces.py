n = int(raw_input())
c = 0
for i in range(n):
    s = map(int, raw_input().split())
    if s[1] - s[0] > 1:
        c += 1
    
print c
