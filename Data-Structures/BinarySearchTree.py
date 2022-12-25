#   Binary Search Tree Implementation

# Search O(logn) / O(h)
# delete O(h)
# insert O(logn)



import sys

class Node:
    # Constructor
    def __init__(self,val):
        self.data = val
        self.left = self.right = None

class BST:
    # Constructor
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.nodeCount
    
    def __remove(self,node,item):
        if node is None :
            return None
        
        cmp = item < node.data

        if item == node.data:
          

            # Case I : when root have two children , then find max/min of subtree
            if node.right is not None and node.left is not None:
                tmp =  self.__findMin(node.right)
                node.data = tmp.data
                # Goto right subtree and delete leftmost element and swapped data with.
                # This prevents from having two nodes in our tree with same value
                node.right = self.__remove(node.right,tmp.data)

            # Case I : when root have only single child left or right

            elif node.left == None:
                rightChild = node.right
                node.data = None
                node = None
                return rightChild
            elif node.right == None:
                leftChild =  node.left
                node.data = None
                node = None
                return leftChild
            else:
                return None

        elif cmp is True:
            node.left = self.__remove(node.left,item)
        elif cmp is False:
            node.right =  self.__remove(node.right,item)

        else:
            return None

        return node

    def remove(self,item):
        if self.contains(item):
            self.root = self.__remove(self.root,item)
            self.nodeCount -= 1
            return True
        else:
            return False



    def findMin(self):
        return self.__findMin(self.root)

    def __findMin(self,node):
        while node.left :
            node = node.left
        return node

    def findMax(self):
        return self.__findMax(self.root)

    def __findMax(self,node):
        while node.right :
            node = node.right
        return node

    # Function to check wheather value already
    # exists in binary tree or not
    def contains(self,item):
        return self.__contains(item,self.root)

    def __contains(self,item,node):
        if node:
            if node.data == item :
                #print("found")
                return True
            elif node.data < item :
                #print("right")
                return self.__contains(item,node.right)
            else :
                #print("left")
                return self.__contains(item,node.left)
        else:
            #print("Not found")
            return False


    # Function to return the height of binary tree
    def height(self):
        return self.__height(self.root)

    def __height(self,node):
        if node == None:
            return 0
        return max(self.__height(node.left) , self.__height(node.right)) + 1

    


    # Function to add values in binary tree
    def __add(self,item,node):
        if node is None :
            node = Node(item)
        else:
           if node.data < item:
               node.right = self.__add(item,node.right)
           else:
               node.left = self.__add(item,node.left)
        return node 


    def add(self,item):
        
        # Check if the value already exists in this
        # binary tree, if it does ignore adding

        if self.contains(item):
            return False
        else:
            self.root = self.__add(item,self.root)
            self.nodeCount += 1
            return True


    # Function to print binary search tree
    # in Pre-Order Traversal
    def preOrder(self):
        return self.__preOrder(self.root)

    def __preOrder(self,node):
        Order = []
        if node:
            Order.append(node.data)
            Order+=self.__preOrder(node.left)
            Order+=self.__preOrder(node.right)
        return Order

    
    # Iterative Method
    #def preOrderTraversal(self):
    #    stack = [self.root]
    #    Order = []
    #    while stack:
    #        node = stack.pop()
    #        Order.append(node.data)
    #        if node.right :
    #            stack.append(node.right)
    #        if node.left :
    #            stack.append(node.left)
    #    return Order
   

    # Function to print binary search tree
    # in Post-Order Traversal
    def postOrder(self):
        return self.__postOrder(self.root)

    
    # Recursive approach

    def __postOrder(self,node):
    # code here
        Order = []
        if node != None:
            Order+=self.__postOrder(node.left)
            Order+=self.__postOrder(node.right)
            Order.append(node.data)
        return Order

    # Function to print binary search tree
    # in In-Order Traversal
    def inOrder(self):
        return self.__inOrder(self.root)


    
    # Recursive Approach
    def __inOrder(self,node):
        Order = []
        if node:
            Order+=self.__inOrder(node.left)
            Order.append(node.data)
            Order+=self.__inOrder(node.right)
        return Order
    

    """
    # Iterative Method
    def inOrderTraversal(self):
        stack = []
        Order = []
        curr = self.root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                Order.append(curr.data)
                curr = curr.right
            else:
                break
        return Order
    """

    # Function to print binary search tree
    # in Level-Order Traversal
    def levelOrder(self):
        return self.__levelOrder(self.root)

    def __levelOrder(self,root):
        # Iterative Method
        Order = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            Order.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return Order

    def print(self):
        return self.__print(self.root)
    
    def __print(self,root):
        Order = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data,": ",end="",sep="")
            Order.append(node.data)
            if node.left:
                print("L:{0},".format(node.left.data),end="")
                queue.append(node.left)
            if node.right:
                print("R:{0}".format(node.right.data),end="")
                queue.append(node.right)
            print("\n")
    
    # Function to check wheather BST is Valid or Not

    def __check_BST(self,node,min_range,max_range):
        if node is None:
            return True
        
        if node.data < min_range or node.data > max_range:
            return False
        
        left = self.__check_BST(node.left,min_range,node.data-1)
        right = self.__check_BST(node.right,node.data,max_range)

        return left and right
    
    def check_BST(self):
        return self.__check_BST(self.root,-sys.maxsize,sys.maxsize)

    # Function to build BST using sorted array
    def build(self,arr):
        self.root = self.__build(arr,0,len(arr)-1)

    def __build(self,arr,low,high):
        if low <= high:
            mid = (low+high)//2
            node = Node(arr[mid])
            node.left = self.__build(arr,low,mid-1)
            node.right = self.__build(arr,mid+1,high)
            return node
        else:
            return None
    
    # Function to check that Binary Search tree is balanced or not
    def balance(self):
        pass
        


  
    
# Driver code

tree = BST()
# print(tree.add(7))
# print(tree.add(8))
# print(tree.add(6))
# print(tree.print())
# print(tree.inOrder())
# print(tree.preOrder())
# print(tree.postOrder())
# print(tree.check_BST())
#print(tree.add(1))
#print(tree.add(3))
#print(tree.add(4))
#print(tree.add(10))
#print(tree.add(14))

# print(tree.contains(9))
#print(tree.add(6))



# print(tree.preOrderTraversal())
#print(tree.findMin().data)
#print(tree.findMax().data)
#print(tree.remove(6))
#print(tree.contains(6))
#print(tree.preOrderTraversal())


#print(tree.height())
# tree.build([1,2,3,4,5,6,7])
# tree.print()