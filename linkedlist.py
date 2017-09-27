class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):
        self.head=None

    def add(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head=temp

    def size(self):
        curr = self.head
        count=0

        while curr is not None:
            curr = curr.next
            count +=1

        return count

    def search(self,data):
        curr = self.head
        found = False

        while curr is not None and not found:
            if curr.data == data:
                found = True
            else:
                curr = curr.next

        return found

    def remove(self,data):
        curr= self.head
        prev = None
        found = False

        while  curr is not None and not found:
            if curr.data == data:
                found = True
            else:
                prev= curr
                curr = curr.next

        if prev is None:
            self.head = curr.next
        else:
            prev.set_next(curr.next)


    def remove_dups(self):
        curr= self.head
        dict = {}
        prev= None


        while curr.next is not None:
            if curr.data in dict:
                prev.next = curr.next
            else:
                dict[curr.data] = True
                prev=curr
                curr = curr.next



l = linkedlist()
l.add(10)
l.add(23)
l.add(45)
l.add(99)
print l.size()
print l.size()
print l.print_list()


