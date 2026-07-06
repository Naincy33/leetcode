class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        prev = intervals[0]
        count = 1

        for current in intervals[1:]:
            if current[1] <= prev[1]:
                # current is covered
                continue
            else:
                prev = current
                count += 1

        return count 