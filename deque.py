""" deque data structure usage as a stack """

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(f'popping from stack: {stack.pop()}')
print(f'peeking the stack: {stack[-1]}')
