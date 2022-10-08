# Heap Sort

def heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    # Checking if left child is greater
    if l < n and arr[largest] < arr[l]:
        largest = l
        
    # Checking if right child is greater
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Changing root if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest] , arr[i]

        # Heapify the root
        heapify(arr,n,largest)

# Function to build Heap
def buildHeap(arr,n):
    for i in range((n//2),-1,-1):
        heapify(arr,n,i)
    
# Function for heap sort
def heapSort(arr,n):
    
    # call to build heap
    buildHeap(arr,n)

    for i in range(n-1,0,-1):
        # Swap
        arr[i] , arr[0] = arr[0] , arr[i]

        # Heapify root element
        heapify(arr,i,0)

        

numbers = [1,2,3,9,10,11,6,7,5]
print("Before Sorting -> ",numbers)
heapSort(numbers,len(numbers))
print("After Sorting -> ",numbers)
