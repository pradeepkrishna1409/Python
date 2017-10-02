class Stack:
    def __init__(self):
        self.items = []

    # method for pushing an item on a stack
    def push(self, item):
        self.items.append(item)

    # method for popping an item from a stack
    def pop(self):
        return self.items.pop()

    # method to check whether the stack is empty or not
    def isEmpty(self):
        return (self.items == [])

    # method to get the top of the stack
    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

def findingSpans(A):
    D = Stack()
    S = [None] * len(A)
    for i in range (0, len(A)):
        while not D.isEmpty() and A[i] > A[D.peek()]:
                D.pop()
        if D.isEmpty():
            P = -1
        else:
            P = D.peek()
        S[i] = i - P
        D.push(i)
    print S

findingSpans(['6', '3', '4', '5', '2'])