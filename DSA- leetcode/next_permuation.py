class SolutionOptimized:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If found, find next greater element on right and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse suffix (right side of pivot)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums


# 🔹 Example
nums = [1, 1, 5]
print("Optimized Output:", SolutionOptimized().nextPermutation(nums))  # [1, 5, 1]
