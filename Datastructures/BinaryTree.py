count=0
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        #test purpose lists
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    def remove(self, item):
        if self.head.val is None:
            print ("there is no item: in BST", item)
        if self.head.val == item:
            # 1) Node to be removed has no children.
            if self.head.left is None and self.head.right is None:
                self.head = None
            # 2) Node to be removed has one child.
            elif self.head.left is None and self.head.right is not None:
                self.head.val = self.head.right.val
                self.head.right = None
            # 2) Node to be removed has one child.
            elif self.head.left is not None and self.head.right is None:
                self.head.val = self.head.left.val
                self.head.left = None
            # 3) Node to be removed has two children.
            else:
                self.head.val = self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print ("There is no item: ", item)
        if cur.val == item:
            # 1) Node to be removed has no children.
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            # 2) Node to be removed has one child.
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            # 2) Node to be removed has one child.
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            # 3) Node to be removed has two children.
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)


    def __most_left_val_from_right_node(self, cur):
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print (cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print cur.val

        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        print (cur.val)


    def __VBST(self,curr,min,max):
        if curr is None:
            return True
        if curr.val <= min or curr.val >= max:
            return False
        return self.__VBST(curr.left,min,curr.val) and self.__VBST(curr.right,curr.val,max)

    def Check_Valid_BST(self):
        return self.__VBST(self.head,-2147483648,2147483647)

    def findLt(self,root,k):

        global count
        if root is None:
            return None

        if root.right is not None:
            self.findLt(root.right,k)

        count+=1

        if count==k:
            print root.val
            return root

        if root.left is not None:
            self.findLt(root.left,k)



    def find_kth_largt(self):
        return self.findLt(self.head,2)



    def find_largets(self):
        return self.maxValue(self.head)


    def maxValue(self,node):
        if node.right:
            return self.maxValue(node.right)
        else:
            return node.val

    def isBalancedBinaryTreeWrapper(self,root):
        if root is None:
            return 0
        lheight = self.isBalancedBinaryTreeWrapper(root.left)
        rheight = self.isBalancedBinaryTreeWrapper(root.right)
        #Kill if height of sub-trees > 1
        if abs(lheight-rheight) > 1:
            return -1
        #return height of sub-tree
        return max(lheight,rheight) + 1

    def Balanced_call(self):
        return self.isBalancedBinaryTreeWrapper(self.head)

    def _max_val(self,cur,maxv):
        if cur is None:
            return maxv

        if cur.val > maxv:
            maxv=cur.val

        lmax= self._max_val(cur.left,maxv)
        rmax= self._max_val(cur.right,maxv)

        return max(lmax,rmax)

    def max_val(self):
        return self._max_val(self.head,self.head.val)

    def leafSum(node):
        if node is None:
            print("node is None")
            return 0
        elif node.left is None and node.right is None:
            return node.data
        else:
            return leafSum(node.left) + leafSum(node.right)

    def cloneBT(self,node):
        if node is None:
            return

        newNode = BinaryTree(node.data)
        newNode.left = self.cloneBT(node.left)
        newNode.right = self.cloneBT(node.right)
        return newNode

    def leftLeafSum(node,left=None):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            #IMPORTANT: left leaf nodes!
            return node.data if left else 0
        else:
            return leftLeafSum(node.left,True)+leftLeafSum(node.right,False)



    def flipTree(node):
        if node is None:
            return
        node.left,node.right = node.right,node.left
        flipTree(node.left)
        flipTree(node.right)

    def CheckMirror(t1,t2):
        #condition1: both nodes are empty
        if (t1 is None and t2 is None):
            return True
        #condition 2: one of the nodes is empty
        elif( t1 is None or t2 is None):
            return False
        #condition 3: data does not match
        elif( t1.getData() != t2.getData()):
            return False
        #condition 4: check for subnodes
        else:
            return CheckMirror(t1.getLeft(),t2.getRight()) and  CheckMirror(t1.getRight(),t2.getLeft())


    def findPathSum(self,node,path=[],path_sum=0):
        if node is None:
            return
        path_sum += node.val
        path.append(node.val)
        if node.left is None and node.right is None:
            print("%s sum=%d" % (path,path_sum))
        else:
            self.findPathSum(node.left,path,path_sum) if node.left else None
            self.findPathSum(node.right,path,path_sum) if node.right else None
            path.pop()
            path_sum -= node.val


bt = BinaryTree()
bt.add(10)
bt.add(5)
bt.add(13)
bt.add(1)
bt.add(8)


#bt.inorder_traverse()
#bt.remove(5)
print "-------"
#bt.inorder_traverse()

#print bt.isbalanced()

#print bt.Balanced_call()

bt.find_kth_largt()
