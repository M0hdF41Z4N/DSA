# Implementation of 
# Double Ended Queue ( Dequeue )




# Method 1 :
# using circular array



class Queue:

    # Constructor
    def __init__(self,k):
        self.front = self.rear = -1
        self.capacity = k
        self.queue = [None] * self.capacity

    # Function to check if queue is empty
    def isEmpty(self):
        return self.front == -1

    # Function to check if queue is Full
    def isFull(self):
        return (self.front == self.rear+1 or (self.front == 0 and self.rear == self.capacity -1))

    # Function to add element in front
    def addFront(self,item):

        # Base Case : when queue is full
        if self.isFull():
            return "Queue is Full"
        
        # Case : when queue is empty
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = item
        
        # Case : when front is at first element
        elif self.front == 0:
            self.front = self.capacity -1
            self.queue[self.front] = item
        
        # Case : all other scenarios
        else:
            self.front -= 1
            self.queue[self.front] = item

    # Function to add element in rear
    def addRear(self,item):

        # Base Case : when queue is full
        if self.isFull():
            return "Queue is Full"

        # Case : when queue is empty
        if self.isEmpty():
            self.rear = self.front = 0
            self.queue[self.array] = item

        # Case : when rear is at last element
        elif self.rear ==  self.capacity-1:
            self.rear = 0
            self.queue[self.array] = item

        # Case : all other scenarios
        else:
            self.rear += 1
            self.queue[self.rear] = item

    
    # Function to delete element front front
    def deleteFront(self):
        
        # Base Case 
        if self.isEmpty() :
            return "Queue is Empty"

        data = self.queue[self.front]

        # Case : if front is at last
        if self.front == self.capacity -1:
            self.front = 0

        # Case : all other generic cases
        else:
            self.front += 1

        return data



    # Function to delete element fromt rear
    def deleteRear(self):

         # Base Case 
        if self.isEmpty() :
            return "Queue is Empty"

        data = self.queue[self.rear]

        # Case : if rear is at first
        if self.rear == 0:
            self.rear = self.capacity - 1

        # Case : all other generic cases
        else:
            self.rear -= 1

        return data
    
    def getFront(self):
        return self.queue[self.front]

    def getRear(self):
        return self.queue[self.rear]

    # Function to print the queue
    def traverse(self):

        # Base Case
        if self.isEmpty():
            return "Queue is Empty"
        
        # Case : when rear is greater than front
        if self.rear >= self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end = " | ")
        
        # Case : When front is greater than rear
        else:
            for i in range(self.front,self.capacity):
                print(self.queue[i],end = " | ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end = " | ")
        print("\n")



# Method 2 :
# using Doubly Linked List

class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class Queue:
    # Constructor
    def __init__(self):
        self.front = self.rear = None

    # Function to check if queue is empty
    def isEmpty(self):
        return self.front == None

    # Function to add element in front
    def addFront(self,item):
        
        newNode = Node(item)

        # Case : when queue is empty
        if self.isEmpty():
            self.front = self.rear = newNode
        
        # Case : all other scenarios
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = self.front.prev

        return
            
    # Function to add element in rear
    def addRear(self,item):

        newNode = Node(item)

        # Case : when queue is empty
        if self.isEmpty():
            self.front = self.rear = newNode

        # Case : all other scenarios
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = self.rear.next

        return

    # Function to delete element front front
    def deleteFront(self):
        
        # Base Case 
        if self.isEmpty() :
            return "Queue is Empty"

        data = self.front.data

        # Case : if front is at last
        if self.front == self.rear:
            self.front = self.rear = None

        # Case : all other generic cases
        else:
            self.front = self.front.next
            self.front.prev = None

        return data



    # Function to delete element fromt rear
    def deleteRear(self):

         # Base Case 
        if self.isEmpty() :
            return "Queue is Empty"

        data = self.rear.data

        # Case : if rear is at first
        if self.rear == self.front == 0:
            self.rear = self.front = None

        # Case : all other generic cases
        else:
            self.rear = self.rear.prev
            self.rear.next =  None
        
        return data
    

    # Function to get front
    def getFront(self):
        return self.front.data

    # Function to get rear
    def getRear(self):
        return self.rear.data

    # Function to print the queue
    def traverse(self):
        trav = self.front
        while trav :
            print(trav.data,end = " | ")
            trav = trav.next
        print("\n")



# Driver Code

q = Queue()
for i in range(6):
    q.addFront(i)



q.traverse()
q.addRear(7)
q.traverse()
print(q.deleteRear())
print(q.deleteRear())
q.traverse()
print(q.deleteFront())
q.traverse()
q.addFront(777)
q.traverse()
