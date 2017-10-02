class stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



def func_bal_checker(str):
    stack_par = stack()
    balanced = True
    pos=0

    while balanced and pos< len(str):
        print("Position at \n", pos)
        if str[pos]=="{":
            stack_par.push(str[pos])
        else:
            if stack_par.is_empty():
                balanced=False
            else:
                stack_par.pop()
        pos = pos + 1


    if balanced and stack_par.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    print("Balance checker function")
    func_bal_checker("{{}}")