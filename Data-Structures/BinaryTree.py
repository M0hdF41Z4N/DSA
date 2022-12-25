#   Binary Tree Implementation

class Node:
    # Constructor
    def __init__(self,val):
        self.data = val
        self.left = self.right = None
    
class binary_tree:
    # Constructor
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    # Function to return the height of binary tree
    def height(self):
        return self.__height(self.root)

    def __height(self,node):
        if node == None:
            return 0
        return max(self.__height(node.left) , self.__height(node.right)) + 1

    # Function to build binary tree using pre-order traversal and in-order traversal
    def build_using_in_pre_order(self,inOrder,inStart,inEnd,preOrder,preStart,preEnd):
        if (preStart>preEnd or inStart>inEnd):
            return None

		# Assigning root
        root = Node(preOrder[preStart])
		
		# Parting using root
        k = 0
        for i in range(inStart,inEnd+1):
            if (inOrder[i] == root.data):
                k = i
                break

		# Attaching left and right subtree
        root.left = self.build_using_in_pre_order(preOrder, preStart+1 , preStart + (k-inStart) , inOrder , inStart ,k-1)

        root.right = self.build_using_in_pre_order(preOrder,preStart+(k-inStart)+1,preEnd,inOrder,k+1,inEnd)
        return root
    
    # Function to build binary tree using post-order traversal and in-order traversal
    def build_using_in_post_order(self,inOrder,inStart,inEnd,postOrder,postStart,postEnd):
        if (postStart>postEnd or inStart>inEnd):
            return None

		# Assigning root
        root = Node(postOrder[postEnd])
		
		# Parting using root
        k = 0
        for i in range(inStart,inEnd+1):
            if (inOrder[i] == root.data):
                k = i
                break

		# Attaching left and right subtree
        root.left = self.build_using_in_post_order(postOrder, postStart , postStart + (k-inStart-1) , inOrder , inStart ,k-1)

        root.right = self.build_using_in_post_order(postOrder,postStart+(k-inStart),postEnd-1,inOrder,k+1,inEnd)
        return root

    def build(self,inOrder,preOrder):
        inStart = preStart = 0
        inEnd = preEnd = len(inOrder)
        self.root = self.build_using_in_pre_order(inOrder,inStart,inEnd,preOrder,preStart,preEnd)

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

    # Function to check that Binary Tree is balanced or not
    def check_balance(self):
        height , bal = self.__check_balance(self.root)
        return bal

    def __check_balance(self,root):
        if root == None:
            height = 0
            is_bal = True
            return height,is_bal
        left_height , left_bal = self.__check_balance(root.left)
        right_height , right_bal = self.__check_balance(root.right)
        is_bal = True
        height = 1+max(left_height,right_height)

        if (abs(left_height-right_height)>1):
            is_bal = False
        if ((not left_bal) or (not right_bal)):
            is_bal = False

        return height,is_bal

    # Function to print the more detail tree
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

def take_tree_input(root,parent,left):
    if root:
        print("Enter root data : ")
    else:
        if left:
            print("Enter left data : {}".format(parent.data))
        else:
            print("Enter right data : {}".format(parent.data))
    n = int(input())
    if n == -1:
        return
    root = Node(n)
    root.left = take_tree_input(False,root,True)
    root.right = take_tree_input(False,root,False)
    return root



# Driver Code

if __name__ == "__main__":
    BT = binary_tree()
    i = take_tree_input(True,0,True)
    BT.root = i
    BT.print()
    print(BT.check_balance())
