# Problem Statement #

# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

def findMissingNumber (nums : list[int]) -> int:
    i = 0
    n = len(nums)
    while (i < n) :
        j = nums[i]
        if j < n and  j != i:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(0, n):
        if nums[i] != i:
            return i

    return n

def findMissing (nums : list[int]) -> int:
    """ list_1 = [3, 2, 0], list_2 = [0, 1, 2, 3], 
        sum(list_2) - sum(list_1) = missing number """
    res = len(nums)
    # [1, len(nums-1)]
    for i in range(0, len(nums)):
        res += (i - nums[i])
    return res

# Time Complexity of findMissing(): O(n)
# Space Complexity for findMissing(): O(1)

def findMissingNum (nums : list[int]) -> int:
    i = 0
    n = len(nums)
    #print(len(num_2))
    while (i < n):
        print(" inside while: i:  " + str(i))
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i:
            return i

    return n

if __name__ == "__main__":
    print("method 1: ")
    arr = [8, 3, 9, 2, 4, 6, 0, 1]
    result= findMissingNumber (arr)
    print(result)

    print("method 2: ")
    list_a = [8, 3, 5, 2, 4, 6, 0, 1]
    result = findMissing(list_a)
    print(result)

    print("method 3: ")
    list_2 = [8, 3, 5, 2, 4, 6, 0, 1]
    # print(len(list_2))

    result_2 = findMissingNum (list_2)
    print(result_2)
    #for i in range (len(result_arr)):
    #    print(result_arr[i], end = ' ')
    
    
# Time complexity #
# The time complexity of the above algorithm is O(n). In the while loop, although we are not incrementing the index i when swapping the numbers, this will result in more than n iterations of the loop, but in the worst-case scenario, the while loop will swap a total of n-1 numbers and once a number is at its correct index, we will move on to the next number by incrementing i. In the end, we iterate the input array again to find the first number missing from its index, so overall, our algorithm will take O(n) + O(n-1) + O(n) which is asymptotically equivalent to O(n).

# Space complexity #
# The algorithm runs in constant space O(1).
