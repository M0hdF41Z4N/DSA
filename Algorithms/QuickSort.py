#   Quick Sort

# Recursice Method

def partition(arr,low,high):
    pivot = arr[high] # declaring last element as pivot
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            # swap
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr = [10,7,8,9,1,5]

print("Before Sorting",arr,end="\n")

quickSort(arr,0,len(arr)-1)

print("After Sorting",arr,end="\n")

