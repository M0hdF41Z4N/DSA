# Stack Implementation Using Doubly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self,item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
            self.size+=1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next
            self.size+=1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            data = self.tail.data
            self.tail = self.tail.prev
            self.size -= 1

        if self.isEmpty():
            self.head = None
        
        else :
            self.tail.next = None # Memory Cleanup
        return data

    def peek(self):
        return self.tail.data

    def isEmpty(self):
        return self.size == 0

    def stack_size(self):
        return self.size

    def traverse(self):
        if self.isEmpty():
            return "Stack is Empty"            
        
        trav = self.head
        print("---------------")
        while trav :
            print(trav.data,end="\n")
            trav = trav.next
        
        print("---------------")
        return
    
# Driver Code

s = Stack()
s.traverse()
for i in range(1,5):
    s.push(i)

s.traverse()
print(s.peek())
print(s.pop())
print(s.peek())
s.traverse()