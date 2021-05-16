class UF:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return

        if self.rank[parent_p] >= self.rank[parent_q]:
            self.parent[parent_q] = parent_p
            self.rank[parent_p] = max(self.rank[parent_q] + 1, self.rank[parent_p])
        else:
            self.parent[parent_p] = parent_q
            self.rank[parent_q] = max(self.rank[parent_p] + 1, self.rank[parent_q])

    def find(self, p):
        parent = self.parent[p]
        while parent != p:
            p = parent
            parent = self.parent[p]
        return parent

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return len(set(self.rank))


uf = UF(10)

for i in range(8):
    p, q = map(int, input().split())
    if not uf.connected(p, q):
        uf.union(p, q)

print(uf.count())
