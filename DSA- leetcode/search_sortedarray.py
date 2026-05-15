""""Problem:
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def searchInsert(self, nums, target):
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found.
        If not, return the index where it would be if inserted in order.

        Must run in O(log n) time.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If target not found, left is the correct insertion index
        return left


# ✅ Object creation and function call
obj = Solution()   # creating object of Solution class

# Example inputs
nums = [1, 3, 5, 6]
target = 2

# Calling the method using object
result = obj.searchInsert(nums, target)

print("Insert position is:", result)
