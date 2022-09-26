#            Queue Implementation using Singly Linked List

class Node:
    def __init__(self,data_val):
        self.data = data_val
        self.next = None

class Queue:
    # Constructor
    def __init__(self):
        self.front = self.rear = None

    # Function to check Queue is Empty
    def is_Empty(self):
        return self.front == None

    # Function to insert element in Queue
    def Enqueue(self,val):
        new_node = Node(val)
        if self.is_Empty() :
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
            

    # Function to delete an element from Queue
    def Dequeue(self):
        if  self.is_Empty() :
            return "Queue is Empty"
        temp = self.front
        self.front = self.front.next

        if self.front == None:
            self.rear = None
        return temp.data
        

    # Function to give front of the Queue
    def getfront(self):
        return self.front.data

    # Function to give rear of the Queue
    def getrear(self):
        return self.rear.data


    # Function to display queue
    def display(self):
        if self.is_Empty():
            return "Queue is Empty"
        copy = self.front
        while copy:
            print(copy.data,end=" | ")
            copy = copy.next
        print("\n")

    def peeking(self):
        return self.front.data

# Driver Code
if __name__== '__main__':
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.display()
    q.Dequeue()
    q.Dequeue()
    q.display()
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(50)
    q.display()
    q.Dequeue()
    q.display()
