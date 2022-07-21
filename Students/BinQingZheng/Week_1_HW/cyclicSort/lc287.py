# Prblem Statement #

# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

def findDuplicate (nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i]-1
            #print(j)
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i] # swap
            else: # We have found the duplicate
                print(i)
                print(j)
                return nums[i]
        else:
            i += 1

    return -1

def findDuplicate_alt (nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1


    for i in range(len(nums)):
        if nums[i] != i+1:
            return nums[i]

    return -1

def main(): 

    my_list = [1, 4, 4, 3]
    result = findDuplicate (my_list)
    print(result)

    print("method 2: ")
    print(findDuplicate_alt(my_list))

main() 

# Time Complexity 
# The time complexity is O(n).

# Space complexity #
# The algorithm runs in constant space O(1) but modifies the input array.


