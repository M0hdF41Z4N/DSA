# Queue implementation using Doubly Linked list

class Node:
    
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class Queue:
    
    def __init__(self):
        self.front = self.rear = None
        self.length = 0

    def isEmpty(self):
        return self.front == None

    def peek(self):
        return self.front.data

    def size(self):
        return self.length

    def Enqueue(self,item):
        new_node = Node(item)
        if self.isEmpty() :
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
            
        self.length += 1


    def Dequeue(self):
        if self.isEmpty():
            return
        data = self.front.data
        if self.front == self.rear :
            self.front = self.rear = None
        
        else :
            self.front = self.front.next
            self.front.prev = None
        if self.front == None:
            self.rear = None

        self.length -= 1
        
        return data

    def Display(self):
        if self.isEmpty() :
            return "Queue is Empty"
        else:
            copy = self.front
            while copy:
                print(copy.data,end=" | ")
                copy = copy.next
            print("\n")

# Driver Code

q = Queue()
print(q.isEmpty())
q.Enqueue(7)
q.Enqueue(8)
q.Enqueue(6)
print(q.peek())
q.Display()
print(q.Dequeue())
q.Display()
q.Dequeue()
q.Display()
q.Dequeue()
print(q.Display())



