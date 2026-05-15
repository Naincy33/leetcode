class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans =0
        n= len(height)
        for i in range(0,n):
            for j in range(i+1, n):
                width = (j-i)
                h = min(height[i], height[j])
                area= width * h

                ans= max(ans, area)
        return ans
    
obj = Solution()
arr = [1,8,6,2,8,4,8,3,10]
print(obj.maxArea(arr))