class MaxPQ:
    def __init__(self):
        self.pq = []
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t

    def swim(self, k):
        while k > 1 and self.less(k // 2, k):
            self.exch(k, k // 2)
            k = k // 2

    def insert(self, x):
        self.n += 1
        self.pq.append(x)
        self.swim(self.n)

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j + 1):
                j += 1
            if not self.less(k, j):
                break
            self.exch(k, j)
            k = j

    def del_max(self):
        maxx = self.pq[1]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        self.pq[self.n + 1] = None
        return maxx
