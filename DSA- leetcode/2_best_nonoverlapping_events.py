class Solution(object):
    def maxTwoEvents(self, events):
        events.sort()
        n = len(events)

        maxFromRight = [0] * n
        maxFromRight[-1] = events[-1][2]

        for i in range(n-2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i+1], events[i][2])

        ans = 0

        for i in range(n):
            start, end, val = events[i]
            ans = max(ans, val)

            left, right = i + 1, n - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2
                if events[mid][0] >= end + 1:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if idx != -1:
                ans = max(ans, val + maxFromRight[idx])

        return ans
obj = Solution()
print(obj.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))