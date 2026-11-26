class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        subset=[]
        def backtrack(start):
            res.append(subset[:])
            for i in range (start, len(nums)):
                if i>start and nums[i]== nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return res
        