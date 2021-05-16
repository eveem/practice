class ArrayStack:
    def __init__(self):
        self.s = []
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def push(self, item):
        self.s.append(item)
        self.n += 1

    def pop(self):
        self.n -= 1
        return self.s[self.n]


x = ArrayStack()
x.push(91)
x.push(12)
print(x.pop())
print(x.is_empty())
