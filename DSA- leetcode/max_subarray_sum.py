# ✅ Question: Maximum Subarray Sum (Kadane's Algorithm)
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum
# and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        # Initialize with first element
        current_sum = 0
        max_sum = nums[0]

        # Traverse array
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            # If sum goes negative, reset it
            if current_sum < 0:
                current_sum = 0

        return max_sum


# 🎯 Example Run
obj = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Input:", nums)
print("Output:", obj.maxSubArray(nums))
