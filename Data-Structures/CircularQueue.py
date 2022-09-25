# Implementation of Circular Queue

print("Hello Github")

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
    def getFront(self):
        return self.queue[self.front]

    # Function to return the rear of queue
    def getRear(self):
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

q = Queue(12)
q.enqueue(6)
q.enqueue(8)
q.enqueue(7)
q.traverse()



