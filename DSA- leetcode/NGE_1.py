class Solution:
    def nextGreaterElement(self, nums1, nums1Size, nums2, nums2Size):
        stack = []
        nge_map = {}  # value -> next greater element
        
        # Process nums2 to build mapping of next greater elements
        for num in nums2:
            while stack and num > stack[-1]:
                nge_map[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements have no next greater
        while stack:
            nge_map[stack.pop()] = -1
        
        # Build result using nums1 order
        return [nge_map[num] for num in nums1]

obj= Solution()
print(obj.nextGreaterElement([4,1,2],3,[1,3,4,2],4))  # Output: [-1,3,-1]