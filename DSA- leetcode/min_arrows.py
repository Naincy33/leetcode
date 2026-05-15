class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if not points:
            return 0

        points.sort(key=lambda x:x[1])

        arrows =1

        end= points[0][1]

        for start, curr_end in points:
            if start >end :
                arrows+= 1
                end = curr_end
        return arrows
obj= Solution()
print(obj.findMinArrowShots([[10,16],[2,5],[1,6],[7,12]]))  # Output: 2