# Implementation of Insertion Sort


def InsertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key



# Driver Code
numbers = [4, 1, 3, 9, 7]
InsertionSort(numbers)
print(numbers)