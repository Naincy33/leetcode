class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1
# Example usage:
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1,