# leetcode 448
# input: [1, n]
# class Solution:
def findDisappearedNumbers(nums: list[int]) -> list[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

list_a = [3, 1, 4]

result = findDisappearedNumbers(list_a)
print(result)

