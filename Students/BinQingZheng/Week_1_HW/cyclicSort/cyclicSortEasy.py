#  Problem Statement #

#  We are given an array containing ‘n’ objects. 
# Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
# This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

#  Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

#from typing import List

# cyclic sort
def cyclicSort (nums: list[int]) -> list[int]: 
    # def cyclicSort (self, nums: List[int]) -> int: ( needed from typing to import List line 10)
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        else: 
            i += 1
    return nums

if __name__ == "__main__":
    nums = [1, 5, 6, 4, 3, 2]
    n = len(nums)
    cyclicSort(nums)
    print("After sorted : ")
    for i in range(0, n):
        print(nums[i], end = ' ')

# Time complexity # 
#  Time complexity is O(n).

# def containsDuplicate(self, nums: List[int]) -> bool:

# Driver code
# if __name__ == "__main__":
   # arr = [1, 1, 2, 1, 3, 5, 1]
    # n = len(arr)

# def function_name(parameter: data_type) -> return_type:
   # """Doctring"""
    # body of the function
    # return expression