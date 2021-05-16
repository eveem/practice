class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedStack:
    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        self.first = Node(item)
        self.first.next = old_first

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item


x = LinkedStack()
x.push(91)
x.push(12)
print(x.pop())
print(x.is_empty())
