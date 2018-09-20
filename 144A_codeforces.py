n = input()
x = input().split(' ')
x = [int(i) for i in x]

s, m, M, pm, pM = 0, 0, 0, 0, 0

for i in range(len(x)):
    if x[i] <= m or i == 0:
        m = x[i]
        pm = i
    if x[i] > M or i == 0:
        M = x[i]
        pM = i

if x[0] == M and x[len(x) - 1] == m:
    print(0)
else:
    if pM < pm:
        s += pM
        s += len(x) - pm
    else:
        s += pM
        s += len(x) - pm - 1

    print(s - 1)