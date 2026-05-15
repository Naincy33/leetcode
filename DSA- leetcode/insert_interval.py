class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        # 1️⃣ Left part: intervals completely before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2️⃣ Overlapping part: merge with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # insert merged newInterval
        res.append(newInterval)

        # 3️⃣ Right part: intervals after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
obj = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,9]
result = obj.insert(intervals, newInterval)
print(result)