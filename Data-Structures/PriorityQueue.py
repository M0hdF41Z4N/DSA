# Implementation of Priority Queue 
# Max to Min



class Queue:
    # Constructor
    def __init__(self):
        self.arr = []
        self.size = 0

    # Function to heapify the tree
    def heapify(self,arr,n,i):
        # Find the largest among root, left child and right child
        largest = i
        l = 2*i + 1
        r =  2*i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        # Swap and continue heapifying if root is not largest
        if i != largest:
            arr[i] , arr[largest] = arr[largest] , arr[i]
            self.heapify(arr,n,largest)


    def insert(self,item):
        if self.size == 0:
            self.arr.append(item)
            self.size += 1
        else:
            self.arr.append(item)
            self.size += 1
            for i in range((self.size//2)-1,-1,-1):
                self.heapify(self.arr,self.size,i)

    # Native approach to search in heap 
    def search(self,item):
        n = self.size
        for i in range(n):
            if self.arr[i] == item:
                return i
        return -1



    def delete(self,item):
        # base case
        if self.size == 0:
            return
        else:
            # find the item in the heap
            i = self.search(item)

            # if element is found in heap
            if i >= 0:
                # Swap with last item
                self.arr[i] , self.arr[-1] = self.arr[-1] , self.arr[i]
            
                # delete the last element
                self.arr = self.arr[:self.size-1]
                self.size -= 1

                # heapify the arr
                for i in range((self.size//2)-1,-1,-1):
                    self.heapify(self.arr,self.size,i)

            else:
                return i


    def Max(self):
        return self.arr[0]

    def traverse(self):
        print("Max-Heap array",self.arr)

    
# Driver Code

q = Queue()
for i in range(5):
    q.traverse()
    q.insert(i)
q.insert(5)
q.traverse()
q.delete(3)
q.traverse()

    

