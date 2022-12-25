class Node:
    def __init__(self,val):
        self.data = val
        self.children = []
    
class Tree:
    # Constructor
    def __init__(self) -> None:
        self.root = None
        self.num_nodes = 0
    
    # Function to get the Height / Depth of tree
    def height(self):
        return self.__height(self.root)

    def __height(self,node):
        h = 0
        for child in node.children:
            ch = self.height(child)
            h = max(h,ch)
        h+=1
        return h


    # Function to print tree
    # in Pre-Order Traversal
    def preOrder(self):
        return self.__preOrder(self.root)

    def __preOrder(self,node):
        Order = []
        if node:
            Order.append(node.data)
            for child in node.children:
                Order+=self.__preOrder(child)
        return Order
    
    # Function to print tree
    # in Post-Order Traversal
    def postOrder(self):
        return self.__postOrder(self.root)

    def __preOrder(self,node):
        Order = []
        if node:
            for child in node.children:
                Order+=self.__postOrder(child)
            Order.append(node.data)
        return Order
    

    # Function to print tree
    # in Level-Order Traversal
    def levelOrder(self):
        return self.__levelOrder(self.root)

    def __levelOrder(self,root):
        Order = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            Order.append(node.data)
            for child in node.children:
                queue.append(child)
        return Order
    
    def take_input(self):
        self.root = self.__take_input()

    def __take_input(self):
        queue = []
        n = int(input("Enter root \n"))
        root = Node(n)
        queue.append(root)
        while queue:
            front = queue.pop(0)
            num_child = int(input("Enter number of children of {} => \n".format(front.data)))
            for i in range(num_child):
                data = int(input("Enter child data of {} => \n".format(front.data)))
                node = Node(data)
                front.children.append(node)
                queue.append(node)
        return root

    

# Driver Code

T = Tree()
T.take_input()
print(T.levelOrder())