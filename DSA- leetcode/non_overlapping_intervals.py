class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        
        # sort by ending time
        intervals.sort(key=lambda x: x[1])
        
        remove = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # overlap → remove this interval
                remove += 1
            else:
                # no overlap → update prev_end
                prev_end = intervals[i][1]
        
        return remove
obj = Solution()
print(obj.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3],[1,5]]))  