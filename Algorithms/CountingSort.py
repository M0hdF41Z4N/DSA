# Implementation of Counting Sort


# Navie algorithm : limitation not working with negative number

def countingSort(nums):
    m = max(nums) # finding maximum in array 
    n = len(nums)
    # Initialize count array
    count = [0] * (m+1)
    output = [0] * n

    # Store the count of each elements in count array
    for i in range(n):
        count[nums[i]] += 1

    # Store the cummulative count
    for i in range(1,len(count)):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        output[count[nums[i]] - 1] =  nums[i]
        count[nums[i]] -= 1
        i -= 1

    # copy the output in array
    for i in range(len(output)):
        nums[i] = output[i]




# Driver Code

numbers = [9,8,6,2,0,3,5,6,12]
print("Before Soritng -> ",numbers)
countingSort(numbers)
print("After Sorting -> ",numbers)

# Working with negative numbers

def CountingSort(nums):
    mx = max(nums)  # finding maximum in array
    mn = min(nums)  # finding minimum in array
    rg = mx-mn+1    # defininf length of count array
    n = len(nums)   # length of array
    count = [0] * rg
    output = [0] * n

    # Store the count of each elements in count array
    for i in range(n):
        count[nums[i]-mn] += 1

    # Store the cummulative count
    for i in range(1,rg):
        count[i] += count[i-1]

    i = n-1
    while i >= 0 :
        output[count[nums[i]-mn]-1] = nums[i]
        count[nums[i]-mn] -= 1
        i -= 1

    for i in range(n):
        nums[i] = output[i]

# Driver Code

numbers = [9,8,6,2,0,3,5,6,12,-2]
print("Before Soritng -> ",numbers)
CountingSort(numbers)
print("After Sorting -> ",numbers)
