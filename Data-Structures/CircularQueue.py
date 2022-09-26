# Implementation of Circular Linked List
# Using Singly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
    
    
class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None
    
    # Function to add element in front of List    
    def addFront(self,key):
        new_node = Node(key)
        if self.isEmpty() :
            self.tail = new_node
            new_node.next = self.tail
            
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            
            
    # Function to add element at end of List
    def append(self,key):
        new_node = Node(key)
        if self.isEmpty() :
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
    
    def search(self,item):
        if self.isEmpty():
            return False
        trav = self.tail.next
        while trav :
            if trav.data == item:
                return trav
            trav = trav.next
            if trav == self.tail.next:
                break
        return False
        
    # Function to add element after a node of List
    def addAfter(self,data,key):
        if self.isEmpty():
            return "List is Empty"
        else:
            if self.tail.data == data:
                self.append(key)
            elif self.tail.next == data:
                self.addFront(key)
            else:
                if self.search(data):
                    prev = self.search(data)
                    new_node = Node(key)
                    new_node.next = prev.next
                    prev.next = new_node
                else:
                    return "Item not found"
            
    def traverse(self):
        if self.isEmpty():
            return "List is Empty"
        trav = self.tail.next
        while trav :
            print(trav.data,end = " -> ")
            trav = trav.next
            if trav == self.tail.next:
                break
        print("\n")

        
        
# Implementation of Circular Queue
# Using array

class Queue:
    # Constructor
    def __init__(self,k):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front = self.rear = -1



    # Function to check if queue is empty
    def isEmpty(self):
        return self.front == -1

    # Function to check if queue is full
    def isFull(self):
        return ((self.rear + 1) % self.capacity == self.front)

    # Function to add item into queue
    def enqueue(self,item):
        # Case 1: if queue is full
        if self.isFull():
            return "Queue is Full"
        # Case 2: if queue is empty
        if self.isEmpty() :
            self.front = self.rear = 0
            self.queue[self.rear] = item
        # All other cases
        else:
            self.rear = (self.rear + 1 ) % self.capacity 
            self.queue[self.rear] = item



    # Function to delete item from queue
    def dequeue(self):
        
        # Case 1 : if queue is empty
        if self.isEmpty():
            return "Queue is Empty"
        
        data = self.queue[self.front]
        
        # Case 2 : if queue is full
        if self.front == self.rear:
            self.front = self.rear = -1
            return data
        
        # All other cases
        else:
            self.front = (self.front + 1) % self.capacity 
            return data


    # Function to return the front of queue
    def getfront(self):
        return self.queue[self.front]

    # Function to return the rear of queue
    def getrear(self):
        return self.queue[self.rear]
      
    def traverse(self):
        
        if self.isEmpty():
            return 'Queue is Empty'
        
        elif self.rear >= self.front :
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end = " | ")
            print("\n")
        else:
            for i in range(self.front ,self.capacity):
                print(self.queue[i],end = " | ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end = " | ")
            print("\n")


        

# Driver Code

l = CircularLinkedList()
for i in range(5):
    l.addFront(i)
l.append(5)
l.traverse()
print(l.addAfter(55,10))
l.traverse()
l.addAfter(2,10)
l.addAfter(4,11)
l.addAfter(5,12)
l.traverse()



