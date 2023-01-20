""" Last in first out (LIFO) stack data structure python implementation as a class"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(f'popping from stack: {s.pop()}')  # 3
print(f'popping from stack: {s.pop()}')  # 2
print(f'is empty: {s.is_empty()}')  # False
print(f'size: {s.size()}')  # 1

