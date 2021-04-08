ans = 0

n, m = [int(i) for i in input().split(" ")]
a = [0] + list(map(int, input().split(" ")))
d = [[] for _ in range(n + 1)]

for i in range(n - 1):
    x, y = [int(j) for j in input().split(" ")]
    d[x].append(y)
    d[y].append(x)

# n = 7
# m = 1
# a = [0] + [1, 0, 1, 1, 0, 0, 0]
# d = [[], [2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3], [3]]

# n = 4
# m = 1
# a = [0] + [1, 1, 0, 0]
# d = [[], [2, 3, 4], [1], [1], [1]]

vis = [False for _ in range(n + 1)]


def dfs(node, count):
    if a[node] == 1:
        count += 1
    else:
        count = 0

    if count > m:
        return
    vis[node] = True
    leaf = True

    for i in d[node]:
        if not vis[i]:
            leaf = False
            dfs(i, count)

    if leaf:
        global ans
        ans += 1


dfs(1, 0)
print(ans)
