class Solution:
    def maxSubarraySumCircular(self, nums):
        
        total_sum = 0

        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        total_sum = nums[0]

        for i in range(1, len(nums)):

            total_sum += nums[i]

            # Maximum Subarray (Kadane)
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            # Minimum Subarray (Kadane)
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

        # All elements negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)
# Time complexity: O(n) for one pass through the array
# Space complexity: O(1) for constant space usage
solution = Solution()
nums = [1, -2, 7, -2]
print(solution.maxSubarraySumCircular(nums))  
nums = [5, -3, 5]
print(solution.maxSubarraySumCircular(nums))  # Output: 10