class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        max_area=0

        for i in range(n):
            h= heights[i]

            left=i
            while left>0 and heights[left-1]>=h:
                left-=1

            right=i
            while right<n-1 and heights[right+1]>=h:
                right+=1

            width= right-left+1
            max_area= max(max_area,h*width)
        
        return max_area
obj= Solution()
print(obj.largestRectangleArea([2,1,5,4,2,3]))  