# Implementation of Bucket Sort



# The navie algorithm

#def bucketSort(nums):

#    # Creating Empty bucket
#    bucket = []
#    slot_num = 10 # 10 means 10 slots, each
#                  # slot's size is 0.1
#    for i in range(slot_num):
#        bucket.append([])

#    # Put array elements in different buckets 
#    for n in nums:
#        index = int(slot_num * n )
#        bucket[index].append(n)

#    # Sort individual buckets 
#    # Here , we're being lazy and using python in-built function
#    for _ in bucket:
#        _.sort()

#    # concatenate the result
#    k = 0 
#    for i in range(slot_num):
#        for j in range(len(bucket[i])):
#            nums[k] = bucket[i][j]
#            k += 1
    
#    return nums

#nums = [0.897, 0.565, 0.665,
#     0.1234, 0.656, 0.3434]

#bucketSort(nums)

#print(nums)

# Algorithm works with Negative values also



def BucketSort(nums,n):

    # Creating Empty Bucket
    bucket = []
    for i in range(n):
        bucket.append([])

    # Put array elements in different buckets
    for i in nums:
        index = int(n*i)
        bucket[index].append(i)

    # Sorting each bucket
    # Here , we're being lazy and using python in-built function
    for _ in bucket:
        _.sort()

    # concatenate the result
    k = 0 
    for i in range(n):
        for j in range(len(bucket[i])):
            nums[k] = bucket[i][j]
            k += 1
    
    return nums



def sortMixed(nums,n):
    Neg = []
    Pos = []

    # Dividing negative and positive elements in different buckets
    for x in nums:
        # Storing -ve values
        if x < 0:
            Neg.append(-1 * x)      # Key
        # Storing +ve values
        else:
            Pos.append(x)

    BucketSort(Neg,len(Neg))
    BucketSort(Pos,len(Pos))

    # First Gathering sorted -ve values in reverse order
    # by converting in -ve value
    for i in range(len(Neg)):
        nums[i] = -1 * Neg[len(Neg) - 1 - i]

    # Gathering sorted +ve values 
    for i in range(len(Neg),n):
        nums[i] = Pos[i-len(Neg)]

    return nums

# Driver Code

nums = [-0.897, 0.565, 0.656, -0.1234, 0, 0.3434]
sortMixed(nums,len(nums))
print(nums)


