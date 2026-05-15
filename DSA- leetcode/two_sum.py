""""You are given an array of integers nums and an integer target.
Return the indices of the two numbers such that they add up to target.
You may assume that:
Each input has exactly one solution,
You may not use the same element twice.
You can return the answer in any order."""

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  # stores num -> index mapping

        for i, num in enumerate(nums):
            complement = target - num

            # if complement already seen, return indices
            if complement in hashmap:
                return [hashmap[complement], i]

            # else store current number with its index
            hashmap[num] = i
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))
