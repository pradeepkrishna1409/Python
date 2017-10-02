class stack:

    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def push(self,item ):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def seek(self):
        return self.items[len(self.items)-1]



class get_min_stack:

    def __init__(self):
        self.stack=[]
        self.min=[]

    def stack_push(self,x):
        self.stack.append(x)
        if not self.min or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop_stack(self):
        print self.min

