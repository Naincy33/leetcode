class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            ans = max(ans, pair_sum)

        return ans
obj = Solution()
nums = [3,5,2,7,3]
result = obj.minPairSum(nums)
print(result)