# Implementation of Bubble Sort

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

# driver code
numbers = [5,6,7,2,8,0,10]
print("Before Sorting  -> ",numbers)
BubbleSort(numbers)
print("After Sorting -> ",numbers)
