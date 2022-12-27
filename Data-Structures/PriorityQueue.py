# Implementation of Priority Queue using binary Heap
# Max to Min

import sys

class Priority_Queue:
    # Constructor
    def __init__(self):
        self.heap = []
        self.size = 0

    # Function to insert element in priority queue, O(log(n))
    def insert(self,item):
        self.heap.append(item)
        self.size += 1
        # call to helping function to maintian the heap property
        self.swim(self.get_size()-1)
           

    # Native approach to search in heap , O(n)
    def search(self,item):
        n = self.get_size()
        for i in range(n):
            if self.heap[i] == item:
                return i
        return -1

    # Function to get the size of priority queue
    def get_size(self):
        return self.size
    
    # Function to check if priority queue is empty or not
    def is_empty(self):
        return self.get_size() == 0

    # Function to get the max element in the priority queue, O(1)
    def get_max(self):
        #  returning -Infinity if priority queue is empty
        if self.is_empty():
            return -sys.maxsize
        return self.heap[0]
    
    # Function to delete and return the maximum element 
    # present in the priority queue. Return -Infinity if priority queue is empty.
    # O(log(n))
    def poll(self):
        #  returning -Infinity if priority queue is empty
        if self.is_empty():
            return -sys.maxsize
        return self.remove_at(0)

    # Perform bottom up node swim, O(log(n))
    def swim(self,child):
        # Grab the index of the next parent node WRT to k
        parent = (child - 1) // 2

        # Keep swimming while we have not reached the
        # root and while we're less than our parent.
        while (child > 0 and (self.heap[child] > self.heap[parent])):
            # Exchange child with the parent
            self.heap[child] , self.heap[parent] = self.heap[parent] , self.heap[child]
            
            child = parent

            # Grab the index of the next parent node WRT to k
            parent = (child - 1) // 2

    # Top down node sink, O(log(n))
    def sink(self,child,n):
        largest = child
        l = 2*child+1
        r = 2*child+2

        # Checking if left child is greater
        if l < n and (self.heap[largest] < self.heap[l]):
            largest = l
            
        # Checking if right child is greater
        if r < n and (self.heap[largest] < self.heap[r]):
            largest = r

        # Changing root if needed
        if largest != child:
            self.heap[child],self.heap[largest] = self.heap[largest] , self.heap[child]

            # Heapify the root
            self.sink(largest,n)

    # Removes a node at particular index, O(log(n))
    def remove_at(self,index):
        data = -sys.maxsize
        if not self.is_empty():
            data = self.heap[index]
            self.heap[index] , self.heap[self.get_size()-1] = self.heap[self.get_size()-1] , self.heap[index]
            
            # Removing the data
            self.heap.pop()
            self.size -= 1

            # Try sinking element
            self.sink(index,self.get_size())

        return data
        
    # O(n)
    def remove(self,item):
        if (item == None): return 
        # Linear removal via search, O(n)
        index = self.search(item)
        if index != -1:
            return self.remove_at(index)

    def traverse(self):
        print("Max-Heap array",self.heap)


# Driver Code

pq = Priority_Queue()


# Sampele test case 1:

# pq.insert(3)
# pq.insert(4)
# pq.insert(63)
# pq.insert(21)
# pq.insert(9)
# print(pq.get_max())
# print(pq.poll())
# pq.insert(7)
# print(pq.get_max())
# print(pq.get_max())
# print(pq.get_max())
# print(pq.poll())

# pq.traverse()

# Sampele test case 2:

# pq.insert(3)
# pq.insert(4)
# pq.insert(63)
# pq.insert(21)
# pq.insert(9)
# print(pq.get_max())
# print(pq.poll())
# pq.insert(7)
# print(pq.get_max())
# print(pq.poll())
# print(pq.get_max())

# pq.traverse()

# Sampele test case 3:

pq.insert(3)
pq.insert(4)
pq.insert(63)
pq.insert(21)
pq.insert(9)
print(pq.get_max())
print(pq.poll())
pq.insert(7)
print(pq.poll())
print(pq.get_size())
print(pq.is_empty())

pq.traverse()

