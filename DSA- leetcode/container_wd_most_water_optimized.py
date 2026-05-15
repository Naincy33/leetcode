class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans =0
        n= len(height)
        left= 0
        right = n-1
        while(left<right):
                width = (right-left)
                h = min(height[left], height[right])
                area= width * h
                ans= max(ans, area)

                if(height[left]<height[right]):
                    left+=1
                else:
                    right -=1
        return ans
    
obj = Solution()
arr =[1,3,5,2,6,9,11]
print(obj.maxArea(arr))