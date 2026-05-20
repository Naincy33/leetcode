class Solution:
    def minSubArrayLen(self, target, nums):

        n = len(nums)

        i = 0
        total = 0
        ans = float('inf')

        for j in range(n):

            total += nums[j]

            while total >= target:

                ans = min(ans, j - i + 1)

                total -= nums[i]
                i += 1

        if ans == float('inf'):
            return 0

        return ans
# Time complexity: O(n) where n is the length of the nums list
# Space complexity: O(1) since we are using only a constant amount of extra space
solution = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target, nums))    