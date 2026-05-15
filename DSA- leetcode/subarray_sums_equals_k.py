#Subarray Sum Equals K
#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

# ------------------------------------------
# BRUTE FORCE SOLUTION (O(n^2))
# ------------------------------------------

class SolutionBrute(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1

        return count


# Driver code / object
nums = [1, 2, 3]
k = 3

obj = SolutionBrute()
print("Brute Output:", obj.subarraySum(nums, k))
