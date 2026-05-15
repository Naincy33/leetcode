class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        for n in nums:
            ans ^= n
        return ans
obj=Solution()
print(obj.singleNumber([4,1,2,1,2]))  # Output