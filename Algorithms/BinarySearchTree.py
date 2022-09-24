# Implementation of Binary Search



# Iterative method

def BinarySearch(arr,key):
    l = 0
    h = len(arr)
    while l <= h :
        mid = (l+h)//2
        if arr[mid] == key :
            return mid
        elif arr[mid] < key:
            l=mid+1
        elif arr[mid] > key:
            h = mid-1
    return -1



# Recursive method

def RecursiveBinarySearch(arr,l,h,key):
    if h >= l:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return RecursiveBinarySearch(arr,mid+1,h,key)
        return RecursiveBinarySearch(arr,l,mid-1,key)
    return -1

