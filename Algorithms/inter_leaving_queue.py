import Queue

class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

que = Queue()

def inter_leaving_queue(que):
    stk =Stack()
    halfsize = que.size//2

    for i in range(halfsize):
        stk.push(que.)