# Stack implementation using Singly linked list

class Node:
    def __init__(self,data_val):
        self.data =  data_val
        self.next = None

class Stack:
    # Constructor to initialize a node
    def __init__(self):
        self.head = None

    
    # Function to push element in stack
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to find stack is empty or not
    def Is_Empty(self):
        return self.head == None

    # Function to pop element from stack
    def pop(self):
        if self.Is_Empty() :
            return False
        temp_node = self.head
        self.head = self.head.next
        popped = temp_node.data
        temp_node =  None # Memory Cleanup
        return popped

    # Function return the peek of the stack
    def peek(self):
        if self.Is_Empty() :
            return
        return self.head.data
        
    
    # Function to print stack 
    def Display(self):
        if self.Is_Empty():
            return "Stack is Empty"
        temp_node = self.head
        while temp_node != None :
            print('%d ->'%temp_node.data, end = "")
            temp_node = temp_node.next
        print("\n")
        
        
# Driver Code

s = Stack()
s.Display()
s.push(9)
s.push(7)
s.push(8)
s.Display()
print("popped element ",s.pop())
s.Display()