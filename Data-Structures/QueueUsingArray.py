# Queue Implementation using Array



class Queue:

    # Constructor
    def __init__(self,k) -> None:
        self.capacity = k
        self.array = [None] * self.capacity
        self.front = self.rear = -1
        self.length = 0
        

    #def adjustIndex(self,index,size):
    #    return index - size if index >= size else index
    
    # Function to check wheather Queue is empty or not
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    # Function to check the size of the queue
    def size(self):
        return self.length

    # Function to return the peek of queue
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.array[self.front]

    # Function to check if queue if full
    def isFull(self):
        return self.rear == self.capacity - 1


    # Function to enqueue an element
    def Enqueue(self,item):
        if self.isFull():
            return "Queue is full"
        elif self.isEmpty():
            self.rear = self.front = 0
            self.array[self.rear] = item
            self.length += 1
        else:
            self.rear += 1
            self.array[self.rear] = item
            self.length += 1
        
       
    # Function to dequeue element
    def Dequeue(self):
        if self.isEmpty() :
            return "Queue is empty"
        else:
            data = self.array[self.front]
            self.array[self.front] = None # Memory Cleanup
            self.front += 1
            self.length -= 1
        return data

    # Function to display
    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.array[i],end=" | ")
            print("\n")


# Driver Code

q = Queue(3)
q.Enqueue(0)
q.Enqueue(0)
q.Enqueue(7)
q.traverse()






    


