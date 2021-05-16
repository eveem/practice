n = raw_input().split(' ')
n = [int(i) for i in n]

h = n[1]

s = raw_input().split(' ')
s = [int(i) for i in s]

s.sort()
s.reverse()

s = [i for i in s if i > 0]

r = 1
if len(s) != 0:
    b = s[0]
rank = []
p = 0
k = 0

for i in s:
    if i != b:
        r += k
        k = 1
    else:
        k += 1
    b = i
    rank.append(r)
    p += 1

re = 0

for i in rank:
    if i <= h:
        re += 1
    
print re