class QuickUnionUF:
    def __init__(self, n):
        self.id = [i for i in range(n)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id[self.root(p)] = self.root(q)
