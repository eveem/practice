class UnorderedMaxPQ:
    def __init__(self):
        self.pq = []
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def insert(self, x):
        self.pq.append(x)
        self.n += 1

    def exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def del_max(self):
        maxx = 0
        for i in range(1, self.n):
            if self.pq[maxx] < self.pq[i]:
                maxx = i

        self.exch(maxx, self.n - 1)
        self.n -= 1
        return p[self.n]
