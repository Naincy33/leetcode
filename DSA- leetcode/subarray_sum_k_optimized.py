# ------------------------------------------
# OPTIMIZED SOLUTION (O(n))
# Prefix Sum + HashMap
# ------------------------------------------

class SolutionOptimized(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix_count = {0: 1}   # prefix sum = 0 seen once
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            # If prefix_sum - k exists, we found subarrays ending here
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]

            # Store current prefix_sum count
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count


# Driver code / object
nums = [1, 2, 3]
k = 3

obj = SolutionOptimized()
print("Optimized Output:", obj.subarraySum(nums, k))
