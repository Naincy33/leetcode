class Solution(object):
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        ops = 0

        while len(nums) > 1 and not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [min_sum] + nums[idx+2:]
            ops += 1

        return ops

obj= Solution()
nums=[2,2,-1,3,-2,2,1,1,1,0,-1]
result= obj.minimumPairRemoval(nums)
print(result) 