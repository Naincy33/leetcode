# ✅ Question: Product of Array Except Self
# Given an array nums, return an array answer such that answer[i]
# is equal to the product of all elements of nums except nums[i].
# You must solve it without using division and in O(n) time.

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Step 1: calculate prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: multiply with suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# 🎯 Example Run
obj = Solution()
nums = [1, 2, 3, 4]
print("Input:", nums)
print("Output:", obj.productExceptSelf(nums))
