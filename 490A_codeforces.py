n = int(input())
arr = [int(i) for i in input().split()]
d = {1: [], 2: [], 3: []}

for i, j in enumerate(arr):
    d[j].append(i + 1)

m = min(min(len(d[1]), len(d[2])), len(d[3]))

print(m)

for i in range(m):
    print(d[1][i], d[2][i], d[3][i])