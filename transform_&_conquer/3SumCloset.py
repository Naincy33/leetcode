class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                curr_sum = nums[i] + nums[left] + nums[right]

                # update closest
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1

                elif curr_sum > target:
                    right -= 1

                else:
                    return curr_sum

        return closest
# Example usage:
solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2 (the sum that is closest to the target is