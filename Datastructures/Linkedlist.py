class Node:
  def __init__(self,val):
    self.val = val
    self.nxt = None


class Linkedlist:

  def __init__(self,item):
    self.head=Node(item)

  def add(self,item):
     curr=self.head
     while curr.nxt is not None:
         curr=curr.nxt
     curr.nxt=Node(item)


  def print_lst(self):
    curr=self.head
    str1=""
    while curr is not None:
      str1 += "[ " + str(curr.val) + " ] --> "
      curr=curr.nxt
    print str1


  def remove(self,item):
      curr=self.head
      prev=None
      found= False
      while not found:
          if curr.val==item:
              found=True
          else:
              prev=curr
              curr=curr.nxt

      if prev==None:
          self.head=curr.nxt
      else:
          prev.nxt=curr.nxt

  def reverse_list(self):
      curr=self.head
      prev=None
      while curr is not None:
          temp=curr.nxt
          curr.nxt=prev
          prev=curr
          curr=temp
      self.head=prev


  def kthnode_last(self,k):
      p1=self.head
      p2=self.head

      for i in range(k):
          p2=p2.nxt

      while p2.nxt is not None:
          p1=p1.nxt
          p2=p2.nxt

      print p1.val


  def delete_duplicate(self):
        cur = self.head
        dict = {}
        prev = None
        while cur is not None:
            if cur.val in dict:
                prev.next = cur.next
            else:
                dict[cur.val]= True
                prev = cur
            cur = cur.next


  def parition(ll, key):
    cur = ll.getHead()
    pre = None
    post = None
    while cur is not None:
        if cur.val != key:
            if cur.val > key:
                if post is None:
                    post = Linkedlist(cur.val)
                else:
                    post.add(cur.val)
            elif cur.val < key:
                if pre is None:
                    pre = Linkedlist(cur.val)
                else:
                    pre.add(cur.val)
        cur = cur.next

    cur = pre.getHead()
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(key)
    cur.next.next = post.getHead()
    return pre.printlist()


   def swapNodes(self, x, y):
      # Nothing to do if x and y are same
      if x == y:
          return

      # Search for x (keep track of prevX and CurrX)
      prevX = None
      currX = self.head
      while currX != None and currX.data != x:
          prevX = currX
          currX = currX.next

      # Search for y (keep track of prevY and currY)
      prevY = None
      currY = self.head
      while currY != None and currY.data != y:
          prevY = currY
          currY = currY.next

      # If either x or y is not present, nothing to do
      if currX == None or currY == None:
          return
      # If x is not head of linked list
      if prevX != None:
          prevX.next = currY
      else: #make y the new head
          self.head = currY

      # If y is not head of linked list
      if prevY != None:
          prevY.next = currX
      else: # make x the new head
          self.head = currX

      # Swap next pointers
      temp = currX.next
      currX.next = currY.next
      currY.next = temp


  def FindMiddle(self):
        slow = self.head
        fast = self.head
        #until valid next node
        while fast.next is not None:
            #2 jump?
            if fast.next.next:
                fast = fast.next.next #reaches end
                slow = slow.next      #reaches middle
            #1 ump - find second middle if #nodes is even
            else:
                fast = fast.next  #reaches end
                slow = slow.next  #reaches middle
        return slow.data

  def add_numbers_linkedlist(list1, list2):
    v1 = list1.getHead()
    v2 = list2.getHead()
    carry = 0
    while v1 is not None:
        val = ((v1.val + v2.val) % 10) + carry
        carry = (v1.val + v2.val) // 10
        v1.val = val
        v1 = v1.next
        v2 = v2.next

    cur = list1.getHead()
    val = 0
    mul = 1
    while cur is not None:
        val = val + (cur.val * mul)
        mul = mul * 10
        cur = cur.next
    return val







L=Linkedlist(3)
L.add(10)
L.add(100)
L.add(200)
L.print_lst()
#L.remove(10)
#L.print_lst()
#L.reverse_list()
#L.print_lst()
#L.kthnode_last(2)

# L1=Linkedlist(1)
# L1.add(100)
# L1.add(200)
# L1.add(301)
# L1.print_lst()

L.swap()
L.print_lst()


def Intersection(nodeA,nodeB):
    #nodeA will hold the result
    resultHead = None
    result =  None
    while nodeA and nodeB:
        if nodeA.val == nodeB.val:  #match
            tmp = nodeA  #nodeA will hold the result
            nodeA = nodeA.next
            nodeB = nodeB.next
            if resultHead is None:
                resultHead = tmp
                result = tmp
                result.next = None
            else:
                result.next = tmp
                result = tmp
                result.next = None
        elif nodeA.data > nodeB.data:
            nodeB = nodeB.next
        else:
            nodeA = nodeA.next
    return resultHead

#print Intersection(L,L1)










