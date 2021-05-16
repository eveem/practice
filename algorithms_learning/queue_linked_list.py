class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item)
        self.last.next = None
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item


x = LinkedQueue()
x.enqueue(91)
x.enqueue(12)
print(x.dequeue())
print(x.dequeue())
print(x.is_empty())
