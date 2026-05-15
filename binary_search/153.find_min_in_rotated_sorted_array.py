class Solution:
    def findMin(self, nums):
        
        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            # minimum right side me
            if nums[mid] > nums[high]:
                low = mid + 1

            # minimum left side me ya mid khud
            else:
                high = mid

        return nums[low]
# Time complexity: O(log n) where n is the length of the nums list
# Space complexity: O(1) for the constant space used by the pointers and variables
solution = Solution()
nums = [3, 4, 5, 1, 2]
print(solution.findMin(nums))