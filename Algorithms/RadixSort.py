# Implementation of Radix Sort


def countingSort(nums,place):
    n = len(nums)
    mx = max(nums)
    output = [0] * n
    count = [0] * (mx+1)

    # Calculate count of elements
    for i in range(n):
        index = nums[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = n-1
    while i >= 0 :
        index = nums[i] // place
        output[count[index % 10] -1 ] = nums[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, n):
        nums[i] = output[i]


def radixSort(nums):
    mx = max(nums)
    place = 1
    while mx // place > 0:
        countingSort(nums,place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]
print("Before Sorting -> ",data)
radixSort(data)
print("After Sorting -> ",data)